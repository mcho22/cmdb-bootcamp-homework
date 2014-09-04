#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as mpl
import csv
import sys


cufflinks_outputs_1 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_outputs_2 = "/Users/cmdb/data/results/SRR072894_clout/genes.fpkm_tracking"
cufflinks_outputs_3 = "/Users/cmdb/data/results/SRR072895_clout/genes.fpkm_tracking"
cufflinks_outputs_4 = "/Users/cmdb/data/results/SRR072896_clout/genes.fpkm_tracking"
cufflinks_outputs_5 = "/Users/cmdb/data/results/SRR072897_clout/genes.fpkm_tracking"
cufflinks_outputs_6 = "/Users/cmdb/data/results/SRR072899_clout/genes.fpkm_tracking"
cufflinks_outputs_7 = "/Users/cmdb/data/results/SRR072901_clout/genes.fpkm_tracking"
cufflinks_outputs_8 = "/Users/cmdb/data/results/SRR072903_clout/genes.fpkm_tracking"
cufflinks_outputs_9 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
cufflinks_outputs_10 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
cufflinks_outputs_11 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
cufflinks_outputs_12 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
cufflinks_outputs_13 = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
cufflinks_outputs_14 = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
cufflinks_outputs_15 = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
cufflinks_outputs_16 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

cf_1 = pd.read_table(cufflinks_outputs_1)
cf_2 = pd.read_table(cufflinks_outputs_2)
cf_3 = pd.read_table(cufflinks_outputs_3)
cf_4 = pd.read_table(cufflinks_outputs_4)
cf_5 = pd.read_table(cufflinks_outputs_5)
cf_6 = pd.read_table(cufflinks_outputs_6)
cf_7 = pd.read_table(cufflinks_outputs_7)
cf_8 = pd.read_table(cufflinks_outputs_8)
cf_9 = pd.read_table(cufflinks_outputs_9)
cf_10 = pd.read_table(cufflinks_outputs_10)
cf_11 = pd.read_table(cufflinks_outputs_11)
cf_12 = pd.read_table(cufflinks_outputs_12)
cf_13 = pd.read_table(cufflinks_outputs_13)
cf_14 = pd.read_table(cufflinks_outputs_14)
cf_15 = pd.read_table(cufflinks_outputs_15)
cf_16 = pd.read_table(cufflinks_outputs_16)

cog = ["gene_short_name"]
coi = ["FPKM"]

cf_FPKM_index = cf_1[cog]
cf_FPKM_1 = cf_1[coi].rename(columns={'FPKM': 'FPKM_M10'})
cf_FPKM_2 = cf_2[coi].rename(columns={'FPKM': 'FPKM_M11'})
cf_FPKM_3 = cf_3[coi].rename(columns={'FPKM': 'FPKM_M12'})
cf_FPKM_4 = cf_4[coi].rename(columns={'FPKM': 'FPKM_M13'})
cf_FPKM_5 = cf_5[coi].rename(columns={'FPKM': 'FPKM_M14A'})
cf_FPKM_6 = cf_6[coi].rename(columns={'FPKM': 'FPKM_M14B'})
cf_FPKM_7 = cf_7[coi].rename(columns={'FPKM': 'FPKM_M14C'})
cf_FPKM_8 = cf_8[coi].rename(columns={'FPKM': 'FPKM_M14D'})
cf_FPKM_9 = cf_9[coi].rename(columns={'FPKM': 'FPKM_F10'})
cf_FPKM_10 = cf_10[coi].rename(columns={'FPKM': 'FPKM_F11'})
cf_FPKM_11 = cf_11[coi].rename(columns={'FPKM': 'FPKM_F12'})
cf_FPKM_12 = cf_12[coi].rename(columns={'FPKM': 'FPKM_F13'})
cf_FPKM_13 = cf_13[coi].rename(columns={'FPKM': 'FPKM_F14A'})
cf_FPKM_14 = cf_14[coi].rename(columns={'FPKM': 'FPKM_F14B'})
cf_FPKM_15 = cf_15[coi].rename(columns={'FPKM': 'FPKM_F14C'})
cf_FPKM_16 = cf_16[coi].rename(columns={'FPKM': 'FPKM_F14D'})

print type (cf_FPKM_index)
print type (cf_FPKM_1)

cf_merged = cf_FPKM_index.join(cf_FPKM_1)
cf_merged = cf_merged.join(cf_FPKM_2)
cf_merged = cf_merged.join(cf_FPKM_3)
cf_merged = cf_merged.join(cf_FPKM_4)
cf_merged = cf_merged.join(cf_FPKM_5)
cf_merged = cf_merged.join(cf_FPKM_6)
cf_merged = cf_merged.join(cf_FPKM_7)
cf_merged = cf_merged.join(cf_FPKM_8)
cf_merged = cf_merged.join(cf_FPKM_9)
cf_merged = cf_merged.join(cf_FPKM_10)
cf_merged = cf_merged.join(cf_FPKM_11)
cf_merged = cf_merged.join(cf_FPKM_12)
cf_merged = cf_merged.join(cf_FPKM_13)
cf_merged = cf_merged.join(cf_FPKM_14)
cf_merged = cf_merged.join(cf_FPKM_15)
cf_merged = cf_merged.join(cf_FPKM_16)

print type (cf_merged)
print cf_merged.head()

cf_merged.to_csv("metadata.csv", sep="\t", index=False)
#cf_merged.to_html("metadata.html")