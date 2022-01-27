# Title: Module_01 Exercise_02
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description:
# Write a script that takes in two strings from the user. 
# If one string is the prefix of the other string, 
# print "True", otherwise, print "False".

# References: 
# https://www.pythontutorial.net/python-string-methods/python-string-startswith/

string_01 = input('Enter your first word: ')
string_02 = input('Enter your second word: ')
result = string_02.startswith(string_01)
print(result)
