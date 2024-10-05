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

gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr11.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr12.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr13.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr14.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr15.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr16.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr17.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr18.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr19.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
gsutil -m cp -r gs://gcp-public-data--gnomad/release/4.1/vcf/joint/gnomad.joint.v4.1.sites.chr20.vcf.bgz /cta/users/nncurabaz/ummu_kulsum
