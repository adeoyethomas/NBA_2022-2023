# Latest update
<ins>31st Jan 2024</ins>:
Since my last update there have been a few changes to the project, for starters I have decided to extract more data from the API than initially intended. At first, I only planned to store data on the Points Per Game (PPG) scored for and against a team, but then I looked into more of the endpoints available on the [RESTful API for basketball data](https://www.api-basketball.com/) API and discovered more useful data. So I have now created the following tables:

* Team info
* Games played
* Games won
* Games lost
* Points for
* Points against
* Game Results (*Still deciding on the best design for this table so that it's in a normalised form*)

More info on these tables in the [README.md](https://github.com/adeoyethomas/NBA_2022-2023/blob/main/README.md) file

### New Challenge
A challenge that has recently come up is that the API has stored data for the pre-season, regular season & the post-season games. This is a challenge because I plan to only work with regular season information for the time being because, during the regular season, all teams play 82 games, making any analysis done on one team more comparable to another team.

### Possible solution
Using the *games* endpoint of the API and the *datetime* library on Python, I will create a function using conditional statements to categorise the games played as pre, regular or post-season games. Then for the games that are outside the range of the regular season dates (October 18, 2022, to April 9, 2023) I will remove the Points for, points against, win or loss, for those games from the DataFrames/tables. I will know the solution works if the sum of a team's wins and loses equal 82, and the first and last regular season game recorded is the same on a reputable website (ESPN, NBA etc.).

# Updates
<ins>8th Aug 2023</ins>:
The plan is to collate and store data from the 2022-2023 season such as a team's regular season finish position, Points Per Game (PPG) conceded & PPG scored using this [RESTful API for basketball data](https://www.api-basketball.com/). I will use Google Cloud Platform to store the data (most likely using a bucket on cloud storage) and then use UDF to transfer the data to BigQuery where I will do some analysis, and then produce some visualizations using Tableau or PowerBi.

<ins>15th Dec 2023</ins>:
It has been a while since I have worked on this project, but I am motivated to develop my skills as a data specialist, and I believe working on this project is the best way to get me there. I decided not to use MySQL for this project any more instead, I will use a Pandas DataFrame to organise the scraped data and then will upload the DataFrame to a bucket on Cloud Storage. This removes an extra storage process which would be costly for a large-scale project.

<ins>3rd Jan 2024</ins>:
Created a table using a DataFrame (DF) to store the team's name/API identifier/League Conference. This DataFrame can now be passed through the API to get the team's PPG for and against, which will then be stored in another DF.
