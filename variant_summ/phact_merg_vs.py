import csv

# File paths
first_csv_path = '/cta/users/qaljabiri/pure/data/filtered_grch38.csv'
second_csv_path = '/cta/users/nncurabaz/phactboost_final/phactboost_scores_complete.csv'
output_csv_path = '/cta/users/qaljabiri/pure/data/final_tsv_output_with_phactboost.csv'

# Load second CSV file into a dictionary
def load_second_csv(second_csv_path):
    second_data = {}
    with open(second_csv_path, mode='r', newline='', encoding='utf-8') as second_file:
        second_reader = csv.DictReader(second_file, delimiter=',')
        for row in second_reader:
            key = (row['chrm'], row['coordinate'], row['ref_nuc'], row['alt_nuc'])
            second_data[key] = row['phactboost_scores']
    return second_data

# Write the merged CSV file
def merge_csv(first_csv_path, second_data, output_csv_path):
    with open(first_csv_path, mode='r', newline='', encoding='utf-8') as first_file:
        first_reader = csv.DictReader(first_file, delimiter=',')
        # Ensure fieldnames from the original file are included
        fieldnames = first_reader.fieldnames + ['phactboost_scores']

        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as output_file:
            output_writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=',')
            output_writer.writeheader()

            for row in first_reader:
                # Debugging: Print the row before modification
                print("Original row:", row)
                
                key = (row['Chromosome'], row['PositionVCF'], row['ReferenceAllele'], row['AlternateAllele'])
                phactboost_scores = second_data.get(key, 'none')
                row['phactboost_scores'] = phactboost_scores

                # Debugging: Print the row after modification
                print("Modified row:", row)

                try:
                    output_writer.writerow(row)
                except ValueError as e:
                    print("Error writing row:", e)
                    print("Row data:", row)

# Execute the functions
second_data = load_second_csv(second_csv_path)
merge_csv(first_csv_path, second_data, output_csv_path)

print("Merging complete. Output saved to:", output_csv_path)

