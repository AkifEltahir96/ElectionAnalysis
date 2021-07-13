# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved voted
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime

# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()

#Print the present time.
print("The time right now is ", now)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'
with open(file_to_load) as election_data:
    # To do: preform analysis.
    print(election_data)

# Close the file.
election_data.close()

import csv
import os

# Assign a variable for the file to load and the path.
ind_file_to_load = os.path.join("Resources", "election_results.csv")
with open(ind_file_to_load) as ind_election_data:
    
    # To do: preform analysis.
    print(ind_election_data)



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

import csv
import os

# Assign a variable for the file to load and the path.
ind_file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources", "election_analysis.txt")

with open(ind_file_to_load) as election_data:
    file_reader = csv.reader(election_data)

for row in file_reader:
    print(row)
