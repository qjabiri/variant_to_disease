#!/bin/bash
#
# -= Resources =-
#SBATCH --job-name=cpdGB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
##SBATCH --mem 24G
#SBATCH --account=users
#SBATCH --qos=mid_mdbf
#SBATCH --partition=mid_mdbf
#SBATCH --time=20:00:00
#SBATCH --output=gnomad_download_%j-slurm.out
##SBATCH --mail-type=ALL
##SBATCH --array=0-1
#SBATCH --cpus-per-task=1
# Load any required modules (e.g., Google Cloud SDK)
module load google-cloud-sdk
# Activate your virtual environment if needed
# source /path/to/your/venv/bin/activate
# Run the gsutil download command


gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr21.vcf.bgz /cta/users/qaljabiri/pure/data
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr22.vcf.bgz /cta/users/qaljabiri/pure/data
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chrX.vcf.bgz /cta/users/qaljabiri/pure/data
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chrY.vcf.bgz /cta/users/qaljabiri/pure/data
