Project: XML and CSV Data Processing Scripts
This project contains Python scripts designed to process and merge genomic data from XML and CSV files. The scripts handle specific tasks related to combining and filtering data for research purposes.
Table of Contents
1. Overview
2. Scripts
   * combine_xml.py
   * phact_merg_xml.py
   * xml_worker.py
3. Requirements


Overview
The scripts in this project are designed to facilitate the processing and analysis of genomic data, particularly focusing on merging data from XML and CSV formats. They are tailored for tasks such as filtering, extracting relevant information, and matching data across different files based on specific criteria.
Scripts




xml_worker.py
* Purpose: This script acts as a utility to handle XML data processing tasks. It includes functions and methods used by the other scripts to parse and process XML files. Made specifically of the clinvar VCV XML files, would have issues with other ones.
* Key Features:
   * Provides helper functions for XML parsing.
   * Facilitates data extraction and transformation from XML format.
   * Supports integration with other scripts for streamlined data processing.


combine_xml.py
* Purpose: This script is used to combine data from XML files with existing gnomad CSV data. It handles merging the processed xml file and merging their contents with a provided CSV file (gnomad).
* Key Features:
   * Parses the processed XML file to extract relevant genomic data (a unique key made using chr, pos, ref, and alt).
   * Merges extracted data with a master CSV file.
   * Ensures data consistency and alignment based on genomic identifiers (a unique key made using chr, pos, ref, and alt).
phact_merg_xml.py
* Purpose: This script specifically focuses on merging data related to PhactBoost scores from CSV files with processed XML+gnomad data. It is designed to augment the genomic data with additional scoring metrics.
* Key Features:
   * Reads PhactBoost scores from CSV files.
   * Merges PhactBoost data with XML-derived data.
Requirements
* Python 3.x
* Required Python libraries (install using pip):
   * csv 
   * os 
   * gzip 


Usage
1. Combine XML and CSV Data:
Run combine_xml.py to merge XML data with your master CSV file:
bash
Copy code
python combine_xml.py
   * 2. Merge PhactBoost Scores:
Run phact_merg_xml.py to augment your XML data with PhactBoost scores from a CSV file:
bash
Copy code
python phact_merg_xml.py
   * 3. XML Data Processing:
   * xml_worker.py is primarily used as a utility by other scripts. You can also use it to parse and process XML files independently.