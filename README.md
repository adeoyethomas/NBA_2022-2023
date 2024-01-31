# NBA 2022-2023 Season
A project looking at the 2022-2023 NBA regular season. For a more personal read into my journey with the project read the [Project_Journal.md](https://github.com/adeoyethomas/NBA_2022-2023/blob/main/Project_Journal.md) file.

## Task
#### Target Data
The initial aim of the task was to extract, organise and store data for NBA teams from an API and analyse this data to see how it affected the teams finishing position during the regular season. The target data was going to be Points Per Game (PPG) scored for and against a team. The aim has developed since then.

There will now be 6 (potentially 7) DataFrames/tables created storing data from the API:

* Team info (Columns = Team name, Team ID, Team Conference)
* Games played (Columns = Team, Home Games Played, Away Games Played, Total Games Played)
* Games won (Columns = Team, Home Games Won, Away Games Won, Total Games Won)
* Games lost (Columns = Team, Home Games Lost, Away Games Lost, Total Games Lost)
* Points for (Columns = Team, Points For at Home, Points For Away, Total Points)
* Points against (Columns = Team, Points Against at Home, Points Against Away, Total Points)
* Game Results (*Still deciding on the best design for this table so that it's in a normalised form*)

Storing the information this way provides more possibilities when it comes to the analysing the data as opposed to just finding trends based a teams overall PPG we can now look into PPG home vs PPG away and how it affected a teams home and away record. Storing the data in this format is also beneficial because the stats for the games played can be truncated to only games played during the regular season, this way analysis of stats will be comparable from team to team becuase all teams play 82 games during the regular season.

## Tech Stack (this may change)
* Python
* Visual Studio Code
* Jupyter Notebook
* Google Cloud
* BigQuery & Snowflake (*Either of the tools can do the job but I will do the same thing using both for practice purposes*)
* Power Bi & Tableau (*Either of the tools can do the job but I will do the same thing using both for practice purposes*)
