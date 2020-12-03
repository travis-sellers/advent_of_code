# Script: day_3_advent_code.py
# Author: Travis Sellers
# Date: 12/3/20
# Purpose: Download sledding map from advent of code
# and find the number of trees that you would
# encounter if you sled RIGHT 3 DOWN 1.


##########
# Part 1 #
##########

# Import necessary modules for task
import itertools
import math

# Define the path where the input data for day 3 is saved
# and read in the map data as a list
data_path = "C:/Users/t669365/Documents/advent_of_code/data/"
file = data_path + "sled_map.txt"

# Create an empty list that will contain each line of the map in its own list
map_list = []

with open(file, 'r', encoding='utf8') as inpt:
    for line in inpt:
        stripped_line = line.strip()
        line_list=stripped_line.split()
        map_list.append(line_list)

# Each line only shows the pattern that each 'line' has on the map.
# This pattern continues indefinitely on each line so let's replicate
# this base on the number of observations and the number of right moves 
# that are made each time we move (3 in this case)
def tree_hits(dm=1, rm=3):

	down_moves = dm
	right_moves = rm
	map_len = len(map_list)
	lists_len = len(map_list[0][0])

	if down_moves == 1:
		reps = math.ceil((right_moves*map_len)/lists_len)
	else:
		reps = math.ceil((right_moves*(map_len/down_moves))/lists_len)

	# Now let's replicate each line (or list in this case) `reps`-1 times
	wide_map_list = []
	for line in map_list:
	    wide_line = list(itertools.repeat(line[0], reps))
	    wide_map_list.append(''.join(wide_line))

	# Now let's loop through the wide map list and count the number of times we hit a tree
	trees_hit = 0
	for i in range(math.ceil(map_len/down_moves)-1):
	    if wide_map_list[(i+1)*down_moves][(i+1)*right_moves] == '#':
		    trees_hit += 1

	print(f"With {str(down_moves)} down moves and {str(right_moves)} right moves, {str(trees_hit)} trees were hit during the sledding adventure!")

	return trees_hit

print(tree_hits())
trees_prod = tree_hits()*tree_hits(dm=1,rm=1)*tree_hits(dm=1,rm=5)*tree_hits(dm=1,rm=7)*tree_hits(dm=2,rm=1)

print(f"The product of trees hit is {str(trees_prod)}")
