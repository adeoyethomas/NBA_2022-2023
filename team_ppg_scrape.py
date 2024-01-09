import requests
import json
from dotenv import load_dotenv
import os
from team_identifiers_grab import team_id_grab
import time
import pandas as pd 

def configure():
    load_dotenv

configure()

# may not be needed anymore because using df's now
'''t_ids_dict = team_id_grab()
team_ids = [k for k in  t_ids_dict.keys()]'''

# split = team_ids[:3]
# print(split)

def team_ppg():
    team_ids_df = team_id_grab()
    team_ppg_df = pd.DataFrame(columns = ['Team', 'Team ID', 'PPG For', 'PPG Against'])

    team_ids = []
    df_row = 0

    for index, row in team_ids_df.iterrows():
        team_ids.append(row['Team ID'])

    for id in team_ids:
        t_id = str(id)
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

            team_ppg_df.loc[df_row] = [team_name, id, ppg_for, ppg_against]
            df_row += 1

            
            print('=====================================================================================')

            print(team_ppg_df)

            print('=====================================================================================')
            
            print('Daily calls remaining = ' + str(daily_calls_remaining))
            print('Calls left per minute = ' + str(perMinute_calls_remaining), '\n')

            time.sleep(7)
            # Sleep for 7 seconds to avoid having more than 10 calls per minute as I am using the free API
           
        else:
            break

    return team_ppg_df

team_ppg_df = team_ppg()