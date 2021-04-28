import os
import csv

# Path to collect data from the Resources folder
csv_file_path = Path("..", "Resources", "election_data.csv")

# Specify an output folder 
output_path = os.path.join("..", "Analysis", "election_analysis.txt")

# Declare the variables
total_votes = 0
khan_votes = 0
correy_votes = 0 
li_votes = 0
otooley_votes = 0 

#The total number of votes cast
for row in csvreader:
    total_votes +=1
    
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won will be seen in the print statements 
    if row[2] == "Khan":
        khan_votes +=1
    elif row[2] == "Correy":
        correy_votes +=1
    elif row[2] == "Li":
        li_votes +=1
    elif row[2] == "O'Tooley":
        otooley_votes +=1

# In order to find the total number of votes each candidate won need to make a dictionary from the two lists that were created 
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

#Need to zip the list of candidates and the total amount of votes 
# Will get the winner of the election based on popular vote by using the max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Need to print the summary of the analysis 
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) *100
li_percent = (li_votes/total_votes) *100
otooley_percent = (otooley_votes/total_votes) *100

# Print Statements
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"Winner: {key}")
