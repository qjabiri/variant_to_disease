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

        # Open the master file and the output file
        output_file = f'{individual_name}_disease_mutations.csv'
        with open(master_file, 'r') as master_csv, open(output_file, 'w', newline='') as out_csv:
            master_reader = csv.DictReader(master_csv)
            fieldnames = master_reader.fieldnames
            writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
            writer.writeheader()

            # Compare each row in the master file to the individual's set
            match_count = 0
            for row in master_reader:
                key = (row['Chromosome'], row['ReferenceAlleleVCF'], row['AlternateAlleleVCF'], row['PositionVCF'])
                if key in individual_set:
                    writer.writerow(row)
                    match_count += 1

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

