import os
import csv

def listmaker(dic):
    # Define the header based on your data fields
    writerlist = [["AlleleID", "Type", "Name", "GeneID", "GeneSymbol", "HGNC_ID", "ClinicalSignificance",
                   "ClinSigSimple", "RS# (dbSNP)", "nsv/esv (dbVar)", "RCVaccession", "PhenotypeIDS",
                   "PhenotypeList", "Assembly", "Chromosome", "Start", "Stop", "ReferenceAllele",
                   "AlternateAllele", "PositionVCF", "ReferenceAlleleVCF", "AlternateAlleleVCF",
                   "FILTER", "AF_joint", "AF_genomes", "AF_exomes"]]

    for key, val in dic.items():
        # No need to prepend the key; just append the values
        writerlist.append(val)

    return writerlist

def merge(gnomad_dir, unique_file, output_file):
    dic = dict()

    # Load unique file into a dictionary
    print("Loading unique file into dictionary...")
    with open(unique_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        print(f"Header: {header}")
        for row in reader:
            key = (row[14], row[-3], row[-2], row[-1])  # Chromosome, PositionVCF, ReferenceAlleleVCF, AlternateAlleleVCF
            dic[key] = row[:22]  # Store the first 22 columns initially (up to AF_exomes)

    print(f"Loaded {len(dic)} unique records from the file.")

    # Process each chromosome file
    for i in range(1, 23):  # Chromosomes 1-22
        dic = process_chromosome(gnomad_dir, str(i), dic)

    # Process chromosome X
    dic = process_chromosome(gnomad_dir, 'X', dic)
    # Process chromosome Y
    dic = process_chromosome(gnomad_dir, 'Y', dic)

    for key, val in dic.items():
        if len(val) < 26:  # 22 original + 4 gnomAD columns = 26
            val.extend(['none'] * (26 - len(val)))
    
    # Write to output CSV
    writerlist = listmaker(dic)
    print("Writing to output CSV...")
    with open(output_file, 'w', newline='') as a:
        writer = csv.writer(a, delimiter=',')
        # Write the header
        writer.writerow(writerlist[0])
        # Write the data rows
        writer.writerows(writerlist[1:])
    
    print("Finished writing to output CSV.")

def process_chromosome(gnomad_dir, chrom, dic):
    filepath = os.path.join(gnomad_dir, f'gnomad_chr{chrom}_p.csv')
    print(f"Processing chromosome {chrom}...")
    if os.path.isfile(filepath):
        with open(filepath) as f:
            reader = csv.reader(f, delimiter='\t')
            header = next(reader)  # Skip header
            print(f"Header: {header}")
            for row in reader:
                key = (row[0].lstrip('chr'), row[1], row[3], row[4])  # #CHROM, POS, REF, ALT

                if key in dic:
                    dic[key].extend([row[6], row[8], row[9], row[10]])  # Add FILTER, AF_joint, AF_genomes, AF_exomes
                    print(f"Updated record for key {key}.")
    else:
        print(f"File {filepath} not found.")
    return dic

# Example usage
gnomad_dir = '/cta/users/qaljabiri/pure/data/gnomad_data'  # Path to the directory containing gnomAD CSV files
unique_file = '/cta/users/qaljabiri/pure/data/clean_tsv.csv'  # Replace with your unique CSV file path
output_file = '/cta/users/qaljabiri/pure/data/combined2.csv'  # Replace with your desired output CSV file path

merge(gnomad_dir, unique_file, output_file)

