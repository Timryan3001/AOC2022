from aoc_utils import fetch_input, get_day_from_filename
import os
import time

# This file is a template for future days

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

#FETCHING INPUTS

day = get_day_from_filename(os.path.basename(__file__))

input_data = fetch_input(day)

lines = input_data.splitlines()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p1 = time.time()

repeated_chars = []

for line in lines:
    halfway = int(len(line)/2)
    comp1, comp2 = set(line[:halfway]),set(line[halfway:])
    # print(f'The first compartment is {comp1}, the second is {comp2}')
    for char in comp1:
        if char in comp2:
            repeated_chars.append(char)

# print(repeated_chars)

lowercase = [chr(i) for i in range(97, 123)]
uppercase = [chr(i) for i in range(65, 91)]

all_letters = lowercase + uppercase

numbers = [num for num in range(1,100)]

# using naive method
# to convert lists to dictionary
res = {}
for key in all_letters:
    for value in numbers:
        res[key] = value
        numbers.remove(value)
        break

# Printing resultant dictionary
# print("Resultant dictionary is : " + str(res))

score = sum(res[char] for char in repeated_chars)

print(f"sum of priorities is {score}")

end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

groups_of_3 = [lines[i:i+3] for i in range(0, len(lines), 3)]

pt2_repeats = []

for group in groups_of_3:
    common_chars = list(set(group[0]) & set(group[1]) & set(group[2]))
    pt2_repeats.extend(common_chars)
    # print(common_chars)

print(pt2_repeats)

pt2_score = sum(res[char] for char in pt2_repeats)

print(f"sum of priorities is {pt2_score}")

end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #