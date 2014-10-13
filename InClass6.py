
# coding: utf-8

# In[3]:

import pandas as pd


# In[54]:

import os, json, requests, pytables


# In[97]:

import numpy as np


# In[29]:

os.chdir("C:\Users\mkim\Documents")


# In[30]:

t1 = pd.read_csv("work_comma.csv")


# In[31]:

t2 = pd.read_table('work_tab.txt',sep='\s+')


# In[32]:

t3 = pd.read_table('stress2_1.txt',sep='\s+')


# In[33]:

r = requests.get('https://api.github.com/events')


# In[42]:

t=r.json()


# In[45]:

fields = ['created_at','public','type']


# In[46]:

data_fr = pd.DataFrame(t,columns = fields)


# In[48]:

data_fr.to_pickle('dframe_pickle')


# In[49]:

pd.read_pickle('dframe_pickle')


# In[55]:

store = pd.HDFStore('inclass6.h5')


# In[57]:

store['obj1'] = data_fr


# In[58]:

store['obj1']


# In[104]:

project = pd.read_csv('Cars93.csv')


# In[105]:

project.describe()


# In[106]:

categorical = pd.cut(project.Horsepower,[0,100,200,300])


# In[107]:

categorical


# In[108]:

pd.value_counts(categorical)


# In[109]:

Speed = {'(0, 100]':'Slow','(100, 200]':'Slow','(200, 300]':'Slow'}


# In[110]:

cat =project['Horsepower'].map(Speed)


# In[111]:

project['Speed'] = cat


# In[112]:

project = project.rename(columns = {'Horsepower':'HP','Price':'Average Price'})


# In[113]:

sampler = np.random.permutation(len(project.index))


# In[114]:

project['rndm'] = sampler


# In[115]:

sampler1 = sampler[:len(project.index)/2]


# In[118]:

sample1 = project.take(sampler1)


# In[117]:

sampler2 = sampler[len(project.index)/2:len(project.index)]


# In[119]:

sample2 = project.take(sampler2)


# In[124]:

frame = sample1


# In[125]:

frame.append(sample2)


# In[126]:

frame.drop_duplicates()


# In[128]:

len(frame.index)


# In[ ]:



