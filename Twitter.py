#!/usr/bin/env python
# coding: utf-8

# # Markdown
# 
# - 1- Authentication,
# - 2- Get CSV file.
# - 3- Get unique tickers in order for us to search tweets that relate to them on twitter.
# - 4- Download the tweets that have those tickers. <------- Here.
# - 5- Create a model that can classify those tweets into Positive/Negative.
# - 6- Use the model in step 5 to classify the downloaded tweets in step 4.
# - 7- get only the positive tweets.
# - 8- Analysis.

# In[11]:


import pandas as pd
import tweepy
import numpy
import os
#import nltk


# In[14]:


consumerKey="lh8PpKHuWwF8h6DiTnL6GCSns"
consumerSecret="bR2tt7BitEqstnOGE8Vjm88eFkOk0frTyd72AR76I2RWAymgY1"
accessToken="243688593-4QY2mdaSjgz4qDNwFWhrBsCW6ZBJLkBWHkBxCoo4"
accessTokenSecret="2mF3OGsdZGP5sYZSC4fqihyp0bWFkT2o0T0rNSFH6Crm1"


# In[15]:


# Authentication
# consumerKey = os.getenv("TWITTER_API_KEY")
# consumerSecret = os.getenv("TWITTER_SECRET_KEY")
# accessToken = os.getenv("TWITTER_ACCESS_TOKEN")
# accessTokenSecret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


# In[ ]:





# In[16]:


import pandas as pd 


# In[17]:


df=pd.read_csv("https://raw.githubusercontent.com/joebary/Project_3_Team_1/main/ESG_data.csv")


# In[18]:


df


# In[19]:


keywords = list(df["Ticker"].unique())
keywords


# In[21]:


noOfTweet = 10_000
tweets = []
for keyword in keywords:
    tweets.append(tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet))


# In[23]:


list(tweets)


# In[ ]:




