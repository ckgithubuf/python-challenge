import csv

with open('Resources/election_data.csv', 'r') as csv_file:
    election_data = csv.DictReader(csv_file)
    election_data = list(election_data)
    total_number_of_votes = len(election_data)
    candidate_data = {}
    for row in election_data:
        candidate_data[row['Candidate']] = candidate_data.get(row['Candidate'], 0) + 1
    winner = max(candidate_data, key = candidate_data.get)
    print("Election Results\n")
    print("-------------------------")
    print(f"Total Votes: {total_number_of_votes}\n")
    print("-------------------------\n")
    for name, vote_count in candidate_data.items():
        votes_percentage = round(vote_count/total_number_of_votes * 100, 3)
        print(f"{name}: {votes_percentage}% ({vote_count})\n")    
    print(f"Winner: {winner}\n")
        
