import gzip
import csv

gz_file_path = '/cta/users/qaljabiri/pure/data/ClinVarVCVRelease_00-latest.xml.gz'
rows = []
trow = []
keep = True  # Set to True for testing; change back to False if needed

with gzip.open(gz_file_path, 'rt', encoding='utf-8') as file:
    for line in file:
        # Strip leading/trailing whitespace and print the line for debugging
        line = line.strip()
        #print(f"Processing line: {line}")  # Debug: print each line being processed

        if "<VariationArchive RecordType" in line:
            print("Found VariationArchive")  # Debug: indicate when a VariationArchive is found
            sline = line.split('"')
            for i in range(len(sline)):
                if 'VariationID' in sline[i]:
                    trow.append("VariationID:" + str(sline[i+1]))
                if 'VariationName' in sline[i]:
                    trow.append("VariationName:" + str(sline[i+1]))
                if 'VariationType' in sline[i]:
                    trow.append("VariationType:" + str(sline[i+1]))
                if 'Accession:' in sline[i]:
                    trow.append("Accession:" + str(sline[i+1]))

        if '<SequenceLocation Assembly=' in line and 'forDisplay="true"' in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'Assembly' in sline[i]:
                    trow.append("Assembly:" + str(sline[i+1]))
                elif 'Chr' in sline[i]:
                    trow.append("Chr:" + sline[i+1])
                elif 'display_start=' in sline[i]:
                    trow.append("display_stop:" + str(sline[i+1]))
                elif 'display_stop' in sline[i]:
                    trow.append("display_stop:" + str(sline[i+1]))
                elif 'start' in sline[i]:
                    trow.append("start:" + str(sline[i+1]))
                elif 'stop' in sline[i]:
                    trow.append("stop:" + str(sline[i+1]))
                elif 'variantLength' in sline[i]:
                    trow.append("variantLength:" + str(sline[i+1]))
                elif 'positionVCF' in sline[i]:
                    trow.append("positionVCF:" + str(sline[i+1]))
                elif 'referenceAlleleVCF' in sline[i]:
                    trow.append("referenceAlleleVCF:" + str(sline[i+1]))
                elif 'alternateAlleleVCF' in sline[i]:
                    trow.append("alternateAlleleVCF:" + str(sline[i+1]))

        if '<Description>' in line:
            sline = line.split('>')
            delm = '<'
            index = sline[1].find(delm)
            result = sline[1][:index]
            trow.append("germline_condition:" + result)

        if '<MedGen' in line:
            sline = line.split('"')
            if sline[3] not in trow:
                trow.append("condition:" + sline[3])

        if line == '</VariationArchive>':
            print("End of VariationArchive, appending row")  # Debug: indicate when a row is appended
            rows.append(trow)
            print(trow)  # Debug: print the row being appended
            trow = []
    
    print("Final rows:", rows)  # Debug: print all rows after processing

