import gzip
import csv

gz_file_path = '/cta/users/qaljabiri/pure/data/ClinVarVCVRelease_00-latest.xml.gz'
rows = []
trow = []
keep = False
condition_set = set()

# Define the headers
headers = [
    "VariationID", "VariationName", "VariationType", "Accession",
    "Assembly", "Chr", "display_start", "display_stop", "start", "stop",
    "variantLength", "positionVCF", "referenceAlleleVCF", "alternateAlleleVCF",
    "condition"
]

with gzip.open(gz_file_path, 'rt', encoding='utf-8') as file:
    for line in file:
        if "<VariationArchive" in line:
            sline = line.split('"')
            trow.append(sline[1])
            trow.append(sline[3])
            trow.append(sline[5])
            trow.append(sline[7])

        if "Homo sapiens" in line or "human" in line:
            keep = True

        if '<SequenceLocation Assembly' in line and 'forDisplay="true"' in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'Assembly' in sline[i]:
                    trow.append(str(line[i+1]))
                elif 'Chr' in sline[i]:
                    trow.append(sline[i+1])
                elif 'display_start=' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'display_stop' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'start' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'stop' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'variantLength' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'positionVCF' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'referenceAlleleVCF' in sline[i]:
                    trow.append(str(sline[i+1]))
                elif 'alternateAlleleVCF' in sline[i]:
                    trow.append(str(sline[i+1]))

        if '<Description>' in line:
            sline = line.split('>')
            delm = '<'
            index = sline[1].find(delm)
            result = sline[1][:index]
            trow.append(result)

        if '<MedGen' in line:
            sline = line.split('"')
            condition = sline[3]
            if condition not in condition_set:
                condition_set.add(condition)

        if line == '</VariationArchive>':
            if keep:
                # Join all unique conditions into one string, separated by semicolons
                trow.append('; '.join(condition_set))
                rows.append(trow)
            trow = []
            condition_set = set()
            keep = False

# Adding the part that writes rows to a CSV file
csv_output_path = '/cta/users/qaljabiri/pure/data/output_variations.csv'

with open(csv_output_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header
    csv_writer.writerow(headers)
    # Write the rows
    for row in rows:
        csv_writer.writerow(row)

print(f"Data has been written to {csv_output_path}")

