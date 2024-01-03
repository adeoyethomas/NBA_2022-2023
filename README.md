# NBA 2022-2023 Season
A personal project looking at the NBA 2022-2023 regular season

## Task
This task is still a work in progress and the overall plan may change so I will keep this file up to date with any changes.

<ins>8th Aug 2023</ins>:
The plan is to collate and store data from the 2022-2023 season such as a team's regular season finish position, Points Per Game (PPG) conceded & PPG scored using this [RESTful API for basketball data](https://www.api-basketball.com/). I will use Google Cloud Platform to store the data (most likely using a bucket on cloud storage) and then use UDF to transfer the data to BigQuery where I will do some analysis, and then produce some visualizations using Tableau or PowerBi.

<ins>15th Dec 2023</ins>:
It has been a while since I have worked on this project but I am motivated to develop my skills as a data specialist and I believe working on this project is the best way to get me there. I decided to not use MySQL for this project anymore instead, I will use a Pandas DataFrame to organise the scraped data and then will upload the DataFrame to a bucket on Cloud Storage. This removes an extra storage process which would be costly for a large-scale project.


## Tech Stack (this may change)
* Python
* Visual Studio Code
* Google Cloud
* BigQuery
* Power Bi or Tableau
