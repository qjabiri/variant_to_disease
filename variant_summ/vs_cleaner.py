import csv
import gzip

def convert_gzipped_txt_to_csv(input_gz, output_csv, columns_to_keep):
    # Open the gzipped file
    with gzip.open(input_gz, 'rt') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter='\t')  # Assuming the input file is tab-delimited
        writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)

        # Write the header to the CSV file
        writer.writeheader()

        for row in reader:
            # Create a new row dictionary with only the selected columns
            filtered_row = {col: row[col] for col in columns_to_keep if col in row}
            writer.writerow(filtered_row)

    print(f"Selected columns have been written to {output_csv}")

# Example usage
input_gz = '/cta/users/qaljabiri/pure/data/variant_summary.txt.gz'  # Path to your gzipped input text file
output_csv = '/cta/users/qaljabiri/pure/data/clean_tsv.csv'  # Replace with your desired output CSV file path

# List of columns you want to keep
columns_to_keep = [
    '#AlleleID', 'Type', 'Name', 'GeneID', 'GeneSymbol', 'HGNC_ID', 
    'ClinicalSignificance', 'ClinSigSimple', 'RS# (dbSNP)', 'nsv/esv (dbVar)', 
    'RCVaccession', 'PhenotypeIDS', 'PhenotypeList', 'Assembly', 'Chromosome', 
    'Start', 'Stop', 'ReferenceAllele', 'AlternateAllele', 'PositionVCF', 'ReferenceAlleleVCF', 'AlternateAlleleVCF'
]

convert_gzipped_txt_to_csv(input_gz, output_csv, columns_to_keep)

