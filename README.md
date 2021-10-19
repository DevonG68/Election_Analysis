# Election_Analysis
Election analysis (congressional) using Python and Visual Studio Code
Election Analysis
Election analysis (congressional) using Python and Visual Studio Code 

Background Info

Colorado Boards of Election, Tom, in election audit of tabulated results for US Congressional precinct in Colorado. Task in reporting total number of votes casts, total number of votes for each candidate, percentage of votes for each candidate, and winner of election based on popular vote. Tom’s manager wants to know if there is a way to automate process using python. Codes written will be used in helping audit senatorial districts and local elections in addition to other congressional elections. Analysis will take in account mail-in ballot (hand counted at central office), punch cards (collected and fed into machine that calculates total), and direct recording electronic (DRE) counting machines (memory cards from DRE machines are sent in by office and read by a computer. Goal is to generate a vote count report that certifies this USP congressional race. 


Project Overview

Colorado Board of Elections employee, tom, has given me the task to complete the election audit of a recent local congressional election by analyzing and obtaining the following:

1.	Calculate the total number of votes cast
2.	Get a complete list of candidates who received votes
3.	Calculate the total number of votes each candidate received
4.	Calculate the percentage of votes each candidate won
5.	Determine the winner of the election based on popular vote

Resources Used

	Data Source: election_results csv
	Software: Python 3.8.8, Visual Studio Code 1.60.2 (Universal), Git Hub

Summary of Project

•	The analysis of the election show that:
•	There were 369,711 total votes cast in the election.
•	The candidates included:
  o	Raymon Anthony Doane
  o	Diana DeGette
  o	Charles Casper Stockham
•	The candidate results were:
  o	Raymon Anthony Doane had 11,606 votes with percentage of 3.1%
  o	Diana DeGette had 272,892 votes with percentage of 73.8%
  o	Charles Casper Stockham had 85,213 votes with percentage of 23%
• The winner of the election was:
  o	Diana DeGetta who had 272,892 votes with percentage of 73.8%


Challenge Overview
Deliverable 1
  Step 1:
  •	Initialize a county list, like the candidate_options list, that will hold the names of the counties.
  •	Initialize a dictionary, like the candidate_votes dictionary, that will hold the county as the key and the votes cast for each county as the values.
    o	County_names = []
    o	County_votes = {}
Step 2:
  •	Initialize an empty string, like winning_candidate, that will hold the county name for the county with the largest turnout.
  •	Initialize a variable, like the winning_count variable, that will hold the number of votes of the county that had the largest turnout.
    o	Largest_county_turnout =  “”
    o	Largest_county_vote = 0
Step 3:
  •	While reading the election results from each row inside the for loop, write a script that gets the county name from each row.
    o	For row in reader:
      	Total_votes = total_votes +1
      	Candidate_name = row[2]
      	County_name = row[1]
Step 4a:
  •	Write a decision statement with a logical operator to check if the county name acquired in Step 3 is in the county list you created in Step 1.
    o	If county_name not in county_names:
Step 4b:
  •	If the county is not in the list created in Step 1, add it to the list of county names like you did when adding a candidate to the candidate_options list.
    o	County_names.append(county_name)
Step 4c:
  •	Write a script that initializes the county vote to zero, like you did when you began to track the vote counts for the candidates.
    o	County_votes[county_name] = 0
Step 5:
  •	Write a script that adds a vote to the county’s vote count as you are looping through all the rows, like you did for the candidate’s vote count.
    o	County_votes[county-name] +=1
Step 6a:
  •	Write a repetition statement to get the county from the county dictionary that was created in Step 1.
    o	For county in county_votes:
Step 6b:
  •	Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
    o	County_vote = county_votes[county]
Step 6c:
  •	Write a script that calculates the county’s votes as a percentage of the total votes.
    o	County_percent = float(county_vote) / float(total_votes) * 100
Step 6d:
  •	Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line.
    o	County_results = (
      	f”{county}: {county_percent:.1f}% ({county_vote:,})\n”)
    o	Print(county_results, end=””)
Step 6e: This step will be completed in Deliverable 2.
Step 6f:
  •	Write a decision statement that determines the county with the largest vote count and then adds that county and its vote count to the variables created in Step 2.
    o	If (county_vote > largest_county_vote):
      	largest_county_vote = count_vote
      	largest_county_turnout = county
Step 7:
  •	Write a print statement that prints out the county with the largest turnout.
    o	Largest_county_turnout = (
      	f”\n-------------------------\n”
      	f”Largest County Turnout: {largest_county_turnout}\n”
      	f”-------------------------\n”)
    o	print(largest_county_turnout)
Deliverable 2
Step 6e:
  •	Write a script that saves each county, the county’s total votes, and the county’s percentage of total votes to the election_results.txt file.
    	Txt_file.write(county_results)
Step 8:
  •	Write a script that saves the county with the largest turnout to the election_results.txt file.
    o	Txt_file.write(largest_county_turnout)
After you run your solution to Deliverable 2, confirm that your election_results.txt file matches the following image:
Election results:
![60F7C1A9-9181-486A-B204-448B3A9AAA8A](https://user-images.githubusercontent.com/85171897/137843806-5c8707e2-cb8e-4a86-a583-9777f0e513aa.jpeg)


Deliverable 3: Written Analysis of Election Audit

Overview of Election Audit:
Conduct an election analysis of US Congressional precinct votes in Colorado. Analysis consists of identifying and reporting the total number of votes casts, total number of votes for each candidate and voter turnout for each county, percentage of votes for each candidate and percentage of votes from each county out of the total count, and the winner of the election based on popular (highest number turnout) of votes per candidate and county. Analysis and generating a vote count report helps to certify the US Congressional race. This will be done by navigating to folders using the command line; read and extract data from csv files; use python data types (integers, strings, etc.); perform mathematical operations using data types and declare variables; create and use data structures like lists, dictionaries, and tuples to display information; create and use decision and repetition statements, then eventually save and write data to an output file and print to an output screen displaying results of votes received. 
Election-Audit Results:
  •	How many votes were cast in this congressional election?
     o	There was a total of 369,711 votes cast in the congressional election.
  •	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    o	County votes in the precinct include:
      	Jefferson with 38,855 votes which is 10.5% of total votes
      	Denver with 306,055 votes which is 82.8% of total votes
      	Arapahoe with 24, 801 votes which is 6.7% of total votes
  •	Which county had the largest number of votes?
    o	Denver had the largest county turnout votes.
  •	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    o	Candidate votes received include: 
      	Charles Casper Stockham with 85,213 votes which is 23% of total votes.
      	Diana DeGette with 272,892 votes which is 73.8% of total votes.
      	Raymon Anthony Doane with 11,606 votes which is 3.1% of total votes.
  •	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    o	Diana won the election with 272,892 votes count and winning percentage of 73.8%.

Election-Audit Summary: 
Business proposal on how this script can be used

The script used in the Election Audit analysis using python coding allows modifications and adjustments to be done easily. It is cross-functional and can be commonly used to streamline data from large data sets such as congressional, state, and other types of election polls. It has high readability to help save time in making modifications, adding new coding features with robust library collection of languages and solutions you can use to customize this script based on the needs of your company with the growth of voter population in any given county. The code also offers hyper flexibility in building data models, devise data sets from automated retrieval of information from csv file provided, changing algorithms once again for customization by plugging in real time data, and apply data mining within a succinct period. Article regarding essentials of python for data analysis can be retrieved at this site: https://www.rtinsights.com/why-python-is-essential-for-data-analysis/

We create our list of counties and candidates from the votes within the CSV, rather than hard coding the candidates’ names, so any election results placed in the csv file in the same format can be counted by this code. Below is our if statement, showing an example of how our list of candidates is created and the votes for each candidate are calculated. Our counties list and vote counting works in the same format, with different variable names to support the counties.

The script can be modified in several different ways. If you want to know the date and time of when the script was written for tracking purposes, you can add a date time module that timestamps when the data was ran.

There is a way to check and ensure the data is added to the output screen/file before completion of analysis. The code written to check and ensure each candidate has been added, was also modified to validate the counties were present also. Below is the code written to validate data for candidates, in return was used for validation of counties. This script can be applied to any other type of data for validation in ensuring it has been retrieved from the file and added to output screen/file. 
![image](https://user-images.githubusercontent.com/85171897/137842966-8745f7e5-24f3-4782-8131-87ab3548218e.png)
