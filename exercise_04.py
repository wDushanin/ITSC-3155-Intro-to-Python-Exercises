# Title: Module_01 Exercise_04
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in a number, n, from the user. 
# Then, take in n floats from the user and store them in a list. 
# For instance, if the user enters 4, then the user will have to enter 4 numbers. 
# Print the list and the mean.

# References: 
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
# https://www.geeksforgeeks.org/find-average-list-python/
# https://www.geeksforgeeks.org/sum-function-python/
# https://realpython.com/len-python-function/

# create a list to store inputs
list = []

# Ask user for size of list
num = int(input('Enter a number: '))

# iterates through the range of entered number
# Starts with position zero and ends with entered number
# (Remember that the last position is n-1, not the actual entered number)
for i in range(0, num):
    # Asks user for individual list inputs
    float_num = float(input(f'Enter number {i+1}: '))
    # Adds inputs to the list
    list.append(float_num)

# Prints the appended list
print(f'List: {list}')

# temporary variable to sum the list elements
temp = sum(list)

# Finds the average of the list by dividing the sum by the length of the list
average = temp/len(list)

# Rounds the average to two decimals and stores result in average variable
average= round(average, 2)
print(f'Average: {average}')

