#!/usr/bin/env python
# coding: utf-8

# # Scrapping Quotes,Author names and Tags from the provided url:http://quotes.toscrape.com/page/1/

# In[2]:


get_ipython().system('pip install bs4')


# In[3]:


get_ipython().system('pip install requests')


# In[ ]:





# In[4]:


#importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[5]:


url = "http://quotes.toscrape.com/page/1/"


# In[6]:


res= requests.get(url)


# In[7]:


html = BeautifulSoup(res.content,'html.parser')


# In[8]:


html


# In[9]:


ol=html.find('div')


# # First we are finding all contents for page no.1

# In[10]:


#To find Quotes
result = ol.find_all('span',class_ = 'text')
print(result)


# In[11]:


#To find Author
result1 = ol.find_all('small',class_ = 'author')
print(result1)


# In[37]:


#To find Tags
result2 = ol.find_all('a',class_ = 'tag')
print(result2)


# # Filtering and editing our content and storing in a list named Content[]

# In[38]:


Content = []
for quote,author,tag in zip(result,result1,result2):
    quote =quote.text.strip()
    author = author.text.strip()
    tag = tag.text.strip()
    Content.append([quote,author,tag])


# # Converting into Dataframe

# In[39]:


df = pd.DataFrame(Content,columns =['Quote','Author','Tags'])


# In[40]:


df.head(5)


# # Scrapping data from first five page and storing it in a list

# In[46]:


Content =[]

for i in range(1,5):
    url = f"http://quotes.toscrape.com/page/{i}/"
    res= requests.get(url)
    html = BeautifulSoup(res.content,'html.parser')
    ol=html.find('div')
    result = ol.find_all('span',class_ = 'text')
    result1 = ol.find_all('small',class_ = 'author')
    result2 = ol.find_all('a',class_ = 'tag')

    for quote,author,tag in zip(result,result1,result2):
        quote =quote.text.strip()
        author = author.text.strip()
        tag = tag.text.strip()
        Content.append([quote,author,tag])


# In[47]:


df = pd.DataFrame(Content,columns =['Quotes','Author','Tags'])


# In[48]:


df.head(20)


# # Converting scrapped data in to CSV file

# In[49]:


df.to_csv('Quotes.csv')


# In[ ]:


#End

