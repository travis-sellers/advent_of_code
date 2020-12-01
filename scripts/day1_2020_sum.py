## Script: day_1_advent_code.py
## Author: Travis Sellers
## Date: 12/1/20
## Purpose: Download Santa's expense report from advent of code 
##          and find the two values that add up to 2020, then
##          find those two values' product

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
exp_sum = 0
while exp_sum != 2020:

	# Sample two expense values from the dataframe and find their sum
	values = df[col].sample(n=2)
	exp_sum = values.sum()

	if exp_sum == 2000:
		values = values.tolist()
		print(f"The values {str(values[0])} and {str(values[1])} have a sum of 2020.")
		print(f"The product of these two values is {np.prod(values)}")