import json
import datetime as dt
from datetime import datetime

# Used this file as a test to grab useful info from games API response
example_data = '''{
    "get": "games",
    "parameters": {
        "league": "12",
        "season": "2022-2023",
        "team": "139",
        "timezone": "America/New_York"
    },
    "errors": [],
    "results": 107,
    "response": [
        {
            "id": 330050,
            "date": "2022-10-03T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1664845200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media.api-sports.io/basketball/teams/152.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 21,
                    "quarter_2": 31,
                    "quarter_3": 30,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 101
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 21,
                    "quarter_3": 39,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 112
                }
            }
        },
        {
            "id": 326128,
            "date": "2022-10-07T20:00:00-04:00",
            "time": "20:00",
            "timestamp": 1665187200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 136,
                    "name": "Chicago Bulls",
                    "logo": "https://media.api-sports.io/basketball/teams/136.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 27,
                    "quarter_2": 45,
                    "quarter_3": 33,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 131
                },
                "away": {
                    "quarter_1": 26,
                    "quarter_2": 37,
                    "quarter_3": 25,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 330052,
            "date": "2022-10-10T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1665450000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 30,
                    "quarter_2": 24,
                    "quarter_3": 24,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 107
                },
                "away": {
                    "quarter_1": 35,
                    "quarter_2": 24,
                    "quarter_3": 22,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 105
                }
            }
        },
        {
            "id": 330053,
            "date": "2022-10-12T22:30:00-04:00",
            "time": "22:30",
            "timestamp": 1665628200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media.api-sports.io/basketball/teams/144.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 37,
                    "quarter_3": 34,
                    "quarter_4": 15,
                    "over_time": null,
                    "total": 115
                },
                "away": {
                    "quarter_1": 37,
                    "quarter_2": 37,
                    "quarter_3": 26,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 126
                }
            }
        },
        {
            "id": 326136,
            "date": "2022-10-14T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1665799200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 141,
                    "name": "Golden State Warriors",
                    "logo": "https://media.api-sports.io/basketball/teams/141.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 36,
                    "quarter_3": 20,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 112
                },
                "away": {
                    "quarter_1": 32,
                    "quarter_2": 24,
                    "quarter_3": 42,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 119
                }
            }
        },
        {
            "id": 326148,
            "date": "2022-10-19T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1666227600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 160,
                    "name": "Utah Jazz",
                    "logo": "https://media.api-sports.io/basketball/teams/160.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 37,
                    "quarter_2": 38,
                    "quarter_3": 19,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 123
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 23,
                    "quarter_3": 27,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 102
                }
            }
        },
        {
            "id": 326162,
            "date": "2022-10-21T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1666404000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 141,
                    "name": "Golden State Warriors",
                    "logo": "https://media.api-sports.io/basketball/teams/141.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 18,
                    "quarter_3": 36,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 123
                },
                "away": {
                    "quarter_1": 40,
                    "quarter_2": 30,
                    "quarter_3": 28,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 128
                }
            }
        },
        {
            "id": 326171,
            "date": "2022-10-22T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1666486800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media.api-sports.io/basketball/teams/152.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 27,
                    "quarter_3": 33,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 29,
                    "quarter_2": 26,
                    "quarter_3": 30,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 117
                }
            }
        },
        {
            "id": 326187,
            "date": "2022-10-24T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1666663200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 156,
                    "name": "Portland Trail Blazers",
                    "logo": "https://media.api-sports.io/basketball/teams/156.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 23,
                    "quarter_2": 32,
                    "quarter_3": 44,
                    "quarter_4": 36,
                    "over_time": null,
                    "total": 135
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 30,
                    "quarter_3": 25,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 326200,
            "date": "2022-10-26T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1666836000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 28,
                    "quarter_3": 32,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 110
                },
                "away": {
                    "quarter_1": 22,
                    "quarter_2": 32,
                    "quarter_3": 17,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 99
                }
            }
        },
        {
            "id": 326214,
            "date": "2022-10-28T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1667005200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 160,
                    "name": "Utah Jazz",
                    "logo": "https://media.api-sports.io/basketball/teams/160.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 35,
                    "quarter_2": 28,
                    "quarter_3": 26,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 117
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 25,
                    "quarter_3": 28,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 101
                }
            }
        },
        {
            "id": 326231,
            "date": "2022-10-30T21:30:00-04:00",
            "time": "21:30",
            "timestamp": 1667179800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 29,
                    "quarter_3": 38,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 121
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 20,
                    "quarter_3": 34,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 326255,
            "date": "2022-11-03T20:00:00-04:00",
            "time": "20:00",
            "timestamp": 1667520000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media.api-sports.io/basketball/teams/152.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 28,
                    "quarter_3": 38,
                    "quarter_4": 15,
                    "over_time": null,
                    "total": 110
                },
                "away": {
                    "quarter_1": 42,
                    "quarter_2": 29,
                    "quarter_3": 22,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 122
                }
            }
        },
        {
            "id": 326274,
            "date": "2022-11-05T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1667696400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 158,
                    "name": "San Antonio Spurs",
                    "logo": "https://media.api-sports.io/basketball/teams/158.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 40,
                    "quarter_2": 30,
                    "quarter_3": 29,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 126
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 24,
                    "quarter_3": 25,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 101
                }
            }
        },
        {
            "id": 326290,
            "date": "2022-11-07T21:30:00-05:00",
            "time": "21:30",
            "timestamp": 1667874600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 158,
                    "name": "San Antonio Spurs",
                    "logo": "https://media.api-sports.io/basketball/teams/158.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 34,
                    "quarter_3": 27,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 109
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 37,
                    "quarter_3": 29,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 115
                }
            }
        },
        {
            "id": 326296,
            "date": "2022-11-09T19:00:00-05:00",
            "time": "19:00",
            "timestamp": 1668038400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 143,
                    "name": "Indiana Pacers",
                    "logo": "https://media.api-sports.io/basketball/teams/143.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 27,
                    "quarter_2": 43,
                    "quarter_3": 25,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 119
                },
                "away": {
                    "quarter_1": 35,
                    "quarter_2": 21,
                    "quarter_3": 33,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 122
                }
            }
        },
        {
            "id": 326312,
            "date": "2022-11-11T19:00:00-05:00",
            "time": "19:00",
            "timestamp": 1668211200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 133,
                    "name": "Boston Celtics",
                    "logo": "https://media.api-sports.io/basketball/teams/133.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 33,
                    "quarter_2": 33,
                    "quarter_3": 31,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 131
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 32,
                    "quarter_3": 34,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 112
                }
            }
        },
        {
            "id": 326332,
            "date": "2022-11-13T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1668387600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 136,
                    "name": "Chicago Bulls",
                    "logo": "https://media.api-sports.io/basketball/teams/136.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 20,
                    "quarter_2": 27,
                    "quarter_3": 29,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 103
                },
                "away": {
                    "quarter_1": 32,
                    "quarter_2": 30,
                    "quarter_3": 35,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 126
                }
            }
        },
        {
            "id": 326355,
            "date": "2022-11-16T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1668654000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 151,
                    "name": "New York Knicks",
                    "logo": "https://media.api-sports.io/basketball/teams/151.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 27,
                    "quarter_2": 27,
                    "quarter_3": 30,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 103
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 25,
                    "quarter_3": 25,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 106
                }
            }
        },
        {
            "id": 326366,
            "date": "2022-11-18T20:30:00-05:00",
            "time": "20:30",
            "timestamp": 1668821400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 138,
                    "name": "Dallas Mavericks",
                    "logo": "https://media.api-sports.io/basketball/teams/138.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 44,
                    "quarter_3": 32,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 127
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 28,
                    "quarter_3": 28,
                    "quarter_4": 16,
                    "over_time": null,
                    "total": 99
                }
            }
        },
        {
            "id": 326382,
            "date": "2022-11-20T19:30:00-05:00",
            "time": "19:30",
            "timestamp": 1668990600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 138,
                    "name": "Dallas Mavericks",
                    "logo": "https://media.api-sports.io/basketball/teams/138.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 25,
                    "quarter_2": 31,
                    "quarter_3": 18,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 97
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 30,
                    "quarter_3": 24,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 98
                }
            }
        },
        {
            "id": 326394,
            "date": "2022-11-22T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1669168800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 140,
                    "name": "Detroit Pistons",
                    "logo": "https://media.api-sports.io/basketball/teams/140.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 28,
                    "quarter_3": 24,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 108
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 30,
                    "quarter_3": 25,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 326404,
            "date": "2022-11-23T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1669251600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "After Over Time",
                "short": "AOT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media.api-sports.io/basketball/teams/152.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 21,
                    "quarter_2": 42,
                    "quarter_3": 34,
                    "quarter_4": 23,
                    "over_time": 6,
                    "total": 126
                },
                "away": {
                    "quarter_1": 38,
                    "quarter_2": 31,
                    "quarter_3": 15,
                    "quarter_4": 36,
                    "over_time": 11,
                    "total": 131
                }
            }
        },
        {
            "id": 326421,
            "date": "2022-11-25T22:30:00-05:00",
            "time": "22:30",
            "timestamp": 1669433400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media.api-sports.io/basketball/teams/144.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 26,
                    "quarter_3": 25,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 104
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 33,
                    "quarter_3": 23,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 114
                }
            }
        },
        {
            "id": 326441,
            "date": "2022-11-28T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1669687200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 142,
                    "name": "Houston Rockets",
                    "logo": "https://media.api-sports.io/basketball/teams/142.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 42,
                    "quarter_2": 28,
                    "quarter_3": 36,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 129
                },
                "away": {
                    "quarter_1": 39,
                    "quarter_2": 29,
                    "quarter_3": 23,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 326458,
            "date": "2022-11-30T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1669860000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 142,
                    "name": "Houston Rockets",
                    "logo": "https://media.api-sports.io/basketball/teams/142.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 44,
                    "quarter_2": 30,
                    "quarter_3": 22,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 120
                },
                "away": {
                    "quarter_1": 24,
                    "quarter_2": 23,
                    "quarter_3": 25,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 100
                }
            }
        },
        {
            "id": 326467,
            "date": "2022-12-02T19:30:00-05:00",
            "time": "19:30",
            "timestamp": 1670027400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 132,
                    "name": "Atlanta Hawks",
                    "logo": "https://media.api-sports.io/basketball/teams/132.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 32,
                    "quarter_3": 30,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 117
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 21,
                    "quarter_3": 35,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 109
                }
            }
        },
        {
            "id": 326480,
            "date": "2022-12-04T15:30:00-05:00",
            "time": "15:30",
            "timestamp": 1670185800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 150,
                    "name": "New Orleans Pelicans",
                    "logo": "https://media.api-sports.io/basketball/teams/150.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 27,
                    "quarter_2": 32,
                    "quarter_3": 28,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 121
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 29,
                    "quarter_3": 21,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 106
                }
            }
        },
        {
            "id": 326498,
            "date": "2022-12-06T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1670382000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 138,
                    "name": "Dallas Mavericks",
                    "logo": "https://media.api-sports.io/basketball/teams/138.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 29,
                    "quarter_3": 28,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 115
                },
                "away": {
                    "quarter_1": 36,
                    "quarter_2": 28,
                    "quarter_3": 27,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 116
                }
            }
        },
        {
            "id": 326512,
            "date": "2022-12-08T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1670554800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 156,
                    "name": "Portland Trail Blazers",
                    "logo": "https://media.api-sports.io/basketball/teams/156.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 36,
                    "quarter_2": 28,
                    "quarter_3": 35,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 120
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 33,
                    "quarter_3": 26,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 121
                }
            }
        },
        {
            "id": 326529,
            "date": "2022-12-10T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1670724000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 160,
                    "name": "Utah Jazz",
                    "logo": "https://media.api-sports.io/basketball/teams/160.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 33,
                    "quarter_3": 31,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 115
                },
                "away": {
                    "quarter_1": 26,
                    "quarter_2": 26,
                    "quarter_3": 38,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 326558,
            "date": "2022-12-14T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1671069600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 161,
                    "name": "Washington Wizards",
                    "logo": "https://media.api-sports.io/basketball/teams/161.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 38,
                    "quarter_2": 34,
                    "quarter_3": 30,
                    "quarter_4": 39,
                    "over_time": null,
                    "total": 141
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 36,
                    "quarter_3": 28,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 128
                }
            }
        },
        {
            "id": 326573,
            "date": "2022-12-16T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1671246000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 33,
                    "quarter_2": 31,
                    "quarter_3": 29,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 126
                },
                "away": {
                    "quarter_1": 32,
                    "quarter_2": 33,
                    "quarter_3": 23,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 108
                }
            }
        },
        {
            "id": 326586,
            "date": "2022-12-18T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1671411600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 135,
                    "name": "Charlotte Hornets",
                    "logo": "https://media.api-sports.io/basketball/teams/135.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 20,
                    "quarter_2": 35,
                    "quarter_3": 39,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 119
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 27,
                    "quarter_3": 28,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 115
                }
            }
        },
        {
            "id": 326601,
            "date": "2022-12-20T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1671591600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 146,
                    "name": "Memphis Grizzlies",
                    "logo": "https://media.api-sports.io/basketball/teams/146.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 35,
                    "quarter_2": 20,
                    "quarter_3": 29,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 105
                },
                "away": {
                    "quarter_1": 14,
                    "quarter_2": 26,
                    "quarter_3": 31,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 91
                }
            }
        },
        {
            "id": 326625,
            "date": "2022-12-23T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1671847200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 156,
                    "name": "Portland Trail Blazers",
                    "logo": "https://media.api-sports.io/basketball/teams/156.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 26,
                    "quarter_3": 35,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 120
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 37,
                    "quarter_3": 16,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 107
                }
            }
        },
        {
            "id": 326633,
            "date": "2022-12-25T22:30:00-05:00",
            "time": "22:30",
            "timestamp": 1672025400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "After Over Time",
                "short": "AOT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 23,
                    "quarter_3": 30,
                    "quarter_4": 32,
                    "over_time": 15,
                    "total": 128
                },
                "away": {
                    "quarter_1": 24,
                    "quarter_2": 33,
                    "quarter_3": 27,
                    "quarter_4": 29,
                    "over_time": 12,
                    "total": 125
                }
            }
        },
        {
            "id": 326650,
            "date": "2022-12-27T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1672196400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 157,
                    "name": "Sacramento Kings",
                    "logo": "https://media.api-sports.io/basketball/teams/157.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 24,
                    "quarter_3": 27,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 106
                },
                "away": {
                    "quarter_1": 20,
                    "quarter_2": 27,
                    "quarter_3": 32,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 326658,
            "date": "2022-12-28T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1672282800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 157,
                    "name": "Sacramento Kings",
                    "logo": "https://media.api-sports.io/basketball/teams/157.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 24,
                    "quarter_2": 38,
                    "quarter_3": 32,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 127
                },
                "away": {
                    "quarter_1": 40,
                    "quarter_2": 35,
                    "quarter_3": 30,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 126
                }
            }
        },
        {
            "id": 326671,
            "date": "2022-12-30T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1672452000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 23,
                    "quarter_2": 37,
                    "quarter_3": 25,
                    "quarter_4": 39,
                    "over_time": null,
                    "total": 124
                },
                "away": {
                    "quarter_1": 19,
                    "quarter_2": 38,
                    "quarter_3": 33,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 119
                }
            }
        },
        {
            "id": 326683,
            "date": "2023-01-01T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1672621200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 133,
                    "name": "Boston Celtics",
                    "logo": "https://media.api-sports.io/basketball/teams/133.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 37,
                    "quarter_2": 25,
                    "quarter_3": 36,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 123
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 26,
                    "quarter_3": 31,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 111
                }
            }
        },
        {
            "id": 326692,
            "date": "2023-01-02T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1672707600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 23,
                    "quarter_2": 36,
                    "quarter_3": 31,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 124
                },
                "away": {
                    "quarter_1": 23,
                    "quarter_2": 30,
                    "quarter_3": 32,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 111
                }
            }
        },
        {
            "id": 326715,
            "date": "2023-01-05T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1672974000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media.api-sports.io/basketball/teams/144.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 34,
                    "quarter_3": 36,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 15,
                    "quarter_2": 17,
                    "quarter_3": 27,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 91
                }
            }
        },
        {
            "id": 326723,
            "date": "2023-01-06T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1673056800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 137,
                    "name": "Cleveland Cavaliers",
                    "logo": "https://media.api-sports.io/basketball/teams/137.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 36,
                    "quarter_3": 32,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 121
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 30,
                    "quarter_3": 24,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 108
                }
            }
        },
        {
            "id": 326745,
            "date": "2023-01-09T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1673316000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 33,
                    "quarter_3": 32,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 23,
                    "quarter_2": 25,
                    "quarter_3": 31,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 109
                }
            }
        },
        {
            "id": 326760,
            "date": "2023-01-11T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1673492400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 36,
                    "quarter_3": 30,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 126
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 26,
                    "quarter_3": 21,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 97
                }
            }
        },
        {
            "id": 326775,
            "date": "2023-01-13T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1673665200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media.api-sports.io/basketball/teams/144.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 24,
                    "quarter_3": 23,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 103
                },
                "away": {
                    "quarter_1": 32,
                    "quarter_2": 25,
                    "quarter_3": 29,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 115
                }
            }
        },
        {
            "id": 326789,
            "date": "2023-01-15T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1673830800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 153,
                    "name": "Orlando Magic",
                    "logo": "https://media.api-sports.io/basketball/teams/153.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 31,
                    "quarter_2": 38,
                    "quarter_3": 25,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 119
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 29,
                    "quarter_3": 34,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 116
                }
            }
        },
        {
            "id": 326803,
            "date": "2023-01-17T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1674007200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 156,
                    "name": "Portland Trail Blazers",
                    "logo": "https://media.api-sports.io/basketball/teams/156.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 39,
                    "quarter_3": 28,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 36,
                    "quarter_3": 22,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 326812,
            "date": "2023-01-18T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1674097200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 30,
                    "quarter_2": 25,
                    "quarter_3": 33,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 33,
                    "quarter_3": 35,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 118
                }
            }
        },
        {
            "id": 326824,
            "date": "2023-01-20T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1674266400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 143,
                    "name": "Indiana Pacers",
                    "logo": "https://media.api-sports.io/basketball/teams/143.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 37,
                    "quarter_2": 24,
                    "quarter_3": 38,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 134
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 25,
                    "quarter_3": 29,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 111
                }
            }
        },
        {
            "id": 326839,
            "date": "2023-01-22T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1674435600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media.api-sports.io/basketball/teams/152.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 18,
                    "quarter_2": 29,
                    "quarter_3": 27,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 99
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 25,
                    "quarter_3": 29,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 101
                }
            }
        },
        {
            "id": 326852,
            "date": "2023-01-24T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1674608400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 150,
                    "name": "New Orleans Pelicans",
                    "logo": "https://media.api-sports.io/basketball/teams/150.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 24,
                    "quarter_2": 23,
                    "quarter_3": 27,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 98
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 35,
                    "quarter_3": 20,
                    "quarter_4": 16,
                    "over_time": null,
                    "total": 99
                }
            }
        },
        {
            "id": 326859,
            "date": "2023-01-25T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1674694800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 148,
                    "name": "Milwaukee Bucks",
                    "logo": "https://media.api-sports.io/basketball/teams/148.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 32,
                    "quarter_3": 23,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 107
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 26,
                    "quarter_3": 20,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 99
                }
            }
        },
        {
            "id": 326877,
            "date": "2023-01-28T15:00:00-05:00",
            "time": "15:00",
            "timestamp": 1674936000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 154,
                    "name": "Philadelphia 76ers",
                    "logo": "https://media.api-sports.io/basketball/teams/154.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 29,
                    "quarter_3": 38,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 126
                },
                "away": {
                    "quarter_1": 38,
                    "quarter_2": 35,
                    "quarter_3": 26,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 119
                }
            }
        },
        {
            "id": 326904,
            "date": "2023-01-31T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1675220400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 150,
                    "name": "New Orleans Pelicans",
                    "logo": "https://media.api-sports.io/basketball/teams/150.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 31,
                    "quarter_2": 26,
                    "quarter_3": 36,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 35,
                    "quarter_2": 25,
                    "quarter_3": 24,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 326919,
            "date": "2023-02-02T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1675389600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 141,
                    "name": "Golden State Warriors",
                    "logo": "https://media.api-sports.io/basketball/teams/141.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 36,
                    "quarter_3": 35,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 134
                },
                "away": {
                    "quarter_1": 35,
                    "quarter_2": 34,
                    "quarter_3": 22,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 117
                }
            }
        },
        {
            "id": 326937,
            "date": "2023-02-04T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1675562400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 132,
                    "name": "Atlanta Hawks",
                    "logo": "https://media.api-sports.io/basketball/teams/132.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 35,
                    "quarter_2": 35,
                    "quarter_3": 27,
                    "quarter_4": 31,
                    "over_time": null,
                    "total": 128
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 22,
                    "quarter_3": 34,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 108
                }
            }
        },
        {
            "id": 326942,
            "date": "2023-02-05T19:00:00-05:00",
            "time": "19:00",
            "timestamp": 1675641600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 31,
                    "quarter_3": 31,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 128
                },
                "away": {
                    "quarter_1": 21,
                    "quarter_2": 22,
                    "quarter_3": 28,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 98
                }
            }
        },
        {
            "id": 326956,
            "date": "2023-02-07T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1675821600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 49,
                    "quarter_2": 30,
                    "quarter_3": 31,
                    "quarter_4": 36,
                    "over_time": null,
                    "total": 146
                },
                "away": {
                    "quarter_1": 19,
                    "quarter_2": 29,
                    "quarter_3": 27,
                    "quarter_4": 37,
                    "over_time": null,
                    "total": 112
                }
            }
        },
        {
            "id": 326967,
            "date": "2023-02-09T19:00:00-05:00",
            "time": "19:00",
            "timestamp": 1675987200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 153,
                    "name": "Orlando Magic",
                    "logo": "https://media.api-sports.io/basketball/teams/153.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 36,
                    "quarter_3": 24,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 115
                },
                "away": {
                    "quarter_1": 26,
                    "quarter_2": 29,
                    "quarter_3": 29,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 104
                }
            }
        },
        {
            "id": 326983,
            "date": "2023-02-11T19:00:00-05:00",
            "time": "19:00",
            "timestamp": 1676160000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 135,
                    "name": "Charlotte Hornets",
                    "logo": "https://media.api-sports.io/basketball/teams/135.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 26,
                    "quarter_3": 23,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 105
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 30,
                    "quarter_3": 37,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 119
                }
            }
        },
        {
            "id": 326998,
            "date": "2023-02-13T19:30:00-05:00",
            "time": "19:30",
            "timestamp": 1676334600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 36,
                    "quarter_2": 26,
                    "quarter_3": 21,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 108
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 38,
                    "quarter_3": 24,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 112
                }
            }
        },
        {
            "id": 327017,
            "date": "2023-02-15T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1676512800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 138,
                    "name": "Dallas Mavericks",
                    "logo": "https://media.api-sports.io/basketball/teams/138.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 35,
                    "quarter_3": 31,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 118
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 19,
                    "quarter_3": 30,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 109
                }
            }
        },
        {
            "id": 327022,
            "date": "2023-02-23T19:00:00-05:00",
            "time": "19:00",
            "timestamp": 1677196800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 137,
                    "name": "Cleveland Cavaliers",
                    "logo": "https://media.api-sports.io/basketball/teams/137.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 31,
                    "quarter_3": 34,
                    "quarter_4": 18,
                    "over_time": null,
                    "total": 109
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 25,
                    "quarter_3": 33,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 115
                }
            }
        },
        {
            "id": 327043,
            "date": "2023-02-25T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1677373200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 146,
                    "name": "Memphis Grizzlies",
                    "logo": "https://media.api-sports.io/basketball/teams/146.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 38,
                    "quarter_3": 28,
                    "quarter_4": 18,
                    "over_time": null,
                    "total": 112
                },
                "away": {
                    "quarter_1": 20,
                    "quarter_2": 22,
                    "quarter_3": 20,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 94
                }
            }
        },
        {
            "id": 327054,
            "date": "2023-02-26T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1677466800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "After Over Time",
                "short": "AOT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media.api-sports.io/basketball/teams/144.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 35,
                    "quarter_2": 31,
                    "quarter_3": 31,
                    "quarter_4": 23,
                    "over_time": 14,
                    "total": 134
                },
                "away": {
                    "quarter_1": 22,
                    "quarter_2": 36,
                    "quarter_3": 30,
                    "quarter_4": 32,
                    "over_time": 4,
                    "total": 124
                }
            }
        },
        {
            "id": 327062,
            "date": "2023-02-28T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1677632400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 142,
                    "name": "Houston Rockets",
                    "logo": "https://media.api-sports.io/basketball/teams/142.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 30,
                    "quarter_2": 24,
                    "quarter_3": 30,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 112
                },
                "away": {
                    "quarter_1": 41,
                    "quarter_2": 33,
                    "quarter_3": 32,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 133
                }
            }
        },
        {
            "id": 327090,
            "date": "2023-03-03T22:00:00-05:00",
            "time": "22:00",
            "timestamp": 1677898800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 146,
                    "name": "Memphis Grizzlies",
                    "logo": "https://media.api-sports.io/basketball/teams/146.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 22,
                    "quarter_3": 30,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 113
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 31,
                    "quarter_3": 22,
                    "quarter_4": 17,
                    "over_time": null,
                    "total": 97
                }
            }
        },
        {
            "id": 327111,
            "date": "2023-03-06T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1678154400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 159,
                    "name": "Toronto Raptors",
                    "logo": "https://media.api-sports.io/basketball/teams/159.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 29,
                    "quarter_3": 25,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 118
                },
                "away": {
                    "quarter_1": 34,
                    "quarter_2": 27,
                    "quarter_3": 27,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 327125,
            "date": "2023-03-08T21:00:00-05:00",
            "time": "21:00",
            "timestamp": 1678327200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 136,
                    "name": "Chicago Bulls",
                    "logo": "https://media.api-sports.io/basketball/teams/136.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 23,
                    "quarter_3": 24,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 96
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 26,
                    "quarter_3": 36,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 117
                }
            }
        },
        {
            "id": 327136,
            "date": "2023-03-10T20:00:00-05:00",
            "time": "20:00",
            "timestamp": 1678496400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 158,
                    "name": "San Antonio Spurs",
                    "logo": "https://media.api-sports.io/basketball/teams/158.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 42,
                    "quarter_3": 30,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 128
                },
                "away": {
                    "quarter_1": 38,
                    "quarter_2": 29,
                    "quarter_3": 26,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 120
                }
            }
        },
        {
            "id": 327150,
            "date": "2023-03-12T15:30:00-04:00",
            "time": "15:30",
            "timestamp": 1678649400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 134,
                    "name": "Brooklyn Nets",
                    "logo": "https://media.api-sports.io/basketball/teams/134.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 30,
                    "quarter_2": 39,
                    "quarter_3": 18,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 120
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 31,
                    "quarter_3": 37,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 122
                }
            }
        },
        {
            "id": 327165,
            "date": "2023-03-14T19:30:00-04:00",
            "time": "19:30",
            "timestamp": 1678836600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 159,
                    "name": "Toronto Raptors",
                    "logo": "https://media.api-sports.io/basketball/teams/159.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 49,
                    "quarter_2": 23,
                    "quarter_3": 26,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 125
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 26,
                    "quarter_3": 36,
                    "quarter_4": 18,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 327178,
            "date": "2023-03-16T19:00:00-04:00",
            "time": "19:00",
            "timestamp": 1679007600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 140,
                    "name": "Detroit Pistons",
                    "logo": "https://media.api-sports.io/basketball/teams/140.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 36,
                    "quarter_3": 22,
                    "quarter_4": 14,
                    "over_time": null,
                    "total": 100
                },
                "away": {
                    "quarter_1": 29,
                    "quarter_2": 29,
                    "quarter_3": 28,
                    "quarter_4": 33,
                    "over_time": null,
                    "total": 119
                }
            }
        },
        {
            "id": 327191,
            "date": "2023-03-18T13:00:00-04:00",
            "time": "13:00",
            "timestamp": 1679158800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 151,
                    "name": "New York Knicks",
                    "logo": "https://media.api-sports.io/basketball/teams/151.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 36,
                    "quarter_2": 26,
                    "quarter_3": 29,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 116
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 39,
                    "quarter_3": 24,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 327199,
            "date": "2023-03-19T15:30:00-04:00",
            "time": "15:30",
            "timestamp": 1679254200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 134,
                    "name": "Brooklyn Nets",
                    "logo": "https://media.api-sports.io/basketball/teams/134.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 21,
                    "quarter_2": 27,
                    "quarter_3": 23,
                    "quarter_4": 31,
                    "over_time": null,
                    "total": 102
                },
                "away": {
                    "quarter_1": 33,
                    "quarter_2": 30,
                    "quarter_3": 28,
                    "quarter_4": 17,
                    "over_time": null,
                    "total": 108
                }
            }
        },
        {
            "id": 327219,
            "date": "2023-03-22T19:00:00-04:00",
            "time": "19:00",
            "timestamp": 1679526000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 161,
                    "name": "Washington Wizards",
                    "logo": "https://media.api-sports.io/basketball/teams/161.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 28,
                    "quarter_3": 16,
                    "quarter_4": 31,
                    "over_time": null,
                    "total": 104
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 24,
                    "quarter_3": 39,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 118
                }
            }
        },
        {
            "id": 327245,
            "date": "2023-03-25T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1679792400,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 148,
                    "name": "Milwaukee Bucks",
                    "logo": "https://media.api-sports.io/basketball/teams/148.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 37,
                    "quarter_2": 26,
                    "quarter_3": 34,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 129
                },
                "away": {
                    "quarter_1": 38,
                    "quarter_2": 28,
                    "quarter_3": 19,
                    "quarter_4": 21,
                    "over_time": null,
                    "total": 106
                }
            }
        },
        {
            "id": 327262,
            "date": "2023-03-27T21:30:00-04:00",
            "time": "21:30",
            "timestamp": 1679967000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 154,
                    "name": "Philadelphia 76ers",
                    "logo": "https://media.api-sports.io/basketball/teams/154.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 25,
                    "quarter_2": 36,
                    "quarter_3": 30,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 116
                },
                "away": {
                    "quarter_1": 18,
                    "quarter_2": 39,
                    "quarter_3": 20,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 111
                }
            }
        },
        {
            "id": 327283,
            "date": "2023-03-30T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1680228000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 150,
                    "name": "New Orleans Pelicans",
                    "logo": "https://media.api-sports.io/basketball/teams/150.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 17,
                    "quarter_2": 23,
                    "quarter_3": 30,
                    "quarter_4": 18,
                    "over_time": null,
                    "total": 88
                },
                "away": {
                    "quarter_1": 21,
                    "quarter_2": 29,
                    "quarter_3": 32,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 107
                }
            }
        },
        {
            "id": 327296,
            "date": "2023-03-31T22:30:00-04:00",
            "time": "22:30",
            "timestamp": 1680316200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 28,
                    "quarter_3": 24,
                    "quarter_4": 16,
                    "over_time": null,
                    "total": 100
                },
                "away": {
                    "quarter_1": 20,
                    "quarter_2": 20,
                    "quarter_3": 34,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 93
                }
            }
        },
        {
            "id": 327311,
            "date": "2023-04-02T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1680481800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 141,
                    "name": "Golden State Warriors",
                    "logo": "https://media.api-sports.io/basketball/teams/141.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 32,
                    "quarter_3": 31,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 112
                },
                "away": {
                    "quarter_1": 36,
                    "quarter_2": 25,
                    "quarter_3": 26,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 110
                }
            }
        },
        {
            "id": 327318,
            "date": "2023-04-04T20:00:00-04:00",
            "time": "20:00",
            "timestamp": 1680652800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 142,
                    "name": "Houston Rockets",
                    "logo": "https://media.api-sports.io/basketball/teams/142.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 31,
                    "quarter_2": 25,
                    "quarter_3": 30,
                    "quarter_4": 38,
                    "over_time": null,
                    "total": 124
                },
                "away": {
                    "quarter_1": 30,
                    "quarter_2": 29,
                    "quarter_3": 26,
                    "quarter_4": 18,
                    "over_time": null,
                    "total": 103
                }
            }
        },
        {
            "id": 327337,
            "date": "2023-04-06T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1680832800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 27,
                    "quarter_2": 29,
                    "quarter_3": 33,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 119
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 30,
                    "quarter_3": 31,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 115
                }
            }
        },
        {
            "id": 327349,
            "date": "2023-04-08T15:30:00-04:00",
            "time": "15:30",
            "timestamp": 1680982200,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 160,
                    "name": "Utah Jazz",
                    "logo": "https://media.api-sports.io/basketball/teams/160.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 26,
                    "quarter_3": 31,
                    "quarter_4": 29,
                    "over_time": null,
                    "total": 118
                },
                "away": {
                    "quarter_1": 19,
                    "quarter_2": 36,
                    "quarter_3": 40,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 114
                }
            }
        },
        {
            "id": 327361,
            "date": "2023-04-09T15:30:00-04:00",
            "time": "15:30",
            "timestamp": 1681068600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 157,
                    "name": "Sacramento Kings",
                    "logo": "https://media.api-sports.io/basketball/teams/157.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 33,
                    "quarter_3": 24,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 109
                },
                "away": {
                    "quarter_1": 43,
                    "quarter_2": 24,
                    "quarter_3": 14,
                    "quarter_4": 14,
                    "over_time": null,
                    "total": 95
                }
            }
        },
        {
            "id": 348159,
            "date": "2023-04-16T22:30:00-04:00",
            "time": "22:30",
            "timestamp": 1681698600,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 29,
                    "quarter_3": 32,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 109
                },
                "away": {
                    "quarter_1": 23,
                    "quarter_2": 21,
                    "quarter_3": 14,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 80
                }
            }
        },
        {
            "id": 348161,
            "date": "2023-04-19T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1681956000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 31,
                    "quarter_2": 33,
                    "quarter_3": 23,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 122
                },
                "away": {
                    "quarter_1": 22,
                    "quarter_2": 27,
                    "quarter_3": 40,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 348162,
            "date": "2023-04-21T21:30:00-04:00",
            "time": "21:30",
            "timestamp": 1682127000,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 28,
                    "quarter_2": 27,
                    "quarter_3": 33,
                    "quarter_4": 23,
                    "over_time": null,
                    "total": 111
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 33,
                    "quarter_3": 33,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 120
                }
            }
        },
        {
            "id": 348164,
            "date": "2023-04-23T21:30:00-04:00",
            "time": "21:30",
            "timestamp": 1682299800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "After Over Time",
                "short": "AOT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 23,
                    "quarter_2": 25,
                    "quarter_3": 32,
                    "quarter_4": 16,
                    "over_time": 18,
                    "total": 114
                },
                "away": {
                    "quarter_1": 22,
                    "quarter_2": 30,
                    "quarter_3": 22,
                    "quarter_4": 22,
                    "over_time": 12,
                    "total": 108
                }
            }
        },
        {
            "id": 348774,
            "date": "2023-04-25T21:00:00-04:00",
            "time": "21:00",
            "timestamp": 1682470800,
            "timezone": "America/New_York",
            "stage": null,
            "week": null,
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media.api-sports.io/basketball/teams/149.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 22,
                    "quarter_2": 26,
                    "quarter_3": 29,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 112
                },
                "away": {
                    "quarter_1": 29,
                    "quarter_2": 18,
                    "quarter_3": 30,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 109
                }
            }
        },
        {
            "id": 348962,
            "date": "2023-04-29T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1682814600,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Quarter-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 31,
                    "quarter_2": 37,
                    "quarter_3": 26,
                    "quarter_4": 31,
                    "over_time": null,
                    "total": 125
                },
                "away": {
                    "quarter_1": 32,
                    "quarter_2": 19,
                    "quarter_3": 30,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 107
                }
            }
        },
        {
            "id": 348963,
            "date": "2023-05-01T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1682992800,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Quarter-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 18,
                    "quarter_2": 22,
                    "quarter_3": 30,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 97
                },
                "away": {
                    "quarter_1": 21,
                    "quarter_2": 21,
                    "quarter_3": 31,
                    "quarter_4": 14,
                    "over_time": null,
                    "total": 87
                }
            }
        },
        {
            "id": 348964,
            "date": "2023-05-05T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1683338400,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Quarter-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 38,
                    "quarter_3": 23,
                    "quarter_4": 31,
                    "over_time": null,
                    "total": 121
                },
                "away": {
                    "quarter_1": 31,
                    "quarter_2": 21,
                    "quarter_3": 36,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 114
                }
            }
        },
        {
            "id": 348965,
            "date": "2023-05-07T20:00:00-04:00",
            "time": "20:00",
            "timestamp": 1683504000,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Quarter-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 32,
                    "quarter_2": 31,
                    "quarter_3": 35,
                    "quarter_4": 31,
                    "over_time": null,
                    "total": 129
                },
                "away": {
                    "quarter_1": 34,
                    "quarter_2": 27,
                    "quarter_3": 31,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 124
                }
            }
        },
        {
            "id": 349526,
            "date": "2023-05-09T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1683684000,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Quarter-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 35,
                    "quarter_2": 17,
                    "quarter_3": 39,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 118
                },
                "away": {
                    "quarter_1": 24,
                    "quarter_2": 25,
                    "quarter_3": 25,
                    "quarter_4": 28,
                    "over_time": null,
                    "total": 102
                }
            }
        },
        {
            "id": 349545,
            "date": "2023-05-11T22:00:00-04:00",
            "time": "22:00",
            "timestamp": 1683856800,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Quarter-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media.api-sports.io/basketball/teams/155.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 26,
                    "quarter_2": 25,
                    "quarter_3": 25,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 100
                },
                "away": {
                    "quarter_1": 44,
                    "quarter_2": 37,
                    "quarter_3": 22,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 125
                }
            }
        },
        {
            "id": 349843,
            "date": "2023-05-16T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1684283400,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Semi-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 37,
                    "quarter_2": 35,
                    "quarter_3": 34,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 132
                },
                "away": {
                    "quarter_1": 25,
                    "quarter_2": 29,
                    "quarter_3": 38,
                    "quarter_4": 34,
                    "over_time": null,
                    "total": 126
                }
            }
        },
        {
            "id": 349844,
            "date": "2023-05-18T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1684456200,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Semi-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 27,
                    "quarter_2": 21,
                    "quarter_3": 28,
                    "quarter_4": 32,
                    "over_time": null,
                    "total": 108
                },
                "away": {
                    "quarter_1": 27,
                    "quarter_2": 26,
                    "quarter_3": 26,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 103
                }
            }
        },
        {
            "id": 349845,
            "date": "2023-05-20T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1684629000,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Semi-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 20,
                    "quarter_2": 35,
                    "quarter_3": 27,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 108
                },
                "away": {
                    "quarter_1": 32,
                    "quarter_2": 26,
                    "quarter_3": 26,
                    "quarter_4": 35,
                    "over_time": null,
                    "total": 119
                }
            }
        },
        {
            "id": 349846,
            "date": "2023-05-22T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1684801800,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Semi-finals",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media.api-sports.io/basketball/teams/145.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 34,
                    "quarter_2": 39,
                    "quarter_3": 16,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 111
                },
                "away": {
                    "quarter_1": 28,
                    "quarter_2": 30,
                    "quarter_3": 36,
                    "quarter_4": 19,
                    "over_time": null,
                    "total": 113
                }
            }
        },
        {
            "id": 350565,
            "date": "2023-06-01T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1685665800,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Final",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 29,
                    "quarter_2": 30,
                    "quarter_3": 25,
                    "quarter_4": 20,
                    "over_time": null,
                    "total": 104
                },
                "away": {
                    "quarter_1": 20,
                    "quarter_2": 22,
                    "quarter_3": 21,
                    "quarter_4": 30,
                    "over_time": null,
                    "total": 93
                }
            }
        },
        {
            "id": 350566,
            "date": "2023-06-04T20:00:00-04:00",
            "time": "20:00",
            "timestamp": 1685923200,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Final",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 23,
                    "quarter_2": 34,
                    "quarter_3": 26,
                    "quarter_4": 25,
                    "over_time": null,
                    "total": 108
                },
                "away": {
                    "quarter_1": 26,
                    "quarter_2": 25,
                    "quarter_3": 24,
                    "quarter_4": 36,
                    "over_time": null,
                    "total": 111
                }
            }
        },
        {
            "id": 350567,
            "date": "2023-06-07T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1686184200,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Final",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 24,
                    "quarter_2": 24,
                    "quarter_3": 20,
                    "quarter_4": 26,
                    "over_time": null,
                    "total": 94
                },
                "away": {
                    "quarter_1": 24,
                    "quarter_2": 29,
                    "quarter_3": 29,
                    "quarter_4": 27,
                    "over_time": null,
                    "total": 109
                }
            }
        },
        {
            "id": 350568,
            "date": "2023-06-09T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1686357000,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Final",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                },
                "away": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 21,
                    "quarter_2": 30,
                    "quarter_3": 22,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 95
                },
                "away": {
                    "quarter_1": 20,
                    "quarter_2": 35,
                    "quarter_3": 31,
                    "quarter_4": 22,
                    "over_time": null,
                    "total": 108
                }
            }
        },
        {
            "id": 351723,
            "date": "2023-06-12T20:30:00-04:00",
            "time": "20:30",
            "timestamp": 1686616200,
            "timezone": "America/New_York",
            "stage": null,
            "week": "NBA - Final",
            "status": {
                "long": "Game Finished",
                "short": "FT",
                "timer": null
            },
            "league": {
                "id": 12,
                "name": "NBA",
                "type": "League",
                "season": "2022-2023",
                "logo": "https://media.api-sports.io/basketball/leagues/12.png"
            },
            "country": {
                "id": 5,
                "name": "USA",
                "code": "US",
                "flag": "https://media.api-sports.io/flags/us.svg"
            },
            "teams": {
                "home": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media.api-sports.io/basketball/teams/139.png"
                },
                "away": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media.api-sports.io/basketball/teams/147.png"
                }
            },
            "scores": {
                "home": {
                    "quarter_1": 22,
                    "quarter_2": 22,
                    "quarter_3": 26,
                    "quarter_4": 24,
                    "over_time": null,
                    "total": 94
                },
                "away": {
                    "quarter_1": 24,
                    "quarter_2": 27,
                    "quarter_3": 20,
                    "quarter_4": 18,
                    "over_time": null,
                    "total": 89
                }
            }
        }
    ]
}'''

# converts the null's to None 
games = json.loads(example_data)

game_lvl = games['response']

# test = (datetime(3000, 1, 1))
# print(test)
# print(type(test))
# date = dt.datetime.fromisoformat(game_lvl['date']).date()
# print(date - datetime(2022, 10, 18).date())
# print(type(date))

def games_by_date(game_lvl):
    pre_season = 0
    reg_season = 0
    post_season = 0
    
    for game in game_lvl:
        if dt.datetime.fromisoformat(game['date']).date() < datetime(2022, 10, 18).date():
            pre_season += 1
        elif dt.datetime.fromisoformat(game['date']).date() >= datetime(2022, 10, 18).date() and dt.datetime.fromisoformat(game['date']).date() <= datetime(2023, 4, 9).date():
            reg_season += 1
        else:
            post_season += 1

      
    print(f"Pre-season: {pre_season}")
    print(f"Reg-season: {reg_season}")
    print(f"Post-season: {post_season}")
    print(f"Total: {pre_season + reg_season + post_season}")

# print(date)
# print(type(date))
            
    return None

games_by_date(game_lvl)



