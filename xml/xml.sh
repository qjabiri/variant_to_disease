#!/bin/bash

#

# -= Resources =-

#SBATCH --job-name=cpdGBi

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=1

##SBATCH --mem 1500G

#SBATCH --account=users

#SBATCH --qos=long_mdbf

#SBATCH --partition=long_mdbf

#SBATCH --time=7-00:00:00

#SBATCH --output=xml_worker_%j-slurm.out

##SBATCH --mail-type=ALL

##SBATCH --array=0-1

#SBATCH --cpus-per-task=1

##INPUT_VCF="/cta/users/qaljabiri/pure/data/extracted_variations_line_by_line3.csv"
##OUTPUT_CSV="/cta/users/qaljabiri/pure/data/cleaned_xml.csv"

python3 phact_merg4.py  ## --input "$INPUT_VCF" --output "$OUTPUT_CSV"


