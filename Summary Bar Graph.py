#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random


# In[33]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Factor = ['Poverty', 'Hunger', 'Tourism', 'Deaths', 'Corruption']
x = Factor
Correlation = [0.40,0.18,0.24,0.02,0.19]
h = Correlation
c = ['red', 'orange', 'yellow', 'green', 'blue']
ax.bar(Factor,Correlation)
fig.set_facecolor('xkcd:darkish blue')
ax.set_facecolor('xkcd:silver')
plt.xlabel("Factor", size = 15, color = 'w', fontname='Times')
plt.ylabel("Correlation", size = 15, color = 'w', fontname='Times')
ax.tick_params(axis='x', colors='white') 
ax.tick_params(axis='y', colors='white') 
for tick in ax.get_xticklabels():
    tick.set_fontname("Times")
for tick in ax.get_yticklabels():
    tick.set_fontname("Times")
plt.title('How Years Of Schooling Affected Each Factor', size = 15, color = 'w', fontname='Times')
plt.bar(x, height = h, color = c)
plt.show()


# In[ ]:




