#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=18
#SBATCH --gpus=1
#SBATCH --partition=gpu_a100
#SBATCH --time=2:00:00
#SBATCH --output=violence2.out

module load 2023
module load Python/3.11.3-GCCcore-12.3.0
module load PyTorch/2.1.2-foss-2023a-CUDA-12.1.1


#Execute a Python program located in $HOME, that takes an input file and output_with_3598 directory as arguments.

# Define arguments
inv_nr='3598' #of eval doc
modelname='globalise/GloBERTise'
seed=21102024

#do
python finetune_with_click.py \
    --seed=$seed \
    --inv_nr="$inv_nr" \
    --root_path="data/json_per_doc_class_IO/" \
    --tokenizername="$modelname" \
    --modelname="$modelname" \
    --label_parameter="violence"
#done

