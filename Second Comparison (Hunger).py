#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import mplcursors


# In[3]:


def loadList(fileName):
  with open(fileName, newline='') as f:
    reader = csv.reader(f)
    dataList = list(reader)
  return dataList


def aggregate(finalList, row):
    
    finalList.append(row)
    
    
    


# In[4]:


col = {"Country":0,"Code":1,"Year":2,"Average":3}

data = loadList('school.csv')

schoolList = []
for n in range(len(data)):
    if (data[n][col["Year"]]) =='2017':
        schoolList.append(data[n])
print (schoolList)
    


# In[5]:


col = {"Country":0,"Code":1,"Year":2,"Hunger":3}
data = loadList('hunger.csv')
hungerList = []


hungerList = []
for n in range (0,len(data)):
    if int(data[n][col["Year"]]) ==2016:
        aggregate(hungerList, data[n])

print(hungerList)
        


# In[6]:


n = 0
masterList = []
while n < len(schoolList):
    p = 0
    countryCode = schoolList[n][col['Code']]
    while p < len(hungerList) and countryCode != hungerList[p][1]:
        p+=1
    if p < len(hungerList):
        masterList.append([schoolList[n][0], float(schoolList[n][3]), float(hungerList[p][3])])
    n+=1
print (masterList)


# In[7]:


n = 0
df = pd.DataFrame(masterList, columns = {"Country":0,"School":1,"Hunger":2})
df


# In[8]:


print (df['Country'])
print (df['School'])
print (df['Hunger'])


# In[12]:


x = (df['School'])
y = (df['Hunger'])
    

colors = ['r','g','b','c','m','y','k']
color = ['w']
c = []
for i in range (0,len(x)):
    if y[i] >= 15:
        c += ['r']
    elif y[i] >= 10:
        c += ['y']
    elif y[i] >= 4:
        c += ['g']
    else:
        c += ['b']
    
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
plt.ylim([0, 30])
plt.xlabel("Years of Schooling", size = 15, color = 'w', fontname='Times')
plt.ylabel("Percentage of Population Without Proper Acess to Food", size = 15, color = 'w', fontname='Times')
plt.title('Years Of Schooling Vs Hunger Rate', size = 15, color = 'w', fontname='Times')
plt.show()


# In[ ]:




