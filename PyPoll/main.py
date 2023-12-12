import csv

'''
Script for reading election_data.csv file and answer below questions
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote
And redirects output to a text file in analysis folder
'''
with open('Resources/election_data.csv', 'r') as csv_file:
    # Reading election data into csv
    election_data = csv.DictReader(csv_file)
    election_data = list(election_data)
    # Counting number of entries in the csv (which amounts to total number of votes)
    total_number_of_votes = len(election_data)
    candidate_data = {}
    # Iterating through each row/entry and adding candidate name into a dictionary
    # Also, keeping track of how many times candidate's name has appeared in the result set
    for row in election_data:
        candidate_data[row['Candidate']] = candidate_data.get(row['Candidate'], 0) + 1
    # Gets the entry who has the maximum number of votes      
    winner = max(candidate_data, key = candidate_data.get)
    # Redirecting results to output.txt file in analysis folder
    with open("analysis/output.txt", "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_number_of_votes}\n")
        file.write("-------------------------\n")
        # Iterate through dictionary and calculate percentage of votes each voter has won
        for name, vote_count in candidate_data.items():
            votes_percentage = round(vote_count/total_number_of_votes * 100, 3)
            file.write(f"{name}: {votes_percentage}% ({vote_count})\n")    
        file.write("-------------------------\n")        
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------")
    # Final output being printed to console   
    with open("analysis/output.txt", "r") as f:
        print(f.read())        
        
