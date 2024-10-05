Project: gnomAD Data Download and Processing
This project consists of a shell script for downloading genomic data from gnomAD using Google Cloud and a Python script for processing and pruning the downloaded data. These scripts are intended for researchers who need to manage and analyze large genomic datasets efficiently.
Table of Contents
1. Overview
2. Files
   * gnomad_download.sh
   * gnomad_pruner3.py
3. Requirements
4. Usage
5. License
Overview
The project includes a Bash script for downloading gnomAD genomic data from Google Cloud Storage and a Python script for pruning and processing the downloaded variant data. These tools are crucial for preparing genomic data for further research and analysis.
Files
gnomad_download.sh
* Purpose: This Bash script is designed to download variant call format (VCF) files from the gnomAD public dataset hosted on Google Cloud Storage. It uses gsutil, a command-line utility for interacting with cloud storage, to fetch specific chromosome data.
* Key Features:
   * Downloads VCF files for chromosomes 21, 22, X, and Y from the gnomAD release 4.1.
   * Utilizes parallel processing (-m flag with gsutil) to speed up the download.
   * Saves downloaded files to the specified directory (/cta/users/qaljabiri/pure/data).
* Script Overview:
The script uses SLURM workload manager directives for resource allocation, which suggests it's intended to run on a high-performance computing (HPC) environment. It sets parameters like job name, number of nodes, memory allocation, and time limit, ensuring efficient use of resources​(gnomad_download).
Usage:
bash
Copy code
sbatch gnomad_download.sh
   * This command will submit the job to the SLURM scheduler, which will handle the execution of the download tasks.
gnomad_pruner3.py
   * Purpose: This Python script is intended to prune and process the gnomAD VCF files downloaded using the gnomad_download.sh script. It filters out unnecessary data, keeping only the relevant genomic variants for further analysis.
   * Key Features:
   * Parses VCF files to extract specific variant information.
   * Filters data based on predefined criteria (e.g., removing non-coding variants).
   * Outputs a refined dataset suitable for downstream analysis.
Usage:
bash
Copy code
python gnomad_pruner3.py
   * Before running the script, ensure that the VCF files are in the expected directory and that any required Python dependencies are installed.
Requirements
   * gnomad_download.sh:
   * Google Cloud SDK (gsutil)
   * SLURM workload manager (for job scheduling)
   * Access to a high-performance computing environment (recommended)
   * gnomad_pruner3.py:
   * Python 3.x
   * Required Python libraries (install using pip):
   * pandas (for data manipulation)
   * vcf (for parsing VCF files)
You can install the required Python packages using the following command:
bash
Copy code
pip install pandas pyvcf
   * Usage
   1. Download gnomAD Data:
Use the gnomad_download.sh script to download the VCF files from Google Cloud Storage:
bash
Copy code
sbatch gnomad_download.sh
   *    2. Prune and Process VCF Data:
Use the gnomad_pruner3.py script to process the downloaded VCF files:
bash
Copy code
python gnomad_pruner3.py
   *    3. Ensure that the VCF files are located in the specified directory (/cta/users/qaljabiri/pure/data) and that the environment is set up correctly.