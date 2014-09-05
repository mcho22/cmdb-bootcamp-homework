#!/usr/bin/env python

import sys
import pandas
import operator

from fasta import FASTAReader

reader = FASTAReader ( sys.stdin )

for sid, sequence in reader:
    
    CpG_total = 0
    seq_list = []
    i = 0
    
    for c in sequence:
        seq_list.append(c)
    
    for char in sequence:
        if char == "C":
            if seq_list[i+1] == "G":
                CpG_total += 1
        i += 1
        if i == len(sequence)-1:
            break
   
    CpG_ratio = float(CpG_total) / len(seq_list)
    
    print sid.split()[0] + " " + sid.split()[1] + " " + str(CpG_ratio)
    
