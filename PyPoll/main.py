# import dependencies
import os
import csv

# grabbing the csv needed for the assignment 
election_csv = os.path.join("Resources", "election_data.csv")

# Create variable that holds a dicitonary, lists, and counter
election = {}

candidate = []
vote_count = []
vote_percentage = []

total_votes = 0
# read csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# iterate through each row to find total votes as well as each unique candidate 
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1

# iterate through each item in my election dictionary to add my candidate key and vote count value
for key, value in election.items():
    candidate.append(key)
    vote_count.append(value)

# iterate through each amount of candidate votes to turn them into percentages  
for votes in vote_count:
    vote_percentage.append(round((votes/total_votes)*100, 1))

# create two variables that finds the highest vote count and then match the candidate with the highest vote count
highest_vote = max(vote_count)
winner = candidate[vote_count.index(highest_vote)]

# create a variable to hold my all lists as a list
new_data = list(zip(candidate, vote_count, vote_percentage))

# print results
print("Election Results \n-------------------------")
print(f'Total Votes: {total_votes} \n-------------------------')
for entry in new_data:
    print(f'{entry[0]}: %{entry[2]} ({entry[1]})')
print(f'------------------------- \nWinner: {winner} \n-------------------------')

# export text file with my results
f = open('election_results.txt', 'w')

with open('election_results.txt', 'w') as f:
    f.write("Election Results \n-------------------------")
    f.write(f'\nTotal Votes: {total_votes} \n-------------------------')
    for entry in new_data:
        f.write(f'\n{entry[0]}: %{entry[2]} ({entry[1]})')
    f.write(f'\n------------------------- \nWinner: {winner} \n-------------------------') 







