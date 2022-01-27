# Title: Module_01 Exercise_03
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in an integer greater than 1.
# Print out the squares of each integer from 0 to the inputted integer.

# References: 
# https://www.w3schools.com/python/ref_func_range.asp



number = int(input('Enter an integer greater than 1: '))

for i in range(number + 1):
    print(f'The square of {i} is {i**2}')

