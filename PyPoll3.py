# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Read and Print the Header Row.
    headers = next(file_reader)


# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes = total_votes + 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin Tracking votes
            candidate_votes[candidate_name] = 0
    
        #Adding Votes
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


#Use a for loop to iterate through the candidate_options list
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) /float(total_votes) * 100
    print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")

print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#Determining the winner.
if (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_percentage = vote_percentage
    winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary) 
    