# Part 1: Randomization (30 points) 
# Task 1: Dice Roller Simulation (10 points) 

import random

print("Welcome to the Randomization application")

roll_dice1 = print(random.randint(1, 6))

roll_dice2 = print(random.randint(1, 6))

print("Total:", random.randint(1, 6) + random.randint(1, 6))

# print("Rolling dice:",  roll_dice1 + roll_dice2)

# Task 2: Random Meal Selector (10 points) 

print("----------------Welcome to the random meal selector program---------------- \n")

breakfast_list = ["Bread and Tea", "Corn flakes", "Golden More"]

lunch_list = ["Rice and beans", "Chicken and rice", "Yam and Egg"]

dinner_list = ["Eba and okro soup", "Poundo yam and stew", "Custard"]

print("Breakfast:", random.choice(breakfast_list))

print("Lunch:", random.choice(lunch_list))

print("Dinner:", random.choice(dinner_list))

# Task 3: Rock, Paper, Scissors Game (10 points) 

print("----------------Welcome to the Rock, Paper, Scissors game!----------------")

choice = ["rock","paper","scissors"]

user_choice = input("Enter your choice Rock, Paper or Scissors: ").lower()

computer_choice = random.choice(choice)

print(f"You choose: {user_choice} and computer choose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
else:
    print("You Lost!")

# Part 2: Lists (30 points) 
# Task 4: Favorite Foods List (15 points) 

print("------------------------Food List------------------------")
fav_food_list = ["Rice", "Pundo Yam","spagetti", "Fried Rice", "Egg and plaintain"]

fav_food_list.append(fav_food_list)
print(f"Your fav foodlist : {fav_food_list}")

fav_food_list.insert(1, "beans")

fav_food_list.remove("Rice")

fav_food_list.reverse()

# fav_food_list.sort()

print(fav_food_list)

# Task 5: Random Name Selector (15 points) 

print("-----------------------Random Name Selector-----------------------------")

friend_list = []

# Append the friend's name to the list
friend_list.append(input("Friend Name: "))
# friend_list.insert(0, input("Friend Name: "))
friend_list.append(input("Friend Name: "))
friend_list.append(input("Friend Name: "))
friend_list.append(input("Friend Name: "))
friend_list.append(input("Friend Name: "))
friend_list.append(input("Friend Name: "))

print(friend_list)  # Optional: To check the added name
print(f"The winner is {random.choice(friend_list)}") # Optional:



