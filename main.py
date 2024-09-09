# Part 1: Randomization (30 points) 
# Task 1: Dice Roller Simulation (10 points) 

import random

print("Welcome to the Randomization application")

roll_dice1 = print(random.randint(1, 6))

roll_dice2 = print(random.randint(1, 6))

print("Total:", random.randint(1, 6) + random.randint(1, 6))

# print("Rolling dice:",  roll_dice1 + roll_dice2)

# Task 2: Random Meal Selector (10 points) 

print("Welcome to the random meal selector program")

breakfast_list = ["Bread and Tea", "Corn flakes", "Golden More"]

lunch_list = ["Rice and beans", "Chicken and rice", "Yam and Egg"]

dinner_list = ["Eba and okro soup", "Poundo yam and stew", "Custard"]

print("Breakfast:", random.choice(breakfast_list))

print("Lunch:", random.choice(lunch_list))

print("Dinner:", random.choice(dinner_list))

  