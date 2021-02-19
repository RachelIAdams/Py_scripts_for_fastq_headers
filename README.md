# Py_scripts_for_fastq_headers
Various python scripts for editing sequence identifiers in fastq files

**rewrite_header_fastq.py**
This script rewrites sequence identifier and replaces the facility-given name with your name based on another dataframe. For example, the facility named each sequence with the barcode, and you want to replace with barcode with a sample name, where the link between the barcode and sample name is detailed in a separate file. It performs something like "Vlookup" in Excel. There are 3 inputs: 1) fastq file of original names; 2) name of the new file want to write to; 3) barcode map. 

**rewrite_header_bysample.py**
Rewrites sequence identifiers for individual fastq files in a directory. The 1 input is the directory containing the list of fastq files to edit identifiers. 

**rewrite_header_fastq_for_usearch_nomapneeded.py**
Rewrites sequence identifier through simplifying the facility-given sequence identify. It simplifies the existing identifier; it does not replace one aspect of the identifier with another name, as done with the rewrite_header_fastq.py. 

**check_unique_sampleIDs.py**
Generates list of unique sample IDs in sequence identifiers
