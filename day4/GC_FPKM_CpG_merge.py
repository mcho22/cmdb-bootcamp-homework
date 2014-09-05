#!/usr/bin/env python

import sys
import pandas as pd
import operator

GC_inputs = "/Users/cmdb/data/day4/893_GC.csv"
FPKM_inputs = "/Users/cmdb/data/day1/tophat_results/transcripts.gtf"
CpG_inputs = "/Users/cmdb/data/day4/893_CpG.csv"

GC_ratio = open (GC_inputs)
fpkm = open (FPKM_inputs)
CpG_ratio = open (CpG_inputs)

new_fpkm_list = []

for lines in fpkm:
    if lines.split()[2] == "transcript":
        new_fpkm_list.append(lines)

new_ratio_list = []

for ln in GC_ratio:
    new_ratio_list.append(ln)

new_CpG_list = []
    
for lns in CpG_ratio:
    new_CpG_list.append(lns)

i = 0

print ",FPKM,GC_ratio,CpG_ratio"

for lines in new_fpkm_list:
    
    gno = lines.split()[11]
    tr_gno = gno[1:-2] + ","
    
    j = 0
    for l in new_ratio_list:
        if l.split()[1] == tr_gno:
            fpkm = lines.split()[13]
            CpG_1 = new_CpG_list[j]
            CpG_2 = CpG_1.split()[2]
            print tr_gno[:-1] + ", " + str(fpkm[1:-2]) + ", " + str(l.split()[2]) + ", " + str(CpG_2)
        j += 1
    
    i += 1
