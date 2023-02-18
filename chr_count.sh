#!/bin/bash

# Create a list of the chr values to search for
chr_values="chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr16 chr17 chr18 chr19 chr20 chr21 chr22 chrX chrY"

# Use awk to select the column that contains the chr values
# Pipe the output to sort and uniq to count the number of occurrences of each unique value
# Pipe the output to sort again, this time with the -n option to sort by the number of occurrences
# Redirect the output to a file called chr_count.txt
awk '{print $2}' extable_full.txt | sort | uniq -c | sort -n > chr_count.txt

