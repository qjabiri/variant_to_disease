import gzip
import re
import argparse

# Function to extract specific fields from the INFO column
def extract_info(info, field):
    hold = info.split(";")
    match = []
    for i in hold:
        if field in i:
            match = i.split("=")
            return match[1] 
    return None

# Argument parser to get input and output file paths
parser = argparse.ArgumentParser(description='Process VCF file.')
parser.add_argument('--input', required=True, help='Path to the input VCF file (gzipped)')
parser.add_argument('--output', required=True, help='Path to the output TSV file')
args = parser.parse_args()

# Open the gzipped VCF file and read it
with gzip.open(args.input, 'rt') as infile, open(args.output, 'w') as outfile:
    # Write header for output file
    outfile.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tAF\tAF_joint\tAF_genomes\tAF_exomes\n")
    
    for line in infile:
        if line.startswith('##'):
            continue  # Skip meta-information lines
        if line.startswith('#'):
            continue  # Skip the header line
        
        # Split the line into columns
        columns = line.strip().split('\t')
        
        # Extract the necessary columns
        chrom = columns[0]
        pos = columns[1]
        vid = columns[2]
        ref = columns[3]
        alt = columns[4]
        qual = columns[5]
        flt = columns[6]
        info = columns[7]
        
        # Extract AF, AF_joint, AF_genomes, AF_exomes from INFO column
        af = extract_info(info, 'AF=')
        af_joint = extract_info(info, 'AF_joint=')
        af_genomes = extract_info(info, 'AF_genomes=')
        af_exomes = extract_info(info, 'AF_exomes=')
        
        # Write the selected columns to the output file
        outfile.write(f"{chrom}\t{pos}\t{vid}\t{ref}\t{alt}\t{qual}\t{flt}\t{af}\t{af_joint}\t{af_genomes}\t{af_exomes}\n")
