# Title: Module_01 Exercise_01
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: 
# Write a script that takes in a grade from 0-100 inclusive 
# (include both 0 and 100 in the range). 
# Assuming a normal 10 point grading scale,
# print off whether the user got an A, B, C, D, or F.

# References: 
# Lecture 02 Video

# STRING variable typecast to an INT variable
grade = int(input('Enter a grade from 0 to 100: '))

if grade >= 90: 
    print('You got an A')
elif grade >= 80:
    print('You got a B')
elif grade >= 70:
    print('You got a C')
elif grade >= 60:
    print('You got a D')
else:
    print('You got a F')