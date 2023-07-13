#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Reading a sample dataset for the analysis
df=pd.read_csv('movies.csv')


# In[3]:


#To print the loaded dataset
df


# In[4]:


#Top 5 rows in the dataset
df.head()


# In[5]:


#To check if there are any null values in the dataset
df.isnull().sum()


# In[6]:


df.info()


# In[7]:


#Number of rows and columns in the dataset taken
df.shape


# In[8]:


#Attributes in the Dataset
for i in df.columns:
    print(i,end=",")


# In[9]:


#1.Top 5 imdb most rated movie names
for name in df.head()['name'].values:
    print(name)


# In[10]:


#2.Top most 5 voted movies
for name in df.sort_values(by='imbd_votes', ascending = False).head()['name'].values:
    print(name)


# In[11]:


#3.Oldest Movie in the dataset
for name in df.sort_values(by='imbd_votes', ascending = True).head(1)['name'].values:
    print(name)


# In[12]:


#4.To obtain the movie of only particular genre Ex:Crime,Drama
c=0
for genre in df['genre']:
    if genre=='Crime,Drama':
        c+=1
print(c)


# In[13]:


#5.To obtain the movies that are included with some particular genre Ex:Crime,Drama along with some other genre
c=0
for genre in df['genre']:
    if (genre in 'Crime,Drama'):
        c+=1
print(c)


# In[14]:


#6.Unique genre available
genres=[]
for i in df['genre']:
    genres +=i.split(',')
uni_gen=list(set(genres))
uni_gen


# In[15]:


#7.To know how many times each genre is there in the dataset
for gen in uni_gen:
    c=0
    for genre in df['genre']:
        if (gen in genre):
            c+=1
    print(gen,'--',c)


# In[16]:


#8.What are the most common genres?
common_genres = df['genre'].str.split(',', expand=True).stack().value_counts()
common_genres.plot(kind='bar', figsize=(10, 6))


# In[17]:


#9.Who are the top-rated directors?
top_directors = df.groupby('director_name')['imdb_rating'].mean().nlargest(10)
top_directors.plot(kind='bar', figsize=(10, 6))


# In[18]:


#10.What is the average duration of movies?
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
average_duration = df['duration'].mean()
average_duration


# In[19]:


#11.Which movies have the same director and writer?
same_director_writer = df[df['director_id'] == df['writter_id']]
same_director_writer[['name', 'director_name']].head(10)


# In[20]:


#12.Who are the most frequent cast members in movies?
top_cast_members = df['cast_name'].str.split(',', expand=True).stack().value_counts().head(10)
top_cast_members.plot(kind='bar', figsize=(10, 6))


# In[21]:


#13.Plotting IMDb rating vs. number of votes

sns.scatterplot(data=df, x='imbd_votes', y='imdb_rating')
plt.title('IMDb Rating vs. Number of Votes')
plt.xlabel('Number of Votes')
plt.ylabel('IMDb Rating')
plt.show()


# In[22]:


#14.Convert 'duration' column to numeric
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
#16.Plotting movie duration distribution
sns.boxplot(data=df, y='duration')
plt.title('Movie Duration Distribution')
plt.xlabel('Duration')
plt.ylabel('Movie Duration')
plt.show()

