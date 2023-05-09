#!/usr/bin/bash
#SBATCH --dependency=singleton
#SBATCH --partition=contrib-gpu
#SBATCH --cpus-per-task=1
#SBATCH --exclude=
#SBATCH --constraint=
#SBATCH --mail-user=dyunis@ttic.edu
#SBATCH --mail-type=FAIL
#SBATCH --job-name=sfp_antmaze_large_seed0
#SBATCH --output=/share/data/speech/Data/dyunis/exps/wandb/sfp/logs/antmaze_large/slurm/%j.out
#SBATCH --error=/share/data/speech/Data/dyunis/exps/wandb/sfp/logs/antmaze_large/slurm/%j.err

env
source "/share/data/speech/Data/dyunis/envs/bet/miniconda3/bin/activate"

cd /home-nfs/dyunis/sfp_fork
python main.py --exp_name antmaze_large_0 --env antmaze-large-diverse-v1 --log_output_dir /share/data/speech/Data/dyunis/exps/wandb/sfp/logs/antmaze_large --seed 0
