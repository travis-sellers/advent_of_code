## Script: day_1_advent_code.py
## Author: Travis Sellers
## Date: 12/1/20
## Purpose: Download Santa's expense report from advent of code 
##          and find the two values that add up to 2020, then
##          find those two values' product

# Import necessary modules
import pandas as pd
import numpy as np

# Define the path where the input data for day 1 is saved and read
# in the expense data for Santa Claus as a pandas dataframe
path = "C:/Users/t669365/Documents/advent_of_code/advent_of_code/data/expenses.csv"
df = pd.read_csv(path)

# Identify the column name in this data frame
col = str(df.columns.tolist()[0])

# Execute a loop that will sample two values from the expense column and find
# their sum. The loop will stop once two values with a sum of 2020 has been found.
def expense_slvr(num_values=2):

	exp_sum = 0

	while exp_sum != 2020:

		# Sample two expense values from the dataframe and find their sum
		values = df[col].sample(n=num_values)
		exp_sum = values.sum()

		if exp_sum == 2020:
			values = values.tolist()
			print("The following values have a sum of 2020: ")
			print(*values, sep=" ")
			print(f"The product of these values is {np.prod(values)}")

# Find the values that sum to 2020 for the two and three value problem.
expense_slvr(num_values=2)
expense_slvr(num_values=3)