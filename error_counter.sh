#!/bin/bash

awk -v counter="$counter" '{gsub("e","*10^",$15); if ($15 > 0.5 || $15 < -0.5) {counter += 1}} END {print "Number of rows with out-of-range values in column 15: " counter}' sorted_output_PSI_error.txt

