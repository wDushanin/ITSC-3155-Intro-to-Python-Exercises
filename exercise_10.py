# Title: Module_01 Exercise_10
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: 
# Take in a string from the user and split it into an 
# array of single characters. Split the list of characters into a 
# list of lists where each inner list has 3 elements. Notice that the
# last inner array may have less than 3 elements.

# References: 
# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
# https://sites.pitt.edu/~naraehan/python3/split_join.html
# https://www.geeksforgeeks.org/python-split-a-list-into-sublists-of-given-lengths/
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

word = input('Enter a string: ')

#split word into individual chars
characters = list(word)

#variable for length of lists
length = 3

#use list comprehension to break into multiple arrays of length 
answer = [characters[i: i + length] for i in range(0, len(characters), length)]

print(answer)