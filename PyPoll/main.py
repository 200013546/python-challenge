# Import Modules
import os
import csv

#  Create Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Get Path For File
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvfile)

    # Read Data After The Header
    for row in csvreader:
        
        # The total number of votes cast
        total_votes += 1
        
        # A complete list of candidates who received votes
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # The winner of the election based on popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join('.', 'Resources', 'election_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as textfile:

# Write New Data
    textfile.write(f"Election Results\n")
    textfile.write(f"---------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"---------------------------\n")
    textfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    textfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    textfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    textfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    textfile.write(f"---------------------------\n")
    textfile.write(f"Winner: {winner_name}\n")
    textfile.write(f"---------------------------\n")