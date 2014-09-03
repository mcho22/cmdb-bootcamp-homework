#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
Pos_str = 0
Neg_str = 0

for lines in f:
    if "XS:A:+" in lines:
        Pos_str += 1
    elif "XS:A:-" in lines:
        Neg_str += 1
    
print "Number of reads which aligns to positive strand = " + str(Pos_str)
print "Number of reads which aligns to negative strand = " + str(Neg_str)