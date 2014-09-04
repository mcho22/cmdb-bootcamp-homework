#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as mpl

# File location input & opening

cufflinks_outputs_1 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_outputs_2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

cf_1 = pd.read_table(cufflinks_outputs_1)
cf_2 = pd.read_table(cufflinks_outputs_2)

# Variable defining

cf_1_1st = cf_1.sort("FPKM", ascending = False)[:5201]["FPKM"]
cf_1_2nd = cf_1.sort("FPKM", ascending = False)[5201:10401]["FPKM"]
cf_1_3rd = cf_1.sort("FPKM", ascending = False)[10401:]["FPKM"]

cf_2_1st = cf_2.sort("FPKM", ascending = False)[:5201]["FPKM"]
cf_2_2nd = cf_2.sort("FPKM", ascending = False)[5201:10401]["FPKM"]
cf_2_3rd = cf_2.sort("FPKM", ascending = False)[10401:]["FPKM"]

cf_sorted = [cf_1_1st, cf_1_2nd, cf_1_3rd, cf_2_1st, cf_2_2nd, cf_2_3rd]

print cf_sorted

# Plotting

mpl.figure()
mpl.boxplot(cf_sorted)
mpl.yscale("log")
mpl.axis([0, 7, 0.001, 100000])
mpl.savefig("Box_plot_893915_3.png")
