#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt


# In[2]:


#how the California real estate market has been affected by the increase in interest rate. 
pd.set_option('display.max_columns', 30)


# In[3]:


ca_real_estate = pd.read_csv("Resources/California_Real_Estate_Raw_Data_Set.csv")


# In[4]:


ca_real_estate_df = ca_real_estate


# In[5]:


ca_real_estate_df.rename(columns = {"Contract Status Change Date": "Date"}, inplace = True)


# In[6]:


ca_real_estate_df.Date = pd.to_datetime(ca_real_estate_df.Date, format = "%m/%d/%y")


# In[7]:


ca_real_estate_df["month"] = ca_real_estate_df.Date.dt.month


# In[8]:


ca_real_estate_df[['Price Per Square Foot']] = ca_real_estate_df[['Price Per Square Foot']].replace('[\$,]','',regex=True).astype(float)


# In[9]:


ca_real_estate_df.columns


# In[10]:


ca_real_estate_df[['L/C Price']] = ca_real_estate_df[['L/C Price']].replace('[\$,]','',regex=True).astype(float)


# In[11]:


ca_real_estate_df[["Sqft"]] = ca_real_estate_df.Sqft.str.split('/', expand=True).drop([1], axis = 1)


# In[12]:


ca_real_estate_df[["YrBuilt"]] = ca_real_estate_df.YrBuilt.str.split('/', expand=True).drop([1], axis = 1)


# In[13]:


ca_real_estate_df[["Bed & Bath", "A", "B", "C"]] = ca_real_estate_df['Br/Ba'].str.split(",", expand = True)
ca_real_estate_df[["Bed", "Bath"]] = ca_real_estate_df["Bed & Bath"].str.split("/", expand = True)
#fix bathroom into a float


# In[14]:


ca_real_estate_df =ca_real_estate_df.drop(columns = ['Bed & Bath'])


# In[15]:


ca_real_estate_df.rename(columns = {"Sqft": "Sqft/A"}, inplace = True)
ca_real_estate_df[["LSqft", "Ac"]] = ca_real_estate_df['LSqft/Ac'].str.split('/', expand = True).replace('[\$,]','',regex=True).astype(float)




real_estate_df = ca_real_estate_df

real_estate_df = pd.DataFrame(real_estate_df)





