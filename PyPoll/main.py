import csv
import os
# Define the source  path for the  csv file
file_path = r"PyPoll/Resources/election_data.csv"
#Define the source path for the result text file in the analysis folder
result_path = r"PyPoll/Analysis/election_resultstest.txt"
# Get the list for the variables required during the script
total_votes = []
Candidates = []
Candidates_summary= {}
votes=[]
vote_result = []
percent_result = []

Winner_count = 0

# open the file
with open(file_path) as file:
    filereader = csv.reader(file, delimiter=",") # demlmiter for the comma seperated values
    header = next(filereader) #skip the header
    
    for row in filereader: #start the loop from the second row
        
        total_votes.append(row[0])
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Candidates_summary[row[2]] = 0
        Candidates_summary[row[2]]= Candidates_summary[row[2]] + 1

print(Candidates_summary)
#write the results into the file
with open(result_path, 'x', newline='') as wf: 
    
    wf.write(f"Election Results\n")
    wf.write(f"_ _ _ _ _ _ _ _ _ _\n")
    wf.write(f"Total Votes {len(total_votes)} \n")
    wf.write(f"_ _ _ _ _ _ _ _ _ _\n")
    #find the total votes and winner based n the number of votes received by the candidate
    for unique in Candidates_summary:
        votes = Candidates_summary.get(unique)
        percentage = (float(votes)/float(len(total_votes)))*100
        results = f"{unique} : {percentage:.3f}% ({votes :})\n"
        if (votes> Winner_count) :
            Winner_count = votes
            Winner = unique
        wf.write(results)
    wf.write(f"_ _ _ _ _ _ _ _ _ _\n")
    wf.write(f"Winner : {Winner}\n")
    wf.write(f"_ _ _ _ _ _ _ _ _ _\n")
 #print the result to the terminal   
with open(result_path) as f:
    lines = f.readlines()
    for each in lines:
        print(each)  