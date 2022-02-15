import constant
"""
Program: average_scores.py
Author: Patricia Hernandez-Vasquez
Last date modified: 02/08/2022
The purpose of this program is to take in a users first and last name, age, and three test scores to find their average grade
The output should show their last name, first name, age, and average grade in order.
"""

"""
Below I took notes, made comments
"""

# store a constant for number of scores we will input: 3, put at top of file

# prompt user for input
# store input as first_name
first_name = input("Please enter your first name: ")
# store input as last_name
last_name = input("Please enter your last name: ")
# add age input
age = input('Please enter your age: ')

# prompt user for the scores (do it constant times, use ....)
first_score = int(input("Please enter first score: "))
second_score = int(input("Please enter second score: "))
third_score = int(input("Please enter third score: "))

# calculate an average
average_score = (first_score + second_score + third_score) / constant.NUMBER_OF_SCORES

print(f"{last_name.capitalize()}, {first_name.capitalize()} age: {age} average grade:{average_score: 5.2f}")

# print output; should look like
# Rodriguez, Linda age: 21 average grade: 92.50
