# Used this file as a test to make sure that I grab the correct information for a team
example_data = {
  "get": "statistics",
  "parameters": {
    "league": "12",
    "season": "2019-2020",
    "team": "139"
  },
  "errors": [],
  "results": 5,
  "response": {
    "league": {
      "id": 12,
      "name": "NBA",
      "type": "League",
      "season": "2019-2020",
      "logo": None
    },
    "country": {
      "id": 5,
      "name": "USA",
      "code": "US",
      "flag": "https://media.api-football.com/flags/us.svg"
    },
    "team": {
      "id": 139,
      "name": "Denver Nuggets",
      "logo": None
    },
    "games": {
      "played": {
        "home": 9,
        "away": 9,
        "all": 18
      },
      "wins": {
        "home": {
          "total": 7,
          "percentage": "0.778"
        },
        "away": {
          "total": 8,
          "percentage": "0.889"
        },
        "all": {
          "total": 15,
          "percentage": "0.833"
        }
      },
      "draws": {
        "home": {
          "total": 0,
          "percentage": "0.000"
        },
        "away": {
          "total": 0,
          "percentage": "0.000"
        },
        "all": {
          "total": 0,
          "percentage": "0.000"
        }
      },
      "loses": {
        "home": {
          "total": 2,
          "percentage": "0.222"
        },
        "away": {
          "total": 1,
          "percentage": "0.111"
        },
        "all": {
          "total": 3,
          "percentage": "0.167"
        }
      }
    },
    "points": {
      "for": {
        "total": {
          "home": 956,
          "away": 961,
          "all": 1917
        },
        "average": {
          "home": "106.2",
          "away": "106.8",
          "all": "106.5"
        }
      },
      "against": {
        "total": {
          "home": 911,
          "away": 902,
          "all": 1813
        },
        "average": {
          "home": "101.2",
          "away": "100.2",
          "all": "100.7"
        }
      }
    }
  }
}

games_home = example_data["response"]["games"]["played"]["home"]
games_away = example_data["response"]["games"]["played"]["away"]
games_all = example_data["response"]["games"]["played"]["all"]

won_home = example_data["response"]["games"]["wins"]["home"]["total"]
won_away = example_data["response"]["games"]["wins"]["away"]["total"]
won_all = example_data["response"]["games"]["wins"]["all"]["total"]

lost_home = example_data["response"]["games"]["loses"]["home"]["total"]
lost_away = example_data["response"]["games"]["loses"]["away"]["total"]
lost_all = example_data["response"]["games"]["loses"]["all"]["total"]

points_for_home = example_data["response"]["points"]["for"]["total"]["home"]
points_for_away = example_data["response"]["points"]["for"]["total"]["away"]
points_for_all = example_data["response"]["points"]["for"]["total"]["all"]

points_against_home = example_data["response"]["points"]["against"]["total"]["home"]
points_against_away = example_data["response"]["points"]["against"]["total"]["away"]
points_against_all = example_data["response"]["points"]["against"]["total"]["all"]


ppg_for = example_data["response"]["points"]["for"]["average"]["all"]
ppg_against = example_data["response"]["points"]["against"]["average"]["all"]
team_name = example_data["response"]["team"]["name"]

print(f"{lost_home} home games lost, {lost_away} away games lost, {lost_all} total games lost")
print(f"{points_for_home} home game points for, {points_for_away} away game points for, {points_for_all} total points for")
print(f"{points_against_home} home game points against, {points_against_away} away game points against, {points_against_all} total points against")