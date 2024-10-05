#disease_list = /cta/users/qaljabiri/pure/data/gene_condition_source_id

import csv
import sys
import os

def find_disease_causing_mutations(individual_name, individual_file, master_file):
    try:
        # Check if the input files exist
        if not os.path.exists(individual_file):
            raise FileNotFoundError(f"Error: Individual file '{individual_file}' not found.")
        if not os.path.exists(master_file):
            raise FileNotFoundError(f"Error: Master file '{master_file}' not found.")

        # Read individual file into a set for quick lookup
        individual_set = set()
        with open(individual_file, 'r') as ind_csv:
            ind_reader = csv.DictReader(ind_csv)
            for row in ind_reader:
                key = (row['#CHROM'].lstrip('chr'), row['REF'], row['ALT'], row['POS'])
                individual_set.add(key)

        # List to hold matching rows for sorting
        matching_rows = []

        # Open the master file and read
        output_file = f'{individual_name}_disease_mutations.csv'
        with open(master_file, 'r') as master_csv:
            master_reader = csv.DictReader(master_csv)
            fieldnames = master_reader.fieldnames

            # Compare each row in the master file to the individual's set
            match_count = 0
            for row in master_reader:
                key = (row['Chromosome'], row['ReferenceAlleleVCF'], row['AlternateAlleleVCF'], row['PositionVCF'])
                
                # Check if the key exists in the individual's set
                if key in individual_set:
                    # Check if the row contains 'Benign'
                    if 'Benign' not in row['ClinicalSignificance']:
                        matching_rows.append(row)
                        match_count += 1

        # Sort matching rows by phactboost_scores in descending order
        matching_rows.sort(key=lambda x: float(x['phactboost_scores']) if x['phactboost_scores'].replace('.', '', 1).isdigit() else float('-inf'), reverse=True)

        # Write the sorted output to CSV
        with open(output_file, 'w', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
            writer.writeheader()
            for row in matching_rows:
                writer.writerow(row)

        if match_count > 0:
            print(f"File '{output_file}' has been written successfully with {match_count} matching entries.")
        else:
            print(f"No matching entries found. The file '{output_file}' has been created but is empty.")

    except FileNotFoundError as e:
        print(e)
    except KeyError as e:
        print(f"Error: Missing expected column in the input files: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <individual_name> <individual_file.csv> <master_file.csv>")
    else:
        individual_name = sys.argv[1]
        individual_file = sys.argv[2]
        master_file = sys.argv[3]
        find_disease_causing_mutations(individual_name, individual_file, master_file)