#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as mpl
import statsmodels.api as sm
from pylab import *

cf = pd.read_csv("/Users/cmdb/data/day4/FPKM_GC_CpG_list.csv")

model = sm.formula.ols( formula = "FPKM ~ GC_ratio + CpG_ratio", data = cf )

res = model.fit()

print res.summary()

df = open ("/Users/cmdb/data/day4/FPKM_GC_CpG_list.csv")

x = []
y = []

print type(df)

i = 0

for lines in df:
    if i > 0:
        x.append(float(lines.split(", ")[1].rstrip("\n")))
        y.append(float(lines.split(", ")[3].rstrip("\n")))
    i+=1

fit=polyfit(x,y,1)
fit_fn = poly1d(fit)

plot(x,y,'yo', x, fit_fn(x), '--k')
xlim(0, 1000)
ylim(0, 0.25)
xlabel("FPKM")
ylabel("CpG occurence")
savefig("day4_regression_FPKM_CpG")