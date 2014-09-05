#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as mpl
import statsmodels.api as sm
from pylab import *

cf = pd.read_csv("/Users/cmdb/data/day4/FPKM_GC_list.csv")

model = sm.formula.ols( formula = "FPKM ~ GC_ratio", data = cf )

res = model.fit()

print res.summary()

df = open ("/Users/cmdb/data/day4/FPKM_GC_list.csv")

x = []
y = []

print type(df)

i = 0

for lines in df:
    if i > 0:
        x.append(float(lines.split(", ")[1]))
        y.append(float(lines.split(", ")[2].rstrip("\n")))
    i+=1

fit=polyfit(x,y,1)
fit_fn = poly1d(fit)

plot(x,y,'yo', x, fit_fn(x), '--k')
xlim(0, 1000)
xlabel("FPKM")
ylabel("GC ratio")
savefig("day4_regression")