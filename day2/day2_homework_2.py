#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as mpl

csv_inputs = "/Users/cmdb/data/day2/metadata.csv"

inp = pd.read_table(csv_inputs)

Sxl_inp = inp[inp["gene_short_name"]=="Sxl"]

Sxl_value_list = []

for row in Sxl_inp.iterrows():
    index, data = row
    Sxl_value_list.append(data.tolist())

Sxl_value_extracted = Sxl_value_list[0]
Sxl_value_trimmed = Sxl_value_extracted[9:]

print Sxl_value_trimmed