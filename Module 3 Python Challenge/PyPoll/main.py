#PyPoll
import os
import csv

election_csv = r'C:\Users\Jeremy Morris\OneDrive\Desktop\OSU Data Analysis Course\Modules\Module 3 Python Challenge\PyPoll\Resources\election_data.csv'

total_votes = 0
Doane_votes = 0
DeGette_votes = 0
Stockham_votes = 0

with open('Modules/Module 3 Python Challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes +=1
        if row[2] == "Raymon Anthony Doane":
            Doane_votes +=1
        elif row[2] == "Diana DeGette":
            DeGette_votes +=1
        elif row[2] == "Charles Casper Stockham":
            Stockham_votes +=1

#dictionary of the lists 
candidates = ["Doane", "DeGette", "Stockham"]
votes = [Doane_votes, DeGette_votes, Stockham_votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)

#sumamry table
Doane_percent= (Doane_votes/total_votes)*100
DeGette_percent= (DeGette_votes/total_votes)*100
Stockham_percent= (Stockham_votes/total_votes)*100 


#The total number of votes cast


#A complete list of candidates who received votes

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
print(f"Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})")
print(f"-------------------------")
print(f"Winner: {key}")
print(f"-------------------------")


#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

#Write summary table election results to text file
output_folder = r'C:\Users\Jeremy Morris\OneDrive\Desktop\OSU Data Analysis Course\Modules\Module 3 Python Challenge\PyPoll\analysis'
output_file = os.path.join(output_folder, 'Election_Results_Summary_table.txt')

with open(output_file, "w") as file:
    file.write(f"Election Results\n")
    file.write(f"-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"-------------------------\n")
    file.write(f"Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes})\n")
    file.write(f"Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})\n")
    file.write(f"Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})\n")
    file.write(f"-------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"-------------------------\n")