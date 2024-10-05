import os
import csv
def merge(gnomad, unique, output):
    header = [
    "VariationID","VariationName","VariationType","Assembly","Chr","display_start",
    "display_stop","start","stop","variantLength","positionVCF",
    "referenceAlleleVCF","alternateAlleleVCF","condition","AF_joint", "AF_genomes", "AF_exomes"
]
   
   
    with open(output, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
    
        with open(unique, 'r') as file:
            for line in file:
                if ('GRCh38') in line:
                    lines = line.split(',')
                    chr = str(lines[5])
                    gnomad_file = os.path.join(gnomad, f'gnomad_chr{chr}_p.csv')
                    if os.path.isfile(gnomad_file):
                        with open(gnomad_file, 'r') as fileg:
                            for lineg in fileg:
                                linegs = lineg.split()
                                t = 0
                                if lines[4] == linegs[0] and lines[-2] == linegs[4] and lines[-3] == linegs[3] and lines[-4] == linegs[1]:
                                    lines.append(','+linegs[6])
                                    lines.append(','+linegs[8])
                                    lines.append(','+linegs[9])
                                    lines.append(','+linegs[10])
                                    t = 1
                                    break
                            break
                        print(lines)
                        writer.writerow(lines)
                    
                    


gnomad_dir = '/cta/users/qaljabiri/pure/data/gnomad_data'  # Path to the directory containing gnomAD CSV files
unique_file = '/cta/users/qaljabiri/pure/data/output_variations.csv'  # Replace with your unique CSV file path
output_file = '/cta/users/qaljabiri/pure/data/xml_gnomad.csv'  # Replace with your desired output CSV file path
merge(gnomad_dir, unique_file, output_file)
