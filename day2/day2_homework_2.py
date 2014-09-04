#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as mpl

csv_inputs = "/Users/cmdb/data/day2/metadata.csv"

inp = pd.read_table(csv_inputs)

Sxl_inp = inp[inp["gene_short_name"]=="Sxl"]

print Sxl_inp