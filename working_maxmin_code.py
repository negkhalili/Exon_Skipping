#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:42:00 2022

@author: negar
"""
# Open the overlap.txt file
with open("/Users/negar/Desktop/overlap.txt", "r") as f:
  # Read the lines of the file into a list
  lines = f.readlines()

# Initialize a dictionary to store the rows with each combination of values in columns 2-9
rows = {}

# Iterate over the lines of the overlap.txt file
for line in lines:
  # Split the line into a list of columns
  columns = line.strip().split(" ")
  
  # Create a tuple of the values in columns 2-9
  values = tuple(columns[1:9])
  
  # If this combination of values has not been seen before, initialize an empty list for it
  if values not in rows:
    rows[values] = []
  
  # Add the line to the list for this combination of values
  rows[values].append(line)

# Iterate over the combinations of values in the rows dictionary
for values, value_rows in rows.items():
  # Initialize an empty list to store the rows with the max and min values in column 13
  maxmin_rows = []

  # Iterate over the rows with this combination of values in columns 2-9
  for line in value_rows:
    # Split the line into a list of columns
    columns = line.strip().split(" ")
    
    # Try to convert the value in column 13 to a float
    try:
      col13_value = float(columns[12])
    except ValueError:
      # If the conversion fails (e.g. because the value is "nan"), set col13_value to None
      col13_value = None
    
    # If the max and min values have not yet been set, initialize them to the value in column 13
    if not maxmin_rows:
      maxmin_rows = [line, line]
    # Otherwise, update the max and min values if necessary
    else:
      # Skip this row if the value in column 13 is None
      if col13_value is None:
        continue
      if col13_value > float(maxmin_rows[0].split(" ")[12]):
        maxmin_rows[0] = line
      elif col13_value < float(maxmin_rows[1].split(" ")[12]):
        maxmin_rows[1] = line

  # Calculate the difference between the max and min values in column 13
  max_value = None
  min_value = None
  if maxmin_rows[0].split(" ")[12] != "nan":
    max_value = float(maxmin_rows[0].split(" ")[12])
  if maxmin_rows[1].split(" ")[12] != "nan":
    min_value = float(maxmin_rows[1].split(" ")[12])
    difference=max_value - min_value
  # If the difference is equal to or greater than 0.3, write the max and min rows to the maxmin3.txt file
  if difference >= 0.4:
    with open("/Users/negar/Desktop/maxmin_nan_4.txt", "a") as f:
      for line in maxmin_rows:
        f.write(line)
