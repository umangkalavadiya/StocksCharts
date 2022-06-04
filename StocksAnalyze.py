#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr


# In[3]:


end = dt.datetime.now()
start = end - dt.timedelta(days=5000)
start,end


# In[4]:


stockList = ['RELIANCE','ADANIPOWER','TATAMOTORS','TCS']
stocks = [i+ '.NS' for i in stockList]
stocks


# In[6]:


df = pdr.get_data_yahoo(stocks,start,end)
df.head()


# In[7]:


df.index


# In[8]:


df.columns


# In[9]:


Close = df.Close
Close.head()


# In[12]:


Close[Close.index > end - dt.timedelta(days=100)].describe(percentiles=[0.1,0.5,0.9])


# In[ ]:





# In[15]:


Close.plot(figsize=(12,8))


# In[ ]:





# In[16]:


import plotly.offline as pyo


# In[17]:


pyo.init_notebook_mode(connected=True)


# In[18]:


pd.options.plotting.backend='plotly'


# In[19]:


Close.plot()


# In[ ]:





# In[21]:


Close['RELIANCE.NS'].pct_change().plot(kind='hist')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




