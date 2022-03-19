#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install requests


# In[3]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url=('https://www.imdb.com/search/title/?sort=user_rating,desc&title_type=game')


# In[5]:


response=requests.get(url)


# In[6]:


response


# In[7]:


soup=BeautifulSoup(response.text)


# In[8]:


soup


# In[9]:


games=soup.select('.lister-item-header a')


# In[10]:


games


# In[11]:


games_list=[]


# In[12]:


for item in games:
    games_list.append(item.text)


# In[13]:


games_list


# In[14]:


typeofgame=soup.select('.genre')


# In[15]:


typeofgame


# In[16]:


type_games=[]


# In[17]:


for item in typeofgame:
    type_games.append(item.text)


# In[18]:


type_games


# In[19]:


ratings=soup.select('.ratings-imdb-rating')


# In[20]:


ratings


# In[21]:


games_ratings=[]


# In[22]:


for item in ratings:
    games_ratings.append(item.text)


# In[23]:


games_ratings


# In[24]:


year=soup.select('.text-muted.unbold')


# In[25]:


release_year=[]


# In[26]:


for item in year:
    release_year.append(item.text)


# In[27]:


release_year


# In[28]:


votes=soup.select('.text-muted+ span')


# In[29]:


votes_games=[]
for item in votes:
    votes_games.append(item.text)


# In[30]:


votes_games


# In[31]:


pip install pandas


# In[32]:


import pandas as pd


# In[33]:


gamesimdb=pd.DataFrame(games_list, columns=['games name'])
gamesimdb['type of games']=type_games
gamesimdb['released year']=release_year
gamesimdb['rating']=games_ratings
gamesimdb['votes']=votes_games


# In[34]:


gamesimdb


# In[ ]:




