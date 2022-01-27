# Title: Module_01 Exercise_05
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in 5 integers from the user and store them in a list.
# Then take in another 5 integers and store them in a separate list.
# Create a third array containing the common values from both arrays without duplicates.
# Print out this third list.

# References: 
# https://www.kite.com/python/answers/how-to-find-common-elements-between-two-lists-in-python
# https://www.kite.com/python/docs/builtins.set.intersection

# creates first list to store inputs
list_01 = []

#creates second list to store inputs
list_02 = []

#Asks users for the elements of list_01
for i in range(0, 5):
    # Asks user for individual list_01 inputs
    num = int(input(f'Enter number for list_01: '))
    # Adds inputs to the list_01
    list_01.append(num)

#Asks users for the elements of list_02
for i in range(0, 5):
    # Asks user for individual list_02 inputs
    num = int(input(f'Enter number for list_02: '))
    # Adds inputs to the list_02
    list_02.append(num)

#Converst lists to sets in order to use intersection 
set_01 = set(list_01)
set_02 = set(list_02)

#Compares the two lists and finds the common elements (aka intersection of the sets)
common = set_01.intersection(set_02)

#print the result
print(common)