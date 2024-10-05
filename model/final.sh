#!/bin/bash

#
# -= Resources =-

#SBATCH --job-name=mut_compare
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
##SBATCH --mem 1500G
#SBATCH --account=users
#SBATCH --qos=long_mdbf
#SBATCH --partition=long_mdbf
#SBATCH --time=7-00:00:00
#SBATCH --output=mut_compare_%j-slurm.out
##SBATCH --mail-type=ALL
#SBATCH --cpus-per-task=1

# Define variables for input files
INDIVIDUAL_NAME="JohnDoe"
INDIVIDUAL_FILE="/cta/users/qaljabiri/pure/data/dv_variants_variant_snpeff_ann.csv"
MASTER_FILE="/cta/users/qaljabiri/pure/data/final_tsv_output_with_phactboost.csv"

# Run the Python script with the input arguments
python3  final_model4.py "$INDIVIDUAL_NAME" "$INDIVIDUAL_FILE" "$MASTER_FILE"

