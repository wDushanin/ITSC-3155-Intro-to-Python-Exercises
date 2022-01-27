# Title: Module_01 Exercise_08
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in 10 integers from user. Create a new list with only elements
# which appear once. Print the list with the unique elements.

# References: 
# https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
# https://www.kite.com/python/answers/how-to-count-item-frequency-in-python

# creates list to store inputs

list_01 = []
freq = {}
list_02 = []

#Asks users for the elements of list_01
for i in range(0, 10):
    # Asks user for individual list_01 inputs
    num = int(input(f'Enter number for list_01: '))
    # Adds inputs to the list_01
    list_01.append(num)

for elem in list_01:
    if elem in freq:
        freq[elem] += 1
    else:
        freq[elem] = 1

if freq == 1:
    list_02.append(freq)

print(list_02)
