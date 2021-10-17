#PyPoll.py

#Add dependencies
#Import module for reading csv files
import csv
#Will import os module allow to create file path across operating system
import os

#Assign a variable for the file to load and the path
csvpath = os.path.join('Resources', 'election_results.csv')
#file_to_load = os.path.join("Resources", "election_results.csv")

#Method 1: plain reading of csv file 
#with open(csvpath, 'r')
with open(csvpath) as election_data:
 #as election_data:
    lines = election_data.read()
    
 #Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")  
 
#Initialize a total vote counter.
total_votes = 0

#Candidates options and candidate votes
candidate_options = []
candidate_votes = {}

#Initialize a county list and county votes
county_options = []
county_votes = {}

#declare a variable holding empty string value for winning candidate and winning count tracker
# selected from candidate_options. 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#declare a variables by initializing a county list and county votes

#To do: open, read, and analyze the data here in file.
#Read the file object with the reader function and open election results
with open(csvpath) as election_data:
    file_reader = csv.reader(election_data)

    print(file_reader)

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
        county_name = row[1]

#file_reader.close()
#declare a new list and add candidate name to the candidate list
        #candidate_options.append(candidate_name)

        #Use if statement to align with for loop - if the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking candidate's vote count; set to 0 then start tally votes
            candidate_votes[candidate_name] = 0
            #add a vote to candidate's count by 1 everytime we run file
        candidate_votes[candidate_name] += 1
print(candidate_votes)

#modify code to write the election_results to text file
with open(file_to_save, "w") as txt_file:
        
# Print the final vote count (argument) to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
            
        #print with parameter end="" to an empty string
        #print(election_results, end="")
        print(election_results, end="")
    # Save the final vote count to the text file.
        txt_file.write(election_results)

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list.
        for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
    #calculate percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
    #print the candidate name and percentage of votes
#print(f"{candidate_name}: received {vote_percentage}% of the vote.")
#To do: print out each candidate's name, vote count, percent of votes to terminal
#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#add each candidate's election results to election_analysis.txt
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
# #print each candidate their voter count and percentage to the terminal
#         print(candidate_results)

#save the candidate results to our text file
        txt_file.write(candidate_results)

#print each candidate their voter count and percentage to the terminal
        print(candidate_results)

#determine winning vote count and candidate
#determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
    
    #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
    #set the winning_candidate from candidate_options equal to the candidate's name.
            winning_candidate = candidate_name
    
    #print out the winning candidate summary
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
        print(winning_candidate_summary)
#Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
