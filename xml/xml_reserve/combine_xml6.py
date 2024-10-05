import os
import csv

def listmaker(dic):
    # Define the header based on your new data fields
    writerlist = [["VariationID", "VariationName", "VariationType", "Assembly", "Chr", 
                   "display_start", "display_stop", "start", "stop", "variantLength", "positionVCF", 
                   "referenceAlleleVCF", "alternateAlleleVCF", "INFO", "FILTER", "AF_joint", 
                   "AF_genomes", "AF_exomes"]]

    for key, val in dic.items():
        writerlist.append(val)  # Only add the value components, exclude the key

    return writerlist

def merge(gnomad_dir, unique_file, output_file):
    dic = dict()

    # Load unique file into a dictionary using column names
    with open(unique_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            key = (row['Chr'], row['positionVCF'], row['referenceAlleleVCF'], row['alternateAlleleVCF'])
            dic[key] = [
                row['VariationID'], row['VariationName'], row['VariationType'], row['Assembly'], row['Chr'],
                row['display_start'], row['display_stop'], row['start'], row['stop'], row['variantLength'],
                row['positionVCF'], row['referenceAlleleVCF'], row['alternateAlleleVCF'], row['INFO']
            ]

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
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                key = (row['#CHROM'].lstrip('chr'), row['POS'], row['REF'], row['ALT'])

                if key in dic:
                    dic[key].extend([row['FILTER'], row['AF_joint'], row['AF_genomes'], row['AF_exomes']])
                    print("Match found and extended:", key)
    return dic

# Example usage
gnomad_dir = '/cta/users/qaljabiri/pure/data/gnomad_data'  # Path to the directory containing gnomAD CSV files
unique_file = '/cta/users/qaljabiri/pure/data/output_variations3.csv'  # Replace with your unique CSV file path
output_file = '/cta/users/qaljabiri/pure/data/xml_gnomad3.csv'  # Replace with your desired output CSV file path

merge(gnomad_dir, unique_file, output_file)

print("Merging complete. Output saved to:", output_file)

