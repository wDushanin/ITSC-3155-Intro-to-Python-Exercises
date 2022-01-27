# Title: Module_01 Exercise_09
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in 5 words from the user. Create a single string from 
# the individual words, separated by spaces, and print the string

# References: 
# https://www.afternerd.com/blog/python-convert-list-string/

list_01 = []
#Asks users for the elements of list_01
for i in range(0, 5):
    # Asks user for individual list_01 inputs
    word = input('Enter a word: ')
    # Adds inputs to the list_01
    list_01.append(word)

#use the join method to catenate the elements in the STR list
sentence = " ".join(list_01)

print(sentence)