import requests
import json
from dotenv import load_dotenv
import os
from team_identifiers_grab import team_info

def configure():
    load_dotenv

configure()

# Gets stats for an NBA team via api-basketball.com api

url = "https://v1.basketball.api-sports.io/statistics?season=2022-2023&team=139&league=12"

payload = {}
headers = {
    'x-rapidapi-key': os.getenv('api_key'),
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
}

t_ids_dict = team_info()
team_ids = [k for k in  t_ids_dict.keys()]

print(team_ids)


split = team_ids[:3]
print(split)

# response = requests.request("GET", url, headers=headers, data=payload)

# # Parses the JSON
# team_statistics = json.loads(response.text)
# # print(json.dumps(team_statistics, indent=4))

# ppg_for = team_statistics["response"]["points"]["for"]["average"]["all"]
# ppg_against = team_statistics["response"]["points"]["against"]["average"]["all"]
# team_name = team_statistics["response"]["team"]["name"]

# print('=====================================================================================')

# print("Team Name is: " + team_name)
# print(team_name +" " + "scored"+ " " + str(ppg_for) + " " + "ppg")
# print(team_name + " " + "conceded" + " " + str(ppg_against) +" " + "ppg")

# print('=====================================================================================')

# # print(json.dumps(response.headers))

# daily_calls_remaining = response.headers['x-ratelimit-requests-remaining']
# perMinute_calls_remaining = response.headers['X-RateLimit-Remaining']

# print('Daily calls remaining = ' + daily_calls_remaining)
# print('Calls left per minute = ' + perMinute_calls_remaining)

#     # time.sleep(7)
