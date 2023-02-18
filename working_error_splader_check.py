#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:32:53 2022

@author: negar
"""

# Open the input file and output file
with open('/Users/negar/Desktop/extable_full.txt', 'r') as input_file, open('/Users/negar/Desktop/output.txt', 'w') as output_file:
    # Read each line of the input file
    for line in input_file:
        # Split the line into columns using the space character as the delimiter
        columns = line.split(' ')

        # Check if the values in columns 10, 11, and 12 are numerical
        if columns[9].isnumeric() and columns[10].isnumeric() and columns[11].isdigit():
            # Calculate x by adding the values in columns 10 and 11 and dividing the result by 2
            x = (float(columns[9]) + float(columns[10])) / 2

            # Calculate the expected value by dividing x by the sum of x and the value in column 12
            expected = x / (x + float(columns[11]))

            # Check if the value in column 12 is zero
            if float(columns[12]) == 0:
                # Set the error rate to zero if the value in column 12 is zero
                error_rate = 0
            else:
                # Calculate the error rate by subtracting the expected value from the value in column 13 and dividing the result by the value in column 13
                error_rate = (float(columns[12]) - expected) / float(columns[12])

            # Write the original values from the input line, as well as the calculated error rate, to the output file
            output_file.write(line.strip() + ' ' + str(error_rate) + '\n')
