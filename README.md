# Election Analysis

## Project Overview
Here I will complete an election audit of a recent local congressional election held by the Colorado Board of Elections. Currently, the election audit contains the results for each candidate and the winner. However, to complete the audit, I will submit data containing county information. This includes the voter turnout for each county, the percentage of votes from each county (out of the total count), and the county with the highest turnout.

## Resources
[Data Source](https://github.com/AkifEltahir96/ElectionAnalysis/blob/main/Resources/election_results.csv)
Software: Python 3.8.7, Visual Studio Code

## Election-Audit Results
How many votes were cast in this congressional election?
  - 369,711 votes were cast in this congressional election (green rectangle). 

Provide a breakdown of the number of votes and the percentage of votes for each county and precinct (red rectangle).
  - The county of Jefferson reported 10.5% of the votes and 38,855 of total votes. 
  - The county of Denver reported 82.8% of the votes and 306,055 of total votes. 
  - The county of Arapahoe reported 6.7% of the votes and 24,801 of total votes.

Which county had the largest number of votes?
  - Devner had the largest number of votes (orange rectangle).
  
Provide a breakdown of the number of votes and the percentage of total votes each candidate recieved (yellow rectangle).
  - Charles Casper Stockham recieved 23.0% of the votes and 85,213 of total votes.
  - Diana DeGette recieved 73.8% of the votes and 272,892 of total votes.
  - Raymon Anthony Doane recieved 3.1% of the votes and 11,606 of total votes.

Which candidate won the election, what was their vote count, and what was their percentage of total votes?
  - Diana DeGette won the election with 73.8% of the votes and 272,892 total votes (blue rectangle).

![Total Votes](https://github.com/AkifEltahir96/ElectionAnalysis/blob/main/Resources/Election%20Results.png)
   
## Election-Audit Summary
For future elections, I have two suggestions on how this script can be modified to be used for other elections. First, I suggest organizing the code so that everything that is going to be written into the text file is all together. This will help centralize all of the information being written into the text file and will reduce the amount of code needed. Second, I would nest some of the for loops into one larger loop instead of having seperate for loops to extract the data in each section of the text file. Overall, I believe these modifications will reduce the amount of unnecessary code, reduce syntax errors, and make the code run more effciently.

