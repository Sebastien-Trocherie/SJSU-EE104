# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:56:05 2022

@author: troch
"""

import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 250

data = hp.get_data('data.csv')

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

#run analysis
wd, m = hp.process(data, sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display computed measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))