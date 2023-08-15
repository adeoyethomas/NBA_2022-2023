# This file uses the teams id to collect the teams (NAME, CONFERENCE, POSITION IN TABLE) 
# and adds it to a dictionary where it's key is the teams ID

import requests
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

# The team_info() function grabs the teams id,name,conference and position
# and organises them in a dictionary where the teams id is the key


def team_info():
    response = requests.request("GET", url, headers=headers, data=payload)
    # request.request sends a request of a specified method to the url (in this case the method is GET)

    standings = json.loads(response.text)
    # json.loads deserialises a JSON object to a standard python object (good for parsing)

    t_lvl = standings['response'][0]
    # t_lvl (team level) grabs the section of the returned data that we need to parse through to collect 
    # info on the team
   
    t_ids_dict = dict()
    # Creating an empty dictionary to store team info called t_ids_dict (team ids dictionary) 
     
    daily_calls_remaining = response.headers['x-ratelimit-requests-remaining']
    perMinute_calls_remaining = response.headers['X-RateLimit-Remaining']
    # Created variables that hold the requests daily limit remaining (100 per day) 
    # and the per minute requests remaining (10 per minute)

    print('Daily calls remaining = ' + daily_calls_remaining)
    print('Calls left per minute = ' + perMinute_calls_remaining,'\n')

    for team in t_lvl:
        if team['group']['name'] == "Western Conference" or team['group']['name'] == "Eastern Conference":
            t_id = str(team['team']['id'])
            t_name = team['team']['name']
            t_conference = team['group']['name']
            t_position = str(team['position'])

#Use the lines below to test that the data for each team is correct
            # print('team id = ' + t_id)
            # print('team name is ' + t_name)
            # print('the team is in the ' + t_conference)
            # print('the team finished ' + t_position + ' in the ' + t_conference,'\n')
            # print('============================================================','\n')

        t_info = {'team_name': t_name, 'conference': t_conference, 'league_position': t_position}
        t_ids_dict[t_id] = t_info


    return t_ids_dict

# Uncomment the line below to test if the function provides the desired structure
# print(team_info())


