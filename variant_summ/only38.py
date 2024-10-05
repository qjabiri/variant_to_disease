import csv

def filter_grch38(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader)  # Read the header
        writer.writerow(header)  # Write the header to the output file
        
        # Filter rows that contain "GRCh38" in the Assembly column
        for row in reader:
            if 'GRCh38' in row:
                writer.writerow(row)

# Example usage
input_file = '/cta/users/qaljabiri/pure/data/combined.csv'  # Replace with your input file path
output_file = '/cta/users/qaljabiri/pure/data/filtered_grch38.csv'  # Replace with your output file path

filter_grch38(input_file, output_file)

