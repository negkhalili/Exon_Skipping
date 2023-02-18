#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 13:24:18 2022

@author: negar
"""


#this program is going through our text
# Open the input file
with open("/Users/negar/Desktop/233_bam_files_results/extable_full.txt", "r") as f:

  # Read the lines of the file into a list and remove leading and trailing white space from each line
  lines = [line.strip() for line in f.readlines()]

# Sort the lines of the input file based on the values in columns 2-9
lines = sorted(lines, key=lambda x: x.split(" ")[1:9])

# Initialize a dictionary to store the groups and their corresponding counts
groups = {}

# Iterate over the lines of the input file
for line in lines:
  # Split the line into a list of columns using a single space as the delimiter
  columns = line.split(" ")
  
  # Check if the line should be skipped
  if all(col == "str" for col in columns):
    continue
  
  # Check if the line contains non-numeric values in columns 4-9
  if any(not col.isdigit() for col in columns[3:9]):
    continue
  
  # Remove extra white space from each value
  columns = [col.strip() for col in columns]
  
  # Convert the values in columns 2-9 to a tuple
  group = tuple(columns[1:9])
  
  # Increment the count for this group
  if group in groups:
    groups[group] += 1
  else:
    groups[group] = 1

# Open the output file for writing
with open("/Users/negar/Desktop/group_count.txt", "w") as f:
  # Write the group counts to the group_count.txt file
  for group, count in groups.items():
    f.write(f"{group}: {count}\n")
