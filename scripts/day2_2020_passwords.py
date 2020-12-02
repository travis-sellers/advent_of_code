## Script: day_2_advent_code.py
## Author: Travis Sellers
## Date: 12/2/20
## Purpose: Download corrupted password list from advent of code 
##          and find the number of passwords that are valid based
##          on the rule set associated with each password


##########
# Part 1 #
##########

# Import necessary modules
import pandas as pd

# Define the path where the input data for day 2 is saved 
# and read in the password data as a list
data_path = "C:/Users/t669365/Documents/advent_of_code/data/"
file = data_path + "passwords.txt"

with open(file, 'r', encoding='utf8') as inpt:
    passwords = inpt.read().split('\n')

# Convert list into a pandas dataframe
df = pd.DataFrame(passwords, columns=['password'])

# Convert column into multiple columns
df[['min_max_l', 'letter', 'word']] = df.password.str.split(expand=True)

# Split min and max letter occurrance column into two colums
df[['min_l', 'max_l']] = df.min_max_l.str.split('-', expand=True)

# Remove ':' character from letter column
df['letter'] = df['letter'].map(lambda x: x.rstrip(':'))

# Now clean up dataframe and identify observations that meet password requirements
final_df = df[['word','min_l','max_l','letter']]
convert_dict = {'min_l': int, 'max_l': int}
final_df = final_df.astype(convert_dict)

# Create a column that counts the number of instances a letter is observed in a password
final_df['letter_count'] = None

for i in range(len(final_df['word'])):
	final_df['letter_count'][i] = final_df.word[i].count(final_df.letter[i])

# Now let's identify how many passwords meet their requirements
print(f"There are {len(final_df.query('letter_count >= min_l and letter_count <= max_l'))} passwords that meet requirements.")

# Preview some of the observations that meet the requirements.
print(final_df.query('letter_count >= min_l and letter_count <= max_l').head())


##########
# Part 2 #
##########

# Let's redefine the max and min columns as position values.
# In other words, these values now denote positions where 
# the corresponding letter should exist in the password string
# Remember 0-indexing and that the letter has to be in EXACTLY
# one of the position values (i.e. can't be in both or neither).
final_df = final_df.rename(columns = {'min_l' : 'pos_1', 'max_l' : 'pos_2'})
final_df['pos_1'] = final_df['pos_1']-1
final_df['pos_2'] = final_df['pos_2']-1

# Now loop through each password and check to see if the letter in question
# is at one of the two required positions
correct_passwords = 0
for i in range(len(final_df)):
	num_matches = 0
	for j,c in enumerate(final_df['word'][i]):
		if final_df['letter'][i] == c and (final_df['pos_1'][i] == j or final_df['pos_2'][i] == j):
			num_matches += 1

	if num_matches == 1:
		correct_passwords += 1

print(f"There are a total of {correct_passwords} passwords that work with the new rules.")



