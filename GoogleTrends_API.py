
# coding: utf-8

# ## Google Trends API using Python 3.7
# 
# 
# Error in python 3.7 package:
# 
# from pandas.io.json import json_normalize ModuleNotFoundError: No module named 'pandas.io'; 'pandas' is not a package
# 
# Solution:https://stackoverflow.com/questions/57218531/modulenotfounderror-no-module-named-pandas-io-for-json-normalize
# 
# + Go to ...\Lib\site-packages\pytrends on your local disk and open file request.py
# + Change: *from **pandas.io.json._normalize** import nested_to_record* to **from pandas.io.json.normalize** import nested_to_record*

# In[69]:


import pandas as pd
from pytrends.request import TrendReq
wlist='coronavirus'
pytrend=TrendReq()
pytrend.build_payload(kw_list=[wlist])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)
tlist=df.sort_values(wlist,ascending=False).head(n=10)
tlist


# In[70]:


tlist.reset_index().plot(x='geoName', y=wlist, figsize=(15, 10), kind ='bar');


# In[42]:


df.reset_index().plot(x='geoName', y='Coronavirus', figsize=(50, 30), kind ='bar');


# In[75]:


# Get Google Hot Trends data
df = pytrend.trending_searches(pn='canada')
df.head()


# In[74]:


pytrend.trending_searches()


# In[80]:


df = pytrend.today_searches(pn='IT')
df.head(n=10)


# In[32]:


# Get Google Keyword Suggestions
keywords = pytrend.suggestions(keyword='Coronavirus')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid')   # This column makes no sense


# In[81]:


pytrend.build_payload(kw_list=['Coronavirus'])


# In[82]:


# Related Queries, returns a dictionary of dataframes
related_queries = pytrend.related_queries()
related_queries.values()


# In[35]:


related_topic = pytrend.related_topics()
related_topic.values()


# In[83]:


pytrends.suggestions('Coronavirus')


# In[89]:


pytrend.build_payload(kw_list=['hamburgo'])
related_queries = pytrend.related_queries()
related_queries.values()

