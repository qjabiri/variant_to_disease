import os
import csv

def listmaker(dic):
    # Define the header based on your new data fields
    writerlist = [["VariationID", "VariationName", "VariationType", "Assembly", "Chr", 
                   "display_start", "display_stop", "start", "stop", "variantLength", "positionVCF", 
                   "referenceAlleleVCF", "alternateAlleleVCF", "condition", "FILTER", "AF_joint", 
                   "AF_genomes", "AF_exomes"]]

    for key, val in dic.items():
        tmp = list(key)  # Start with the key components
        tmp.extend(val)  # Add the value components
        writerlist.append(tmp)

    return writerlist

def merge(gnomad_dir, unique_file, output_file):
    dic = dict()

    # Load unique file into a dictionary
    with open(unique_file, 'r') as file:
        for line in file:
            row = line.split(",")
            print(row)
            if len(row) < 13:  # Ensure there are at least 13 columns
                #print(f"Skipping row due to insufficient columns: {row}")
                continue
            key = (row[4], row[10], row[11], row[12])  # Chr, positionVCF, referenceAlleleVCF, alternateAlleleVCF
            dic[key] = row[:14]  # Store the first 154 columns initially (up to condition)

    # Process each chromosome file
    for i in range(1, 23):  # Chromosomes 1-22
        dic = process_chromosome(gnomad_dir, str(i), dic)

    # Process chromosome X
    dic = process_chromosome(gnomad_dir, 'X', dic)
    # Process chromosome Y
    dic = process_chromosome(gnomad_dir, 'Y', dic)

    for key, val in dic.items():
        if len(val) < 18:  # 15 original + 3 gnomAD columns = 18
            val.extend(['none'] * (18 - len(val)))

    # Write to output CSV
    writerlist = listmaker(dic)
    with open(output_file, 'w', newline='') as a:
        writer = csv.writer(a, delimiter=',')
        # Write the header
        writer.writerow(writerlist[0])
        # Write the data rows
        writer.writerows(writerlist[1:])

def process_chromosome(gnomad_dir, chrom, dic):
    filepath = os.path.join(gnomad_dir, f'gnomad_chr{chrom}_p.csv')
    print(f"Processing chromosome: {chrom}")
    if os.path.isfile(filepath):
        with open(filepath) as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)  # Skip header
            for row in reader:
                key = (row[0].lstrip('chr'), row[1], row[3], row[4])  # #CHROM, POS, REF, ALT

                if key in dic:
                    dic[key].extend([row[6], row[8], row[9], row[10]])  # Add FILTER, AF_joint, AF_genomes, AF_exomes
                    print("yay")
    return dic

# Example usage
gnomad_dir = '/cta/users/qaljabiri/pure/data/gnomad_data'  # Path to the directory containing gnomAD CSV files
unique_file = '/cta/users/qaljabiri/pure/data/output_variations.csv'  # Replace with your unique CSV file path
output_file = '/cta/users/qaljabiri/pure/data/xml_gnomad22.csv'  # Replace with your desired output CSV file path

merge(gnomad_dir, unique_file, output_file)
