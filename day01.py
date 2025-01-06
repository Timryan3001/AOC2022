from aoc_utils import fetch_input, get_day_from_filename
import os
import time

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))


input_data = fetch_input(day)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

#parsing all the inputs
groups = input_data.split("\n\n")

list_of_lists = []

for group in groups:
    numbers = group.split("\n")
    numbers = [int(num) for num in numbers]

    list_of_lists.append(numbers)

# print(list_of_lists)

#testing if summing lists works
test = [1,2,3]
# print(sum(test))

summed_lists = []

for list in list_of_lists:
    sums = sum(list)
    summed_lists.append(sums)

summed_lists.sort()
# print(summed_lists[-1])

end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

top_3 = summed_lists[-3:]

end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(summed_lists[-1])
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")
print(sum(top_3))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #