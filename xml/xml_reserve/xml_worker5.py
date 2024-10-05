import gzip
import csv

gz_file_path = '/cta/users/qaljabiri/pure/data/ClinVarVCVRelease_00-latest.xml.gz'
rows = []
trow = []
info = ""
keep = True  # Set to True for testing; change back to False if needed

with gzip.open(gz_file_path, 'rt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()

        if "<VariationArchive RecordType" in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'VariationID' in sline[i]:
                    trow.append(sline[i+1])
                if 'VariationName' in sline[i]:
                    trow.append(sline[i+1])
                if 'VariationType' in sline[i]:
                    trow.append(sline[i+1])
                if 'Accession:' in sline[i]:
                    trow.append(sline[i+1])

        if '<SequenceLocation Assembly=' in line and 'forDisplay="true"' in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'Assembly' in sline[i] and sline[i+1] == 'GRCh38':
                    trow.append(sline[i+1])
                elif 'Chr' in sline[i]:
                    trow.append(sline[i+1])
                elif 'display_start=' in sline[i]:
                    trow.append(sline[i+1])
                elif 'display_stop' in sline[i]:
                    trow.append(sline[i+1])
                elif 'start' in sline[i]:
                    trow.append(sline[i+1])
                elif 'stop' in sline[i]:
                    trow.append(sline[i+1])
                elif 'variantLength' in sline[i]:
                    trow.append(sline[i+1])
                elif 'positionVCF' in sline[i]:
                    trow.append(sline[i+1])
                elif 'referenceAlleleVCF' in sline[i]:
                    trow.append(sline[i+1])
                elif 'alternateAlleleVCF' in sline[i]:
                    trow.append(sline[i+1])

        if '<Description>' in line:
            sline = line.split('>')
            delm = '<'
            index = sline[1].find(delm)
            result = sline[1][:index]
            result = result.replace(",", "")
            info += f"Description={result};"

        if '<MedGen' in line:
            sline = line.split('"')
            medgen_id = sline[1] + ' ' + sline[3]
            medgen_id = medgen_id.replace(",", "")
            info += f"MedGen={medgen_id};"

        if line == '</VariationArchive>':
            if len(trow) > 0:  # Only add trow if it has content
                trow.append(info.replace(",", ""))  # Append the INFO string to the trow list
                rows.append(trow)
            trow = []
            info = ""  # Reset the INFO string for the next VariationArchive block

# Writing to CSV with specified headers
csv_output_path = '/cta/users/qaljabiri/pure/data/output_variations3.csv'
headers = [
    "VariationID", "VariationName", "VariationType",
    "Assembly", "Chr", "display_start", "display_stop", "start", "stop",
    "variantLength", "positionVCF", "referenceAlleleVCF", "alternateAlleleVCF",
    "INFO"
]

with open(csv_output_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(headers)
    for row in rows:
        csv_writer.writerow(row)

print(f"Data has been written to {csv_output_path}")

