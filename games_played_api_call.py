# This file uses the teams id to collect the teams (NAME, CONFERENCE, POSITION IN TABLE) 
# and adds it to a dictionary where it's key is the teams ID

import requests
import pandas as pd
import json
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()
#url = "https://v1.basketball.api-sports.io/timezone"
url = "https://v1.basketball.api-sports.io/games?league=12&season=2022-2023&team=139&timezone=America/New_York"

payload = {}
headers = {
    'x-rapidapi-key': os.getenv('api_key'),
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
}

# The team_id_grab() function grabs the teams id,name,conference 
# and conference position and stores it in a DataFrame


# request.request sends a request of a specified method to the url (in this case the method is GET)
response = requests.request("GET", url, headers=headers, data=payload)

# json.loads deserialises a JSON object to a standard python object (good for parsing)
# also it turns nulls to a None python object
parsed_games = json.loads(response.text)
games = json.dumps(parsed_games, indent=4)
    
# Creating variables that hold the requests daily limit remaining (100 per day) 
# and the per minute requests remaining (10 per minute)
daily_calls_remaining = response.headers['x-ratelimit-requests-remaining']
perMinute_calls_remaining = response.headers['X-RateLimit-Remaining']

print(f'Daily calls remaining = {daily_calls_remaining}')
print(f'Calls left per minute = {perMinute_calls_remaining}\n')

print(games)



