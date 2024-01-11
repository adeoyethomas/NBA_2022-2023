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
url = "https://v1.basketball.api-sports.io/standings?league=12&season=2022-2023"

payload = {}
headers = {
    'x-rapidapi-key': os.getenv('api_key'),
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
}

# The team_id_grab() function grabs the teams id,name,conference 
# and conference position and stores it in a DataFrame

def team_id_grab():
    # request.request sends a request of a specified method to the url (in this case the method is GET)
    response = requests.request("GET", url, headers=headers, data=payload)

    # json.loads deserialises a JSON object to a standard python object (good for parsing)
    # also it turns nulls to a None python object
    standings = json.loads(response.text)

    # team_lvl (team level) grabs the section of the returned data that we need to parse through to collect 
    # info on the team
    team_lvl = standings['response'][0]
       
    # Creating a DataFrame to store the team API ids
    team_ids_df = pd.DataFrame(columns = ['Team', 'Team ID', 'Conference', 'Conference Position'])
     
    # Creating variables that hold the requests daily limit remaining (100 per day) 
    # and the per minute requests remaining (10 per minute)
    daily_calls_remaining = response.headers['x-ratelimit-requests-remaining']
    perMinute_calls_remaining = response.headers['X-RateLimit-Remaining']
    
    print(f'Daily calls remaining = {daily_calls_remaining}')
    print(f'Calls left per minute = {perMinute_calls_remaining}\n')

    df_row = 0

    for team in team_lvl:
        if team['group']['name'] == "Western Conference" or team['group']['name'] == "Eastern Conference":
            t_id = int(team['team']['id'])
            t_name = team['team']['name']
            t_conference = team['group']['name']
            t_position = str(team['position'])

            team_ids_df.loc[df_row] = [t_name, t_id, t_conference, t_position]
            df_row += 1
    return team_ids_df

# Uncomment the lines below to make sure the function returns the correct information
# team_ids_df = team_id_grab()
# print(team_ids_df)


