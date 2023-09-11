#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

# Directory containing the single FASTA files
input_directory = r'path_to_directory_with_fasta_files'

# Output multi-FASTA file
output_file = 'combined.fasta'

# Open the output file for writing
with open(output_file, 'w') as combined_fasta:
    # List all files in the directory
    file_list = os.listdir(input_directory)
    
    # Loop through each file
    for file_name in file_list:
        if file_name.endswith('.fasta'):  # Ensure it's a FASTA file
            with open(os.path.join(input_directory, file_name), 'r') as single_fasta:
                # Copy each line (including the header and sequence) to the combined file
                combined_fasta.write(single_fasta.read())

