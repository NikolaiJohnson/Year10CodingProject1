#!/usr/bin/env python
# coding: utf-8

# In[11]:


import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import mplcursors


# In[12]:


def loadList(fileName):
  with open(fileName, newline='') as f:
    reader = csv.reader(f)
    dataList = list(reader)
  return dataList


def aggregate(finalList, row):
    
    finalList.append(row)
    
    
    


# In[17]:


col = {"Country":0,"Code":1,"Year":2,"Average":3}
data = loadList('school.csv')
schoolList = []


schoolList = []
for n in range (0,len(data)):
    if int(data[n][col["Year"]]) ==2017:
        aggregate(schoolList, data[n])

print(schoolList)
        


# In[18]:


col = {"Country":0,"Code":1,"Year":2,"Tourism":3}
data = loadList('tourism.csv')
tourismList = []


tourismList = []
for n in range (0,len(data)):
    if int(data[n][col["Year"]]) ==2017:
        aggregate(tourismList, data[n])

print(tourismList)
        


# In[19]:


n = 0
masterList = []
while n < len(schoolList):
    p = 0
    countryCode = schoolList[n][col['Code']]
    while p < len(tourismList) and countryCode != tourismList[p][1]:
        p+=1
    if p < len(tourismList):
        masterList.append([schoolList[n][0], float(schoolList[n][3]), float(tourismList[p][3])])
    n+=1
print (masterList)


# In[20]:


n = 0
df = pd.DataFrame(masterList, columns = {"Country":0,"School":1,"Tourism":2})
df


# In[22]:


print (df['Country'])
print (df['School'])
print (df['Tourism'])


# In[33]:


x = (df['School'])
y = (df['Tourism'])
    

colors = ['r','g','b','c','m','y','k']
color = ['w']
c = []
for i in range (0,len(x)):
    if y[i] >= 30000000:
        c += ['b']
    elif y[i] >= 10000000:
        c += ['g']
    elif y[i] >= 4000000:
        c += ['y']
    else:
        c += ['r']
    
m, b = np.polyfit(x,y,1)
fitEquation = m*x+b

s = []
for i in range(0,len(x)):
    s += [100]
    

plt.figure(figsize = (50,50))
fig,ax = plt.subplots()
dots = ax.scatter(x, y, s, c=c)
annotations = []
for i in range (0,len(x)):
    annotations+=[df['Country'][i]]
#     if y[i] > 10:
#         annotations+=[df['Country'][i]]
#     else:
#         annotations+=[""]
    
#for i in range(len(annotations)):
   # plt.annotate(annotations[i], (x[i], y[i]))



font = {'family' : 'Vogue',
        'weight' : 'bold'}

plt.rc('font', **font)


fig.set_facecolor('xkcd:darkish blue')
ax.set_facecolor('xkcd:silver')

ax.tick_params(axis='x', colors='white') 
ax.tick_params(axis='y', colors='white') 

#mplcursors.cursor(multiple = True).connect(
#     "add", lambda sel: sel.annotation.set_text(
#           annotations[sel.target.index]
# )
for tick in ax.get_xticklabels():
    tick.set_fontname("Times")
for tick in ax.get_yticklabels():
    tick.set_fontname("Times")

plt.plot(x, fitEquation, color='red')
cursor = mplcursors.cursor(dots)
cursor.connect("add",lambda sel: sel.annotation.set_text(annotations[sel.index]))
plt.ylim([0, 65000000])
plt.xlabel("Years of Schooling", size = 15, color = 'w', fontname='Times')
plt.ylabel("Number of Tourists Per Year(In Tens of Millions)", size = 15, color = 'w', fontname='Times')
plt.title('Years Of Schooling Vs Annual Tourists', size = 15, color = 'w', fontname='Times')
plt.show()


# In[ ]:




