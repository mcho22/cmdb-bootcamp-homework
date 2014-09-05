#!/usr/bin/env python

import sys
import pandas as pd
import operator

GC_inputs = "/Users/cmdb/data/day4/893_GC.csv"
FPKM_inputs = "/Users/cmdb/data/day1/tophat_results/transcripts.gtf"

GC_ratio = open (GC_inputs)
fpkm = open (FPKM_inputs)

new_fpkm_list = []

for lines in fpkm:
    if lines.split()[2] == "transcript":
        new_fpkm_list.append(lines)

new_ratio_list = []

for ln in GC_ratio:
    new_ratio_list.append(ln)

temp_gene_list = []
fpkm_paired_list = []
ratio_paired_list = []

i = 0

print ",FPKM,GC_ratio"

for lines in new_fpkm_list:
    
    gno = lines.split()[11]
    tr_gno = gno[1:-2] + ","
    
    for l in new_ratio_list:
        if l.split()[1] == tr_gno:
            fpkm = lines.split()[13]
            print tr_gno[:-1] + ", " + str(fpkm[1:-2]) + ", " + str(l.split()[2])
    
    i += 1
