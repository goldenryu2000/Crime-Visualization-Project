#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pygal
from pygal.style import DarkStyle


# In[34]:


l = ['Offences Relating to Documents & Property Marks' , 'Miscellaneous IPC Crimes' , 
     'Offences Affecting the Human Body','Offences Affecting the Human Body-2','Offences against Property',
    'Offences against Public Tranquillity','Offences against the State']


# In[37]:


for i in l: 
    df = pd.read_csv("Raw Data/csv-files/{}.csv".format(i))
    ch = list(df.get('Crime Head'))
    a = list(df.get('2017'))
    b = list(df.get('2018'))
    c = list(df.get('2019'))
    a = [int(x) for x in a]
    b = [int(y) for y in b]
    c = [int(z) for z in c]
    # 2017
    bar_chart = pygal.Pie(fill=True , style= DarkStyle)
    bar_chart.title = "{}-2017".format(i)
    for j in range(len(ch)):
        bar_chart.add(ch[j],a)
    bar_chart.render_to_file('svg-files/{}/{}-2017.svg'.format(i,i)) 
    # 2018
    bar_chart = pygal.Pie(fill=True , style= DarkStyle)
    bar_chart.title = "{}-2018".format(i)
    for k in range(len(ch)):
        bar_chart.add(ch[k],b)
    bar_chart.render_to_file('svg-files/{}/{}-2018.svg'.format(i,i)) 
    # #2019
    bar_chart = pygal.Pie(fill=True , style= DarkStyle)
    bar_chart.title = "{}-2019".format(i)
    for m in range(len(ch)):
        bar_chart.add(ch[m],c)
    bar_chart.render_to_file('svg-files/{}/{}-2019.svg'.format(i,i))
    print("created svg for {}".format(i))


# In[ ]:




