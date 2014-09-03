#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
num_lines = 0

for lines in f:
    fields = lines.rstrip("\r\n").split("\t")
    if fields[2] == "2L":
        if int(fields[3]) >= 10000 and int (fields[3]) <= 20000:
            num_lines = num_lines + 1
    
print num_lines