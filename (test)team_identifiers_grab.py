import json
import pandas as pd

# This is the output on the API call on the URL "https://v1.basketball.api-sports.io/standings?league=12&season=2022-2023"
standings='''{
    "get": "standings",
    "parameters": {
        "league": "12",
        "season": "2022-2023"
    },
    "errors": [],
    "results": 1,
    "response": [
        [
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/139.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 52,
                        "percentage": "0.642"
                    },
                    "lose": {
                        "total": 29,
                        "percentage": "0.358"
                    }
                },
                "points": {
                    "for": 9386,
                    "against": 9127
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 146,
                    "name": "Memphis Grizzlies",
                    "logo": "https://media-4.api-sports.io/basketball/teams/146.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 51,
                        "percentage": "0.630"
                    },
                    "lose": {
                        "total": 30,
                        "percentage": "0.370"
                    }
                },
                "points": {
                    "for": 9487,
                    "against": 9149
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 157,
                    "name": "Sacramento Kings",
                    "logo": "https://media-4.api-sports.io/basketball/teams/157.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 48,
                        "percentage": "0.593"
                    },
                    "lose": {
                        "total": 33,
                        "percentage": "0.407"
                    }
                },
                "points": {
                    "for": 9803,
                    "against": 9572
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media-4.api-sports.io/basketball/teams/155.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 45,
                        "percentage": "0.556"
                    },
                    "lose": {
                        "total": 36,
                        "percentage": "0.444"
                    }
                },
                "points": {
                    "for": 9205,
                    "against": 9030
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 141,
                    "name": "Golden State Warriors",
                    "logo": "https://media-4.api-sports.io/basketball/teams/141.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 43,
                        "percentage": "0.531"
                    },
                    "lose": {
                        "total": 38,
                        "percentage": "0.469"
                    }
                },
                "points": {
                    "for": 9596,
                    "against": 9504
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 6,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/144.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 43,
                        "percentage": "0.531"
                    },
                    "lose": {
                        "total": 38,
                        "percentage": "0.469"
                    }
                },
                "points": {
                    "for": 9195,
                    "against": 9159
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 7,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 150,
                    "name": "New Orleans Pelicans",
                    "logo": "https://media-4.api-sports.io/basketball/teams/150.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 42,
                        "percentage": "0.519"
                    },
                    "lose": {
                        "total": 39,
                        "percentage": "0.481"
                    }
                },
                "points": {
                    "for": 9270,
                    "against": 9110
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 8,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/145.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 42,
                        "percentage": "0.519"
                    },
                    "lose": {
                        "total": 39,
                        "percentage": "0.481"
                    }
                },
                "points": {
                    "for": 9480,
                    "against": 9444
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 9,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media-4.api-sports.io/basketball/teams/149.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 41,
                        "percentage": "0.506"
                    },
                    "lose": {
                        "total": 40,
                        "percentage": "0.494"
                    }
                },
                "points": {
                    "for": 9381,
                    "against": 9389
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 10,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media-4.api-sports.io/basketball/teams/152.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 39,
                        "percentage": "0.481"
                    },
                    "lose": {
                        "total": 42,
                        "percentage": "0.519"
                    }
                },
                "points": {
                    "for": 9518,
                    "against": 9444
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 11,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 138,
                    "name": "Dallas Mavericks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/138.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 38,
                        "percentage": "0.469"
                    },
                    "lose": {
                        "total": 43,
                        "percentage": "0.531"
                    }
                },
                "points": {
                    "for": 9249,
                    "against": 9222
                },
                "form": null,
                "description": null
            },
            {
                "position": 12,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 160,
                    "name": "Utah Jazz",
                    "logo": "https://media-4.api-sports.io/basketball/teams/160.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 37,
                        "percentage": "0.457"
                    },
                    "lose": {
                        "total": 44,
                        "percentage": "0.543"
                    }
                },
                "points": {
                    "for": 9483,
                    "against": 9549
                },
                "form": null,
                "description": null
            },
            {
                "position": 13,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 156,
                    "name": "Portland Trail Blazers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/156.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 33,
                        "percentage": "0.407"
                    },
                    "lose": {
                        "total": 48,
                        "percentage": "0.593"
                    }
                },
                "points": {
                    "for": 9198,
                    "against": 9471
                },
                "form": null,
                "description": null
            },
            {
                "position": 14,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 142,
                    "name": "Houston Rockets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/142.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 21,
                        "percentage": "0.259"
                    },
                    "lose": {
                        "total": 60,
                        "percentage": "0.741"
                    }
                },
                "points": {
                    "for": 8967,
                    "against": 9616
                },
                "form": null,
                "description": null
            },
            {
                "position": 15,
                "stage": "NBA",
                "group": {
                    "name": "Western Conference",
                    "points": 0
                },
                "team": {
                    "id": 158,
                    "name": "San Antonio Spurs",
                    "logo": "https://media-4.api-sports.io/basketball/teams/158.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 21,
                        "percentage": "0.259"
                    },
                    "lose": {
                        "total": 60,
                        "percentage": "0.741"
                    }
                },
                "points": {
                    "for": 9131,
                    "against": 9975
                },
                "form": null,
                "description": null
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 148,
                    "name": "Milwaukee Bucks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/148.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 82,
                    "win": {
                        "total": 58,
                        "percentage": "0.707"
                    },
                    "lose": {
                        "total": 24,
                        "percentage": "0.293"
                    }
                },
                "points": {
                    "for": 9589,
                    "against": 9291
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 133,
                    "name": "Boston Celtics",
                    "logo": "https://media-4.api-sports.io/basketball/teams/133.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 56,
                        "percentage": "0.691"
                    },
                    "lose": {
                        "total": 25,
                        "percentage": "0.309"
                    }
                },
                "points": {
                    "for": 9551,
                    "against": 9022
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 154,
                    "name": "Philadelphia 76ers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/154.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 53,
                        "percentage": "0.654"
                    },
                    "lose": {
                        "total": 28,
                        "percentage": "0.346"
                    }
                },
                "points": {
                    "for": 9314,
                    "against": 8989
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 137,
                    "name": "Cleveland Cavaliers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/137.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 51,
                        "percentage": "0.630"
                    },
                    "lose": {
                        "total": 30,
                        "percentage": "0.370"
                    }
                },
                "points": {
                    "for": 9110,
                    "against": 8658
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 151,
                    "name": "New York Knicks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/151.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 47,
                        "percentage": "0.580"
                    },
                    "lose": {
                        "total": 34,
                        "percentage": "0.420"
                    }
                },
                "points": {
                    "for": 9378,
                    "against": 9133
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 6,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 134,
                    "name": "Brooklyn Nets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/134.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 45,
                        "percentage": "0.556"
                    },
                    "lose": {
                        "total": 36,
                        "percentage": "0.444"
                    }
                },
                "points": {
                    "for": 9190,
                    "against": 9091
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 7,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media-4.api-sports.io/basketball/teams/147.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 43,
                        "percentage": "0.531"
                    },
                    "lose": {
                        "total": 38,
                        "percentage": "0.469"
                    }
                },
                "points": {
                    "for": 8854,
                    "against": 8893
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 8,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 132,
                    "name": "Atlanta Hawks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/132.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 41,
                        "percentage": "0.506"
                    },
                    "lose": {
                        "total": 40,
                        "percentage": "0.494"
                    }
                },
                "points": {
                    "for": 9597,
                    "against": 9567
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 9,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 159,
                    "name": "Toronto Raptors",
                    "logo": "https://media-4.api-sports.io/basketball/teams/159.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 82,
                    "win": {
                        "total": 41,
                        "percentage": "0.500"
                    },
                    "lose": {
                        "total": 41,
                        "percentage": "0.500"
                    }
                },
                "points": {
                    "for": 9254,
                    "against": 9133
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 10,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 136,
                    "name": "Chicago Bulls",
                    "logo": "https://media-4.api-sports.io/basketball/teams/136.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 39,
                        "percentage": "0.481"
                    },
                    "lose": {
                        "total": 42,
                        "percentage": "0.519"
                    }
                },
                "points": {
                    "for": 9173,
                    "against": 9089
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 11,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 161,
                    "name": "Washington Wizards",
                    "logo": "https://media-4.api-sports.io/basketball/teams/161.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 35,
                        "percentage": "0.432"
                    },
                    "lose": {
                        "total": 46,
                        "percentage": "0.568"
                    }
                },
                "points": {
                    "for": 9170,
                    "against": 9264
                },
                "form": null,
                "description": null
            },
            {
                "position": 12,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 153,
                    "name": "Orlando Magic",
                    "logo": "https://media-4.api-sports.io/basketball/teams/153.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 34,
                        "percentage": "0.420"
                    },
                    "lose": {
                        "total": 47,
                        "percentage": "0.580"
                    }
                },
                "points": {
                    "for": 9026,
                    "against": 9223
                },
                "form": null,
                "description": null
            },
            {
                "position": 13,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 143,
                    "name": "Indiana Pacers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/143.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 34,
                        "percentage": "0.420"
                    },
                    "lose": {
                        "total": 47,
                        "percentage": "0.580"
                    }
                },
                "points": {
                    "for": 9394,
                    "against": 9660
                },
                "form": null,
                "description": null
            },
            {
                "position": 14,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 135,
                    "name": "Charlotte Hornets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/135.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 26,
                        "percentage": "0.321"
                    },
                    "lose": {
                        "total": 55,
                        "percentage": "0.679"
                    }
                },
                "points": {
                    "for": 8992,
                    "against": 9515
                },
                "form": null,
                "description": null
            },
            {
                "position": 15,
                "stage": "NBA",
                "group": {
                    "name": "Eastern Conference",
                    "points": 0
                },
                "team": {
                    "id": 140,
                    "name": "Detroit Pistons",
                    "logo": "https://media-4.api-sports.io/basketball/teams/140.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 17,
                        "percentage": "0.210"
                    },
                    "lose": {
                        "total": 64,
                        "percentage": "0.790"
                    }
                },
                "points": {
                    "for": 8964,
                    "against": 9616
                },
                "form": null,
                "description": null
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Atlantic",
                    "points": 0
                },
                "team": {
                    "id": 133,
                    "name": "Boston Celtics",
                    "logo": "https://media-4.api-sports.io/basketball/teams/133.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 56,
                        "percentage": "0.691"
                    },
                    "lose": {
                        "total": 25,
                        "percentage": "0.309"
                    }
                },
                "points": {
                    "for": 9551,
                    "against": 9022
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Atlantic",
                    "points": 0
                },
                "team": {
                    "id": 154,
                    "name": "Philadelphia 76ers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/154.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 53,
                        "percentage": "0.654"
                    },
                    "lose": {
                        "total": 28,
                        "percentage": "0.346"
                    }
                },
                "points": {
                    "for": 9314,
                    "against": 8989
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Atlantic",
                    "points": 0
                },
                "team": {
                    "id": 151,
                    "name": "New York Knicks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/151.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 47,
                        "percentage": "0.580"
                    },
                    "lose": {
                        "total": 34,
                        "percentage": "0.420"
                    }
                },
                "points": {
                    "for": 9378,
                    "against": 9133
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Atlantic",
                    "points": 0
                },
                "team": {
                    "id": 134,
                    "name": "Brooklyn Nets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/134.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 45,
                        "percentage": "0.556"
                    },
                    "lose": {
                        "total": 36,
                        "percentage": "0.444"
                    }
                },
                "points": {
                    "for": 9190,
                    "against": 9091
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Atlantic",
                    "points": 0
                },
                "team": {
                    "id": 159,
                    "name": "Toronto Raptors",
                    "logo": "https://media-4.api-sports.io/basketball/teams/159.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 82,
                    "win": {
                        "total": 41,
                        "percentage": "0.500"
                    },
                    "lose": {
                        "total": 41,
                        "percentage": "0.500"
                    }
                },
                "points": {
                    "for": 9254,
                    "against": 9133
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Southeast",
                    "points": 0
                },
                "team": {
                    "id": 147,
                    "name": "Miami Heat",
                    "logo": "https://media-4.api-sports.io/basketball/teams/147.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 43,
                        "percentage": "0.531"
                    },
                    "lose": {
                        "total": 38,
                        "percentage": "0.469"
                    }
                },
                "points": {
                    "for": 8854,
                    "against": 8893
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Southeast",
                    "points": 0
                },
                "team": {
                    "id": 132,
                    "name": "Atlanta Hawks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/132.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 41,
                        "percentage": "0.506"
                    },
                    "lose": {
                        "total": 40,
                        "percentage": "0.494"
                    }
                },
                "points": {
                    "for": 9597,
                    "against": 9567
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Southeast",
                    "points": 0
                },
                "team": {
                    "id": 161,
                    "name": "Washington Wizards",
                    "logo": "https://media-4.api-sports.io/basketball/teams/161.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 35,
                        "percentage": "0.432"
                    },
                    "lose": {
                        "total": 46,
                        "percentage": "0.568"
                    }
                },
                "points": {
                    "for": 9170,
                    "against": 9264
                },
                "form": null,
                "description": null
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Southeast",
                    "points": 0
                },
                "team": {
                    "id": 153,
                    "name": "Orlando Magic",
                    "logo": "https://media-4.api-sports.io/basketball/teams/153.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 34,
                        "percentage": "0.420"
                    },
                    "lose": {
                        "total": 47,
                        "percentage": "0.580"
                    }
                },
                "points": {
                    "for": 9026,
                    "against": 9223
                },
                "form": null,
                "description": null
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Southeast",
                    "points": 0
                },
                "team": {
                    "id": 135,
                    "name": "Charlotte Hornets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/135.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 26,
                        "percentage": "0.321"
                    },
                    "lose": {
                        "total": 55,
                        "percentage": "0.679"
                    }
                },
                "points": {
                    "for": 8992,
                    "against": 9515
                },
                "form": null,
                "description": null
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Central",
                    "points": 0
                },
                "team": {
                    "id": 148,
                    "name": "Milwaukee Bucks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/148.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 82,
                    "win": {
                        "total": 58,
                        "percentage": "0.707"
                    },
                    "lose": {
                        "total": 24,
                        "percentage": "0.293"
                    }
                },
                "points": {
                    "for": 9589,
                    "against": 9291
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Central",
                    "points": 0
                },
                "team": {
                    "id": 137,
                    "name": "Cleveland Cavaliers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/137.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 51,
                        "percentage": "0.630"
                    },
                    "lose": {
                        "total": 30,
                        "percentage": "0.370"
                    }
                },
                "points": {
                    "for": 9110,
                    "against": 8658
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Central",
                    "points": 0
                },
                "team": {
                    "id": 136,
                    "name": "Chicago Bulls",
                    "logo": "https://media-4.api-sports.io/basketball/teams/136.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 39,
                        "percentage": "0.481"
                    },
                    "lose": {
                        "total": 42,
                        "percentage": "0.519"
                    }
                },
                "points": {
                    "for": 9173,
                    "against": 9089
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Central",
                    "points": 0
                },
                "team": {
                    "id": 143,
                    "name": "Indiana Pacers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/143.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 34,
                        "percentage": "0.420"
                    },
                    "lose": {
                        "total": 47,
                        "percentage": "0.580"
                    }
                },
                "points": {
                    "for": 9394,
                    "against": 9660
                },
                "form": null,
                "description": null
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Central",
                    "points": 0
                },
                "team": {
                    "id": 140,
                    "name": "Detroit Pistons",
                    "logo": "https://media-4.api-sports.io/basketball/teams/140.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 17,
                        "percentage": "0.210"
                    },
                    "lose": {
                        "total": 64,
                        "percentage": "0.790"
                    }
                },
                "points": {
                    "for": 8964,
                    "against": 9616
                },
                "form": null,
                "description": null
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Northwest",
                    "points": 0
                },
                "team": {
                    "id": 139,
                    "name": "Denver Nuggets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/139.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 52,
                        "percentage": "0.642"
                    },
                    "lose": {
                        "total": 29,
                        "percentage": "0.358"
                    }
                },
                "points": {
                    "for": 9386,
                    "against": 9127
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Northwest",
                    "points": 0
                },
                "team": {
                    "id": 149,
                    "name": "Minnesota Timberwolves",
                    "logo": "https://media-4.api-sports.io/basketball/teams/149.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 41,
                        "percentage": "0.506"
                    },
                    "lose": {
                        "total": 40,
                        "percentage": "0.494"
                    }
                },
                "points": {
                    "for": 9381,
                    "against": 9389
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Northwest",
                    "points": 0
                },
                "team": {
                    "id": 152,
                    "name": "Oklahoma City Thunder",
                    "logo": "https://media-4.api-sports.io/basketball/teams/152.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 39,
                        "percentage": "0.481"
                    },
                    "lose": {
                        "total": 42,
                        "percentage": "0.519"
                    }
                },
                "points": {
                    "for": 9518,
                    "against": 9444
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Northwest",
                    "points": 0
                },
                "team": {
                    "id": 160,
                    "name": "Utah Jazz",
                    "logo": "https://media-4.api-sports.io/basketball/teams/160.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 37,
                        "percentage": "0.457"
                    },
                    "lose": {
                        "total": 44,
                        "percentage": "0.543"
                    }
                },
                "points": {
                    "for": 9483,
                    "against": 9549
                },
                "form": null,
                "description": null
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Northwest",
                    "points": 0
                },
                "team": {
                    "id": 156,
                    "name": "Portland Trail Blazers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/156.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 33,
                        "percentage": "0.407"
                    },
                    "lose": {
                        "total": 48,
                        "percentage": "0.593"
                    }
                },
                "points": {
                    "for": 9198,
                    "against": 9471
                },
                "form": null,
                "description": null
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Pacific",
                    "points": 0
                },
                "team": {
                    "id": 157,
                    "name": "Sacramento Kings",
                    "logo": "https://media-4.api-sports.io/basketball/teams/157.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 48,
                        "percentage": "0.593"
                    },
                    "lose": {
                        "total": 33,
                        "percentage": "0.407"
                    }
                },
                "points": {
                    "for": 9803,
                    "against": 9572
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Pacific",
                    "points": 0
                },
                "team": {
                    "id": 155,
                    "name": "Phoenix Suns",
                    "logo": "https://media-4.api-sports.io/basketball/teams/155.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 45,
                        "percentage": "0.556"
                    },
                    "lose": {
                        "total": 36,
                        "percentage": "0.444"
                    }
                },
                "points": {
                    "for": 9205,
                    "against": 9030
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Pacific",
                    "points": 0
                },
                "team": {
                    "id": 141,
                    "name": "Golden State Warriors",
                    "logo": "https://media-4.api-sports.io/basketball/teams/141.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 43,
                        "percentage": "0.531"
                    },
                    "lose": {
                        "total": 38,
                        "percentage": "0.469"
                    }
                },
                "points": {
                    "for": 9596,
                    "against": 9504
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Pacific",
                    "points": 0
                },
                "team": {
                    "id": 144,
                    "name": "Los Angeles Clippers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/144.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 43,
                        "percentage": "0.531"
                    },
                    "lose": {
                        "total": 38,
                        "percentage": "0.469"
                    }
                },
                "points": {
                    "for": 9195,
                    "against": 9159
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Pacific",
                    "points": 0
                },
                "team": {
                    "id": 145,
                    "name": "Los Angeles Lakers",
                    "logo": "https://media-4.api-sports.io/basketball/teams/145.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 42,
                        "percentage": "0.519"
                    },
                    "lose": {
                        "total": 39,
                        "percentage": "0.481"
                    }
                },
                "points": {
                    "for": 9480,
                    "against": 9444
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 1,
                "stage": "NBA",
                "group": {
                    "name": "Southwest",
                    "points": 0
                },
                "team": {
                    "id": 146,
                    "name": "Memphis Grizzlies",
                    "logo": "https://media-4.api-sports.io/basketball/teams/146.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 51,
                        "percentage": "0.630"
                    },
                    "lose": {
                        "total": 30,
                        "percentage": "0.370"
                    }
                },
                "points": {
                    "for": 9487,
                    "against": 9149
                },
                "form": null,
                "description": "Promotion - NBA (Play Offs: 1/8-finals)"
            },
            {
                "position": 2,
                "stage": "NBA",
                "group": {
                    "name": "Southwest",
                    "points": 0
                },
                "team": {
                    "id": 150,
                    "name": "New Orleans Pelicans",
                    "logo": "https://media-4.api-sports.io/basketball/teams/150.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 42,
                        "percentage": "0.519"
                    },
                    "lose": {
                        "total": 39,
                        "percentage": "0.481"
                    }
                },
                "points": {
                    "for": 9270,
                    "against": 9110
                },
                "form": null,
                "description": "Promotion - NBA (Promotion - Play Offs: )"
            },
            {
                "position": 3,
                "stage": "NBA",
                "group": {
                    "name": "Southwest",
                    "points": 0
                },
                "team": {
                    "id": 138,
                    "name": "Dallas Mavericks",
                    "logo": "https://media-4.api-sports.io/basketball/teams/138.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 38,
                        "percentage": "0.469"
                    },
                    "lose": {
                        "total": 43,
                        "percentage": "0.531"
                    }
                },
                "points": {
                    "for": 9249,
                    "against": 9222
                },
                "form": null,
                "description": null
            },
            {
                "position": 4,
                "stage": "NBA",
                "group": {
                    "name": "Southwest",
                    "points": 0
                },
                "team": {
                    "id": 142,
                    "name": "Houston Rockets",
                    "logo": "https://media-4.api-sports.io/basketball/teams/142.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 21,
                        "percentage": "0.259"
                    },
                    "lose": {
                        "total": 60,
                        "percentage": "0.741"
                    }
                },
                "points": {
                    "for": 8967,
                    "against": 9616
                },
                "form": null,
                "description": null
            },
            {
                "position": 5,
                "stage": "NBA",
                "group": {
                    "name": "Southwest",
                    "points": 0
                },
                "team": {
                    "id": 158,
                    "name": "San Antonio Spurs",
                    "logo": "https://media-4.api-sports.io/basketball/teams/158.png"
                },
                "league": {
                    "id": 12,
                    "name": "NBA",
                    "type": "League",
                    "season": "2022-2023",
                    "logo": "https://media-4.api-sports.io/basketball/leagues/12.png"
                },
                "country": {
                    "id": 5,
                    "name": "USA",
                    "code": "US",
                    "flag": "https://media-4.api-sports.io/flags/us.svg"
                },
                "games": {
                    "played": 81,
                    "win": {
                        "total": 21,
                        "percentage": "0.259"
                    },
                    "lose": {
                        "total": 60,
                        "percentage": "0.741"
                    }
                },
                "points": {
                    "for": 9131,
                    "against": 9975
                },
                "form": null,
                "description": null
            }
        ]
    ]
}'''

# Creating a DataFrame to store the team API ids
team_ids_df = pd.DataFrame(columns = ['Team', 'Team ID', 'Conference', 'Conference Position'])

#Loads the json data so nulls are converted to None
standings = json.loads(standings)

# This is the standings json response but reached into the level where teams are listed
team_lvl = standings['response'][0]

def team_id_df_creation(team_lvl):
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

team_ids_df = team_id_df_creation(team_lvl)
print(team_ids_df)

team_ids = []

for index, row in team_ids_df.iterrows():
    team_ids.append(row['Team ID'])

print(team_ids)

