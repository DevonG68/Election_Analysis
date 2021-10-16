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
        # for i in range(len(row)):
        #     print(row[i])

# 2. add to the total vote count
        total_votes += 1
        #print (row[2])
        candidate_name = row[2]

#file_reader.close()
#declare a new list and add candidate name to the candidate list
        #candidate_options.append(candidate_name)

        #If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking candidate's vote count; set to 0 then start tally votes
            candidate_votes[candidate_name] = 0
            #add a vote to candidate's count by 1 everytime we run file
            candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list.
    for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
    #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
    #print the candidate name and percentage of votes
print(f'{candidate_name}: received {vote_percentage}% of the vote.')
# To do: print out each candidate's name, vote count, percent of votes to terminal
print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

#declare a variable holding empty string value for winning candidate and winning count tracker
# selected from candidate_options
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#determine winning vote count and candidate
#determine if the votes are greater than the winning count
If (votes > winning_count and (vote_percentage > winning_percentage):
    #if true then set winning_count = votes and winning_percent = vote_percentage
    winning_count = votes
    winning_percentage = vote_percentage
    #set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name
    
    #print out the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"))
print(winning_candidate_summary)