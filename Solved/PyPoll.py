#PyPoll.py

#First we'll import the os module
#This will allow us to create file path across operating system
import os
#Import module for reading csv files
import csv

#Assign a variable for the file to load and the path
#csvpath = os.path.join("..", "Resources", "election_results.csv")
file_to_load = 'Resources'

#Method 1: plain reading of csv file 
with open(csvpath, 'r') as election_data:
    lines = election_data.read()
    print(lines)
    print(type(lines))


    #To do: perform analysis.
    #print(election_data)

#Close the file.
#election_data.close()


#The date we need to retrieve.

# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote.