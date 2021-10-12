#PyPoll.py

#First we'll import the os module
#This will allow us to create file path across operating system
import os
#Import module for reading csv files
import csv

#Assign a variable for the file to load and the path
csvpath = os.path.join('Resources', 'election_results.csv')
#file_to_load = os.path.join("Resources", "election_results.csv.py")

#Method 1: plain reading of csv file 
#with open(csvpath, 'r')
with open(csvpath) as election_data:
 #as election_data:
    lines = election_data.read()
    #print(lines)
    #print(type(lines))
    #print(election_data)
#Close the file
#election_data.close()

 #Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")  
 #Using the open() function with "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
#with open (file_to_save, "w") as txt_file:
#write some data to the file
#outfile.write("Hello World")
    #txt_file.write("Hello World, ")

#write three counties to the file
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #add newline escape sequence 
    #txt_file.write("Arapahoe\nDenver\nJefferson")

#Close the file
#outfile.close()

#To do: read and analyze the data here.
#Read the file object with the reader function and open election results
with open(csvpath) as election_data:
    file_reader = csv.reader(election_data)

    print(file_reader)

#print each row in the CSV file by retrieving first item from each row
#for row in file_reader:
    #for i in range(len(row)):
        #print(row[i])

#read and print the header row.
    csv_headers = next(file_reader)
    print(csv_headers)

#print each row in the CSV file by retrieving first item from each row
    for row in file_reader:
        for i in range(len(row)):
            print(row[i])

#file_reader.close()


    



   
#The date we need to retrieve.

# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote.