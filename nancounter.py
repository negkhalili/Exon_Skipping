#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:05:40 2022

@author: negar
"""


# I want to count the nan
# Open the file
with open("/Users/negar/Desktop/233_bam_files_results/extable_full.txt", "r") as f:
  # Initialize a counter to store the number of "nan" strings
  nan_count = 0

  # Read the file line by line
  for line in f:
    # Split the line into a list of columns
    columns = line.strip().split(" ")
    
    # Check if the value in column 13 is "nan"
    if columns[12] == "nan":
      # If it is, increment the counter
      nan_count += 1

# Print the number of "nan" strings
print(f"Number of 'nan' strings: {nan_count}")
