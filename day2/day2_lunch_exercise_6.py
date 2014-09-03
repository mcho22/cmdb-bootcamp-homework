#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )

total = 0

for i, line in enumerate (f):
    
    fields = line.rstrip("\r\n").split("\t")
    total = total + float(fields[4])

print total / i