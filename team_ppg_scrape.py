import requests
import json
from dotenv import load_dotenv
import os
from team_identifiers_grab import team_info
import time

def configure():
    load_dotenv

configure()

t_ids_dict = team_info()
team_ids = [k for k in  t_ids_dict.keys()]

# split = team_ids[:3]
# print(split)

def team_ppg():
    t_ppg_dict = dict()

    for id in team_ids:
        t_id = id
        # API URL for NBA team data via api-basketball.com
        url = "https://v1.basketball.api-sports.io/statistics?season=2022-2023&team="+t_id+"&league=12"

        payload = {}
        headers = {
            'x-rapidapi-key': os.getenv('api_key'),
            'x-rapidapi-host': 'v1.basketball.api-sports.io'
        }

        daily_calls_remaining = 1
        perMinute_calls_remaining = 1

        # if statement to make sure I don't go over the API's free version daily and per minunte limit
        if perMinute_calls_remaining > 0 and daily_calls_remaining > 0: 
            response = requests.request("GET", url, headers=headers, data=payload)
            # request.request sends a request of a specified method to the url (in this case the method is GET)

            # Parses the JSON
            team_statistics = json.loads(response.text)
            # Use the print statment below to check the layout of the data pulled with the GET request
            # print(json.dumps(team_statistics, indent=4))

            daily_calls_remaining = int(response.headers['x-ratelimit-requests-remaining'])
            perMinute_calls_remaining = int(response.headers['X-RateLimit-Remaining'])

            ppg_for = team_statistics["response"]["points"]["for"]["average"]["all"]
            ppg_against = team_statistics["response"]["points"]["against"]["average"]["all"]
            team_name = team_statistics["response"]["team"]["name"]

            print('=====================================================================================')

            print("Team Name is: " + team_name)
            print(team_name +" " + "scored"+ " " + str(ppg_for) + " " + "ppg")
            print(team_name + " " + "conceded" + " " + str(ppg_against) +" " + "ppg", '\n')

            print('Daily calls remaining = ' + str(daily_calls_remaining))
            print('Calls left per minute = ' + str(perMinute_calls_remaining), '\n')

            t_ppg = {'team_name': team_name, 'ppg_for': ppg_for, 'ppg_against': ppg_against}
            t_ppg_dict[t_id] = t_ppg
            print(t_ppg_dict)

            time.sleep(7)
            # Sleep for 7 seconds to avoid having more than 10 calls per minute as I am using the free API
           
        else:
            break

    return t_ppg_dict

print(team_ppg())