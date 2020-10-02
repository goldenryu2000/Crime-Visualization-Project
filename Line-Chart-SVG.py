#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pygal
from pygal.style import DarkStyle


# In[23]:


l = ['Offences Relating to Documents & Property Marks' , 'Miscellaneous IPC Crimes' , 
     'Offences Affecting the Human Body','Offences Affecting the Human Body-2','Offences against Property',
    'Offences against Public Tranquillity','Offences against the State']


# In[25]:


for t in l:
    line_chart = pygal.Line(style=DarkStyle)
    line_chart.x_labels = '2017','2018','2019'
    line_chart.title = '{}-(2017-2019)'.format(t)
    df = pd.read_csv("Raw Data/csv-files/{}.csv".format(t))
    print("Writing {}.svg".format(t))
    ch = list(df.get('Crime Head'))
    a = list(df.get('2017'))
    b = list(df.get('2018'))
    c = list(df.get('2019'))
    a = [int(x) for x in a]
    b = [int(y) for y in b]
    c = [int(z) for z in c]
    for i in range(len(ch)):
        line_chart.add(ch[i],[a[i],b[i],c[i]]) 
    line_chart.render_to_file('svg-files/Line-charts/{}.svg'.format(t)) 

