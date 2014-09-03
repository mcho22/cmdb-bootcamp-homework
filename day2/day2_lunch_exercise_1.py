#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
num_lines = 0

for lines in f:
    num_lines = num_lines + 1
    
print num_lines