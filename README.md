# Code and data to fine-tune a general model for event classification as well as ROBE experts

## usage

We fine-tune all models on Snellius: run train_single_model.sh to fine-tune a model. Parameters should be adjusted in this file as well as in _finetune_with_click.py_ to change the label set (depending on the expert) and possibly hyperparameters like the amount of epochs (default = 20) 

## evaluation

We have a separate repository dedicated to evaluating the models: https://github.com/globalise-huygens/nlp-event-classifier-evaluation/blob/main/README.md
