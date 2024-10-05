import gzip
import csv
gz_file_path = '/cta/users/qaljabiri/pure/data/ClinVarVCVRelease_00-latest.xml.gz'
rows = []
trow = []
keep = True  #change back to false if change happens
with gzip.open(gz_file_path, 'rt', encoding='utf-8') as file:
    for line in file:
        #print('yay')
        if "<VariationArchive VariationID=" in line:
            print("yay")
            sline = line.split('"')
            trow.append("VariationID:" + sline[1])
            trow.append("VariationName:" + sline[3])
            trow.append("VariationType:" + sline[5])
            trow.append("Accession:" + sline[7])

        #if "Homo sapiens" in line or "human" in line:
            #keep = True
        #if " <CanonicalSPDI" in line:
            #sline = line.split(">")
            #trow.append("CanonicalSPDI:" + sline[1])
        if '<SequenceLocation Assembly' in line and 'forDisplay="true"' in line:
            sline = line.split('"')
            for i in range(len(sline)):
                if 'Assembly' in sline[i]:
                    trow.append("Assembly:" + str(line[i+1]))
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
        if  '<Description>' in line:
            sline = line.split('>')
            delm = '<'
            index =  sline[1].find(delm)
            result = sline[1][:index]
            trow.append("germline_condition:" + result)
        if '<MedGen' in line:
            sline = line.split('"')
            if sline[3] not in trow:
                trow.append("condition:" + sline[3])
        if line == '</VariationArchive>':
            #if keep == True:
            print(trow)
            rows.append(trow)
            trow = []
            #keep = False
    print(row)

