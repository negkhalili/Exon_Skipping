#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:22:06 2022

@author: negar
"""


#this program is going through our text
#Open the input file
with open("/Users/negar/Desktop/233_bam_files_results/extable_full.txt", "r") as f:

  # Read the lines of the file into a list and remove leading and trailing white space from each line
  lines = [line.strip() for line in f.readlines()]

# Sort the lines of the input file based on the values in columns 2-9
lines = sorted(lines, key=lambda x: x.split(" ")[1:9])
# Initialize a dictionary to store the groups and their corresponding rows
groups = {}

# Iterate over the lines of the input file
for line in lines:
  # Split the line into a list of columns using a single space as the delimiter
  # and remove extra white space from each value
  columns = [col.strip() for col in line.split(" ")]
  
  # Check if the line should be skipped
  if all(col == "str" for col in columns):
    continue
  
  # Check if the line contains non-numeric values in columns 4-9
  if any(not col.isdigit() for col in columns[3:9]):
    continue
  
  # Convert the values in columns 2-9 to a tuple
  group = tuple(columns[1:9])
  
  # Store the row in the groups dictionary
  if group in groups:
    groups[group].append(line)
  else:
    groups[group] = [line]

# Initialize lists to store the unique and overlap rows
unique_rows = []
overlap_rows = []

# Iterate over the groups and their rows
for group, rows in groups.items():
  # Check if the group is unique or overlaps with other groups
  if len(rows) == 1:
    unique_rows.extend(rows)
  else:
    overlap_rows.extend(rows)

# Open the unique.txt file for writing
with open("/Users/negar/Desktop/unique.txt", "w") as f:
  # Write the rows from the unique_rows list to the file
  for row in unique_rows:
    f.write(f"{row}\n")

# Open the overlap.txt file for writing
with open("/Users/negar/Desktop/overlap.txt", "w") as f:
  # Write the rows from the overlap_rows list to the file
  for row in overlap_rows:
    f.write(f"{row}\n")
