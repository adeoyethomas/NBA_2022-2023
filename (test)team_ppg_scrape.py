# Used this file as a test to make sure that I grab the correct PPG information for a team
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

ppg_for = example_data["response"]["points"]["for"]["average"]["all"]
ppg_against = example_data["response"]["points"]["against"]["average"]["all"]
team_name = example_data["response"]["team"]["name"]

print("Team Name is: " + team_name)
print(team_name +" " + "scored " + str(ppg_for) + " ppg")
print(team_name + " " + "conceded " + str(ppg_against) + " ppg")