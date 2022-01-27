# Title: Module_02 Exercise_11
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 26, 2022

# Description: script that takes in a string from the user. 
# Print the string out backwards.

# References: 
# https://www.w3schools.com/python/python_howto_reverse_string.asp

#Takes user's string input and slices backwards on step at a time
#the slice step and direction is determined by the integer
# (seen here as "-1")
#Documentation for future self: a_string[start:stop:step]
string_01 = input('Enter a string: ') [:: -1]
print(string_01)