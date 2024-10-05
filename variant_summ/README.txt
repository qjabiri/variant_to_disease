Project: Variant Data Processing Scripts
This project consists of Python scripts for processing and analyzing genomic variant data. The scripts are designed to handle tasks such as combining data from different sources, filtering based on specific criteria, and cleaning data for further analysis.
Table of Contents
1. Overview
2. Scripts
   * combine_vs.py
   * only38.py
   * phact_merg_vs.py
   * vs_cleaner.py
3. Requirements
4. Usage
5. License
Overview
The scripts in this project are designed to streamline the processing of genomic variant data, focusing on merging, filtering, and cleaning data for downstream analysis. They are particularly useful for integrating data from various sources and ensuring consistency in data format and content.
Scripts
combine_vs.py
* Purpose: This script is used to combine variant data from multiple sources into a single, unified dataset. It is designed to handle gnomad and the processed variant summary from clinvar CSV’s, aligning data based on specific genomic identifiers(chr, pos, ref, alt).
* Key Features:
   * Combines variant data from various files.
   * Aligns and merges data based on common identifiers such as chromosome, position, reference, and alternate alleles.
   * Ensures consistency across the merged dataset.


only38.py
* Purpose: This script filters variant data to include only entries that match the GRCh38 assembly version. It is useful for ensuring that data is consistent with a specific genomic assembly standard.
* Key Features:
   * Filters input data to retain only GRCh38 entries.
   * Removes or flags entries that do not match the desired assembly version.
   * Outputs a clean dataset that conforms to the GRCh38 standard.


phact_merg_vs.py
* Purpose: This script focuses on merging variant data with PhactBoost scores. It enhances the variant data by adding scoring information that can be used to prioritize and assess variants.
* Key Features:
   * Reads and merges PhactBoost score data with variant information.
   * Outputs an augmented dataset with additional scoring metrics.


vs_cleaner.py
* Purpose: This script is designed to clean and preprocess the variant summary data file from clinvar. It removes unnecessary data, corrects formatting issues, and ensures the dataset is ready for analysis.
* Key Features:
   * Cleans variant data files by removing redundant or irrelevant information.
   * Standardizes data formats for consistency.
   * Prepares data for further analysis or integration with other datasets.


Requirements
* Python 3.x
* Required Python libraries (install using pip):
   * os
   * gzip
   * csv 


Usage
1. Combine Variant Data:
Run combine_vs.py to merge variant data from different sources into a single file:
bash
Copy code
python combine_vs.py
   * 2. Filter for GRCh38 Assembly:
Run only38.py to filter your data for the GRCh38 assembly version:
bash
Copy code
python only38.py
   * 3. Merge PhactBoost Scores:
Run phact_merg_vs.py to add PhactBoost scores to your variant data:
bash
Copy code
python phact_merg_vs.py
   * 4. Clean Variant Data:
   * Run vs_cleaner.py to clean and preprocess your variant data files:
bash
Copy code
python vs_cleaner.py