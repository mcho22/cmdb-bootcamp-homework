#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
types = []
global_before_str = "Initial"

for lines in f:
    fields = lines.rstrip("\r\n").split("\t")
    align_loc = str(fields[2])
    if align_loc != global_before_str:
        types.append(fields[2])
    global_before_str = align_loc
    
print sorted(types)