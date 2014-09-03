#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
num_2L = 0
num_2R = 0
num_3L = 0
num_3R = 0
num_4 = 0
num_X = 0

for lines in f:
    fields = lines.rstrip("\r\n").split("\t")
    if fields[2] == "2L" or fields[2] == "2LHet":
        num_2L += 1
    elif fields[2] == "2R" or fields[2] == "2RHet":
        num_2R += 1
    elif fields[2] == "3L" or fields[2] == "#LHet":
        num_3L += 1
    elif fields[2] == "3R" or fields[2] == "3RHet":
        num_3R += 1
    elif fields[2] == "4":
        num_4 += 1
    elif fields[2] == "X" or fields[2] == "XHet":
        num_X += 1
    
print "2L: " + str(num_2L)
print "2R: " + str(num_2R)
print "3L: " + str(num_3L)
print "3R: " + str(num_3R)
print "4: " + str(num_4)
print "X: " + str(num_X)