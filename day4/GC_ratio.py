#!/usr/bin/env python

import sys
import pandas
import operator

from fasta import FASTAReader

reader = FASTAReader ( sys.stdin )

for sid, sequence in reader:
    
    gc_total = 0
    
    for char in sequence:
        if char == "G":
            gc_total += 1
        elif char == "C":
            gc_total += 1
        
    gc_ratio = float(gc_total) / float(len(sequence))
    
    print sid.split()[0] + " " + sid.split()[1] + ", " + str(gc_ratio)
    
