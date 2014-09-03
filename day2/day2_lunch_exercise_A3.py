#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
num_lines = 0

for i, line in enumerate (f):
    
    fields = line.rstrip("\r\n").split("\t")
    phred_raw = str(fields[10])
    phred_list = list(phred_raw)
    read_length = len(str(fields[9]))
    phred_trs = 0
    
    for char in phred_list:
        phred_trs = phred_trs + ord(char) - 33
        phred_ave = float(phred_trs) / float(read_length) 
            
    if phred_ave > 30:
        num_lines += 1
                
print "Number of lines with average phred score > 30 = " + str(num_lines)
