#!/bin/bash
#
# -= Resources =-
#SBATCH --job-name=cpdGB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
##SBATCH --mem 24G
#SBATCH --account=users
#SBATCH --qos=long_mdbf
#SBATCH --partition=long_mdbf
#SBATCH --time=7-00:00:00
#SBATCH --output=gnomad_pruner_%j-slurm.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=qjabiri@gmail.com
##SBATCH --array=0-1
#SBATCH --cpus-per-task=1

# Define input and output paths
INPUT="/cta/users/qaljabiri/pure/data/gnomad.joint.v4.1.sites.chrY.vcf.bgz"
OUTPUT="/cta/users/qaljabiri/pure/data/gnomad_chrY_p.csv"

# Run the Python script with the specified input and output
python3 gnomad_pruner3.py --input $INPUT --output $OUTPUT

