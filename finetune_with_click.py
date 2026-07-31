import ast
import torch
import transformers
from transformers import set_seed, AutoModelForTokenClassification, TrainingArguments, Trainer, DataCollatorForTokenClassification
from get_data_selection import get_filepath_list, file_selection_invnr
from utils import construct_datadicts, initiate_tokenizer
from datasets import Dataset
import evaluate
import numpy
import json
import os
from datetime import date
import click
from select_id2label_experts import select_labeldicts
from select_id2label import select_labeldicts_all

OUTPUT_PATH = 'expert_models/violence2/' # adapt

def create_settings(root_path, inv_nr, tokenizername, modelname, seed):
    """
    Creates a dictionary containing information necessary for finetuning as well as metadata necessary for
    analysis further down the line. The dictionary will contain
    - data on the document that will be NOT finetuned but tested on:
        - filename
        - round in which it was annotated
        - inventory number of the document (which we use as identifier)
        - page numbers of the document
        - year the document was written in
        - range of half a century in which this yeat falls
    - data on the finetuning settings
        - model to be used
        - tokenizer to be used
        - seed to be used
        - list of labels in finetuning task
    """
    settings = file_selection_invnr(root_path, inv_nr)
    settings['tokenizer'] = tokenizername
    settings['model'] = modelname
    settings['seed'] = seed
    return(settings)

def initiate(settings, root_path, label_parameter):
    """
    prepares for finetuning by loading the correct tokenizer, getting paths to the training data and initiating a pre-trained model
    """
    tokenizername = settings['tokenizer']
    tokenizer = initiate_tokenizer(settings)
    testfile_names = settings['metadata_testfile']['original_filename']
    filepaths = get_filepath_list(root_path)

    id2label, label2id = select_labeldicts(label_parameter)
    num_labels = len(id2label)

    model = AutoModelForTokenClassification.from_pretrained(
        settings['model'], num_labels=num_labels, id2label=id2label, label2id=label2id
    )

    data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

    return(tokenizername, tokenizer, testfile_names, filepaths, model, data_collator)



@click.command()
@click.option('--seed', type=click.INT)
@click.option('--inv_nr', type=click.STRING)
@click.option('--root_path', type=click.STRING)
@click.option('--tokenizername', type=click.STRING)
@click.option('--modelname', type=click.STRING)
@click.option('--label_parameter', type=click.STRING)
def main(root_path, inv_nr, tokenizername, modelname, seed, label_parameter):
    """
    finetunes a model
    """
    # check versioning on external server
    print("VERSIONS")
    print(transformers.__version__)
    print(evaluate.__version__)

    label2id = select_labeldicts(label_parameter)

    # on snellius: 4.32.1
    # 0.4.2

    # set a seed to make sure results are reproducible
    set_seed(seed)
    torch.backends.cudnn.deterministic = True
    today = date.today()
    seqeval = evaluate.load("seqeval")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # load settings according to parameters given via click
    settings = create_settings(root_path, inv_nr, tokenizername, modelname, seed)

    # prepare tokenizer, paths to training data, load pre-trained model and data collator
    tokenizername, tokenizer, testfile_names, filepaths, model, data_collator = initiate(settings, root_path, label_parameter)

    # prepare the data as extracted from Inception to a json file that can be finetuned with
    prepared_tr, train_data, test_data, prepared_te = construct_datadicts(tokenizername, tokenizer, filepaths, testfile_names, label_parameter)
    train = Dataset.from_list(train_data)
    test = Dataset.from_list(test_data)

    for param in model.parameters(): param.data = param.data.contiguous()

    def compute_metrics(p):
        """
        computes scores per eval_step and saves predictions in settings file
        """
        predictions, labels = p
        predictions = numpy.argmax(predictions, axis=2)

        print(predictions)

        true_predictions = [
            [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]

        settings['predictions'] = true_predictions

        true_labels = [
            [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]

        settings['gold'] = true_labels

        results = seqeval.compute(predictions=true_predictions, references=true_labels)

        return {
            "precision": results["overall_precision"],
            "recall": results["overall_recall"],
            "f1": results["overall_f1"],
            "accuracy": results["overall_accuracy"],
        }

    # set parameters
    learning_rate = 5e-5
    per_device_train_batch_size = 16
    per_device_test_batch_size = 16
    num_train_epochs = 20 #adapt
    weight_decay = 0.01

    settings['training_args'] = {'learning_rate': learning_rate, 'per_device_train_batch_size': per_device_train_batch_size, 'num_train_epochs': num_train_epochs, 'weight_decay': weight_decay}

    training_args = TrainingArguments(
        output_dir="expert_models/violence2/",
        learning_rate=learning_rate,
        per_device_train_batch_size=per_device_train_batch_size,
        per_device_eval_batch_size=per_device_test_batch_size,
        num_train_epochs=num_train_epochs,
        weight_decay=weight_decay,
        evaluation_strategy="epoch", # eval_strategy when using transformers 4.43.2
        save_strategy="epoch",
        save_total_limit=1,
        load_best_model_at_end=False,
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train,
        eval_dataset=test,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )
    print("Start training")

    # train
    trainer.train()

    # make sure the settings file containing predictions for each file with metadata are saved
    # this code assumes a folder structure where OUTPUT_PATH branches out in folders with names SEED_MODEL (for example 888_GysBERT)
    try:
        modelname = settings['model'].split('/')[1]
    except IndexError: 
        modelname = settings['model']

    with open(OUTPUT_PATH+'/settings'+str(today)+'.json', 'w') as fp:
        json.dump(settings, fp)

if __name__ == '__main__':
    main()
