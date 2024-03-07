#!/usr/bin/env python
# coding: utf-8

# # US Accidents Exploratory Data Analysis

# In[ ]:


#talk about EDA

#talk about the dataset (source, what it contains, how it will be useful)

#Kaggle
#informaiton about accidents
#can use useful to prevent accidents

##Findings
#Miami is the city with highest accidents
#CA is the state with highest accidents
#Cannot find New York in the highest accidents citis list desipte of it being highiest populated city
#Found out New York is excluded from the data
#Less than 10% of cities have more than 1000 yearly accident
#More the 3100 cities have reported less than 5 accidents in a year, it is suspected that the data is not accurately reported. Hence it is safe to remove those cities from the list
#There is exponential decrease in the cities with number of accidents greater than 1000
#High percentage of accidents happens from 7 to 10 and 15 to 19 probably because of most of the people go and come from offices
#High percentage of accidents happens during weekdays
#Number of accidents is consistant accross all months of the year, it is higest in December
#There is inconsistancy in data collection across years 
#Source2 has given the balanced data however there is some incosistancy with Source1, it can you inferred that lot of data is missing from Source1
#Per the pie chart we can say that wheather has no impact on number of accidents


# In[3]:


# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")


# In[4]:


df = pd.read_csv("/Users/rithviksharma/Downloads/US_Accidents_March23.csv")# Data Loading


# In[ ]:


# Basic Data Overview


# In[5]:


df # Displays the DataFrame


# In[6]:


df.info() # Information about DataFrame


# In[7]:


df.describe() # Descriptive statistics


# In[46]:


# Numeric Data Identification

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)

len(numeric_df.columns)


# In[9]:


# Missing Data Analysis

missing_percent = (df.isna().sum() / len(df)).sort_values(ascending=False)
missing_percent


# In[10]:


# Plot missing data percentages
missing_percent[missing_percent != 0].plot(kind='barh')


# In[11]:


# Dropping Columns with High Missing Values

drop_column = missing_percent[missing_percent>0.2].index
df.drop(columns=drop_column)


# In[12]:


# Analyzing Accidents by City

cities = df.City.unique()
len(cities)


# In[13]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[14]:


cities_by_accident[:20]


# In[15]:


'New York' in df.City # Accidents in New York and NY State


# In[16]:


'NY' in df.State # Accidents in New York and NY State


# In[48]:


#Sort the Series in ascending order and select the top 20 cities
cities_by_accident_sorted = cities_by_accident.sort_values(ascending=True).tail(20)

# Plot in a horizontal bar chart
cities_by_accident_sorted.plot(kind='barh', figsize=(10, 8))


# In[50]:


state_by_accident = df.State.value_counts()

#Sort the Series in ascending order and select the top 20 cities
State_by_accident_sorted = state_by_accident.sort_values(ascending=True).tail(20)

# Plot in a horizontal bar chart
State_by_accident_sorted.plot(kind='barh', figsize=(10, 8))


# In[18]:


# Accidents Distribution Among High and Low Incident Cities

cities_by_accident_low = cities_by_accident[cities_by_accident<1000]
cities_by_accident_high = cities_by_accident[cities_by_accident>=1000]


# In[19]:


len(cities_by_accident_high)/len(cities)


# In[20]:


# Plotting Accident Distribution in High Incident Cities

sns.histplot(cities_by_accident_high,log_scale=True)


# In[21]:


# Plotting Accident Distribution in Low Incident Cities

sns.histplot(cities_by_accident_low,log_scale=True)


# In[22]:


cities_by_accident[cities_by_accident<=5]


# In[47]:


# Filtering Cities with Minimal Accidents

df = df.groupby('City').filter(lambda x: len(x) > 5)


# In[24]:


df


# In[25]:


df.Start_Time


# In[26]:


# Time Analysis of Accidents
# Distribution by Hour

df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')


# In[27]:


# Creating the distribution plot
sns.histplot(df.Start_Time.dt.hour, bins=24, kde=False, stat='probability')


# In[28]:


# Distribution by Day of Week

sns.histplot(df.Start_Time.dt.dayofweek, bins=7, kde = False, stat='probability')


# In[29]:


# Monthly Accidents Distribution for Each Year (2016-2022)

df_yearly = df[df.Start_Time.dt.year == 2016]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[30]:


df_yearly = df[df.Start_Time.dt.year == 2017]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[31]:


df_yearly = df[df.Start_Time.dt.year == 2018]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[32]:


df_yearly = df[df.Start_Time.dt.year == 2019]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[33]:


df_yearly = df[df.Start_Time.dt.year == 2020]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[34]:


df_yearly = df[df.Start_Time.dt.year == 2021]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[35]:


df_yearly = df[df.Start_Time.dt.year == 2022]
sns.histplot(df_yearly.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[37]:


df_yearly = df[df.Start_Time.dt.year == 2019]
source1 = df_yearly[df_yearly.Source == 'Source1' ]
sns.histplot(source1.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[38]:


df_yearly = df[df.Start_Time.dt.year == 2019]
source2 = df_yearly[df_yearly.Source == 'Source2' ]
sns.histplot(source2.Start_Time.dt.month, bins=12, kde = False, stat='probability')


# In[39]:


# Data Source Analysis

df.Source.value_counts().plot(kind='pie')


# In[40]:


df.Start_Lat


# In[41]:


df.Start_Lng


# In[42]:


# Geographic Distribution of Accidents

sns.scatterplot(x=df.Start_Lng, y=df.Start_Lat, size=0.001)


# In[43]:


# Heatmap of Accidents

get_ipython().system('pip install folium --quiet folium')
import folium
from folium.plugins import HeatMap


# In[45]:


sample_df = df.sample(int(0.001 * len(df)))
lat_lon_pairs = list(zip(list(sample_df.Start_Lat),list(sample_df.Start_Lng)))
heat_map = folium.Map()
HeatMap(lat_lon_pairs).add_to(heat_map)
heat_map


# In[63]:


weather_condition = df['Weather_Condition'].value_counts()
weather_condition_filtered = weather_condition.head(10)
weather_condition_filtered


# In[64]:


weather_condition_filtered.plot(kind='pie')

