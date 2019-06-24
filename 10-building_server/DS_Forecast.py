#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Using APIs/Data Structures
# Using the Dark Sky Forecast API at https://developer.forecast.io/, generate a sentence that describes the weather that day.

# Right now it is TEMPERATURE degrees out and SUMMARY. Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.

# TEMPERATURE is the current temperature
# SUMMARY is what it currently looks like (partly cloudy, etc - it's "summary" in the dictionary). Lowercase, please.
# TEMP_FEELING is whether it will be hot, warm, cold, or moderate. You will probably use HIGH_TEMP and your own thoughts and feelings to determine this.
# HIGH_TEMP is the high temperature for the day.
# LOW_TEMP is the low temperature for the day.
# RAIN_WARNING is something like "bring your umbrella!" if it is going to rain at some point during the day.


# In[2]:


import requests
from bs4 import BeautifulSoup
import dotenv
import datetime


# In[3]:


from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("DARKSKY_API_KEY")
MAIL_API = os.getenv('MAILGUN_API_KEY')


# In[4]:


response = requests.get(f'https://api.darksky.net/forecast/{API_KEY}/40.7128,-74.0060?units=si')
new_york_weather = response.json()


# In[5]:


new_york_weather.keys()


# In[6]:


currently  = new_york_weather['currently']
today = new_york_weather['daily']['data'][0]

TEMPERATURE = currently['temperature']
SUMMARY = currently['summary'].lower()
HIGH_TEMP = today['temperatureHigh']
LOW_TEMP = today['temperatureLow']

if HIGH_TEMP > 30:
    TEMP_FEELING = 'hot'
elif HIGH_TEMP > 25:
    TEMP_FEELING = 'warm'
elif HIGH_TEMP > 15:
    TEMP_FEELING = 'moderate'
else:
    TEMP_FEELING = 'cold'

if today['icon'] == 'rain':
    RAIN_WARNING = 'bring your umbralla'
else:
    RAIN_WARNING = ''
    
text = f'Right now it is {TEMPERATURE} degrees out and {SUMMARY}. Today will be {TEMP_FEELING} with a high of {HIGH_TEMP} and a low of {LOW_TEMP}. {RAIN_WARNING}.'


# In[7]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d, %Y")

title = f'8AM Weather forecast: {date_string}'


# In[8]:



response = requests.post(
        "https://api.mailgun.net/v3/sandboxa3143f679f974eb882f4c0b75d815986.mailgun.org/messages",
        auth=("api", MAIL_API ),
        data={"from": "Excited User <mailgun@sandboxa3143f679f974eb882f4c0b75d815986.mailgun.org>",
            "to": ["taylorlau.yee@hotmail.com", "hl3289@columbia.edu"],
            "subject": title,
            "text": text})
response.text


# In[ ]:




