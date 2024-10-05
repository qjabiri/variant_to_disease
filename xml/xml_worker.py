import gzip
import csv

gz_file_path = '/cta/users/qaljabiri/pure/data/ClinVarVCVRelease_00-latest.xml.gz'
rows = []
trow = ["NA"] * 16
info = ""
keep = True  # Set to True for testing; change back to False if needed

with gzip.open(gz_file_path, 'rt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        # if "<VariationArchive RecordType" in line:

        if "<VariationArchive " in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'VariationID' in sline[i]:
                    trow[0] = (sline[i+1])
                if 'VariationName' in sline[i]:
                    trow[1] = (sline[i+1])
                if 'VariationType' in sline[i]:
                    trow[2] = (sline[i+1])
                if 'NumberOfSubmissions' in sline[i]:
                    trow[3] = (sline[i+1])
                if 'Accession' in sline[i]:
                    trow[4] = (sline[i+1])

        if '<Gene Symbol=' in line:
            sline = line.split('"')
            if trow[5] == 'NA':
                trow[5] = (sline[1])
            else:
                trow[5] = trow[5] + ' ' + (sline[1])

        if '<SequenceLocation Assembly=' in line and 'forDisplay="true"' in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'Assembly' in sline[i] and sline[i+1] == 'GRCh38':
                    trow[6] = (sline[i+1])
                elif 'Chr' in sline[i]:
                    trow[7] = (sline[i+1])
                elif 'display_start=' in sline[i]:
                    trow[8] = (sline[i+1])
                elif 'display_stop' in sline[i]:
                    trow[9] = (sline[i+1])
                elif 'start' in sline[i]:
                    trow[10] = (sline[i+1])
                elif 'stop' in sline[i]:
                    trow[11] = (sline[i+1])
                elif 'variantLength' in sline[i]:
                    trow[12] = (sline[i+1])
                elif 'positionVCF' in sline[i]:
                    trow[13] = (sline[i+1])
                elif 'referenceAlleleVCF' in sline[i]:
                    trow[14] = (sline[i+1])
                elif 'alternateAlleleVCF' in sline[i]:
                    trow[15] = (sline[i+1])

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
        if 'DB="Orphanet"' in line:
            sline = line.split('"')
            orph_id = sline[1]
            info += f"Orphanet={orph_id};"
        if 'DB="OMIM"' in line:
            sline = line.split('"')
            orph_id = sline[3]
            info += f"OMIM={orph_id};"
        if line == '</VariationArchive>':
            if len(trow) > 0:  # Only add trow if it has content
                trow.append(info.replace(",", ""))  # Append the INFO string to the trow list
                rows.append(trow)
            info = ""  # Reset the INFO string for the next VariationArchive block
            trow = ["NA"] * 16

# Writing to CSV with specified headers
csv_output_path = '/cta/users/qaljabiri/pure/data/output_variations4.csv'
headers = [
    "VariationID", "VariationName", "VariationType", "NumberOfSubmissions", "Accession", "Gene",
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
