#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


df = pd.read_csv("c:/Users/Hulk/Desktop/practica Jupyter/DATASETS/weather_data.csv")


# ### Temperaturas en la ciudad de Nueva York

# In[3]:


df


# ### Temperatura mas alta

# In[4]:


df['Temperature'].max()


# ### Dias que llovio

# In[5]:


df['EST'][df['Events']=='Rain']


# ### Velocidad promedio del viento

# In[6]:


df.fillna(0, inplace=True)
df['WindSpeedMPH'].mean()


# In[ ]:




