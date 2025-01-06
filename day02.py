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

lines = input_data.strip().split("\n")
column1 = []
column2 = []


for line in lines:
    col1, col2 = map(str, line.split()) 
    column1.append(col1)
    column2.append(col2)

# creating tuples
tuples = list(zip(column1,column2))

tuple_set = set(tuples)


def calc_game_scores(tuples):
    score = 0
    for m1, m2 in tuples:
        if m2 == 'X' and m1 == 'A':
            score += 3
        elif m2 == 'X' and m1 == 'B':
            score += 0
        elif m2 == 'X' and m1 == 'C':
            score += 6
        elif m2 == 'Y' and m1 == 'A':
            score += 6
        elif m2 == 'Y' and m1 == 'B':
            score += 3
        elif m2 == 'Y' and m1 == 'C':
            score += 0       
        elif m2 == 'Z' and m1 == 'A':
            score += 0
        elif m2 == 'Z' and m1 == 'B':
            score += 6
        elif m2 == 'Z' and m1 == 'C':
            score += 3

    return score

score = calc_game_scores(tuples)

def add_on_base_values(tuples):
    base_value = 0 
    for m1,m2 in tuples:
        if m2 == 'X':
            base_value += 1
        elif m2 == 'Y':
            base_value += 2
        elif m2 == 'Z':
            base_value += 3

    return base_value
    

base_value = add_on_base_values(tuples)

total_score = base_value+score

print(total_score)

print(f"Score from results is {score}\nScore from base values is {base_value}\nScore in total is {total_score}")


end_time_p1 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

start_time_p2 = time.time()

#part 2 goes here

def p2_calc_game_scores(tuples):
    p2_score = 0
    for m1, m2 in tuples:
        if m2 == 'X' and m1 == 'A':
            p2_score += 3
        elif m2 == 'X' and m1 == 'B':
            p2_score += 1
        elif m2 == 'X' and m1 == 'C':
            p2_score += 2
        elif m2 == 'Y' and m1 == 'A':
            p2_score += 4
        elif m2 == 'Y' and m1 == 'B':
            p2_score += 5
        elif m2 == 'Y' and m1 == 'C':
            p2_score += 6     
        elif m2 == 'Z' and m1 == 'A':
            p2_score += 8
        elif m2 == 'Z' and m1 == 'B':
            p2_score += 9
        elif m2 == 'Z' and m1 == 'C':
            p2_score += 7

    return p2_score

p2_score = p2_calc_game_scores(tuples)

print(f"Score from results is {p2_score}")


end_time_p2 = time.time()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RESULTS # 

print(f"Execution Time for P1: {end_time_p1 - start_time_p1:.4f} seconds")
print(f"Execution Time for P2: {end_time_p2 - start_time_p2:.4f} seconds")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #