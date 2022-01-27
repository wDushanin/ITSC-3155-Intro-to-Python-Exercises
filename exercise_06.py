# Title: Module_01 Exercise_06
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in a row number from 1 to 5 inclusive and a column number from 1 to 5.
# Print out a grid of 0s, but in the row and column entered by the user, print a 1.

# References: 
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

#Variables to create number of rows and columns for 2D array
rows, cols = (5,5)
#Creates array with all entries set to 0
array = [[0 for i in range(cols)]for j in range(rows)]

row_id = int(input(f'Enter a row number from 1 to 5: '))
col_id = int(input(f'Enter a column number from 1 to 5: '))

#Places the 1 in the correct location entered by user
array[row_id-1][col_id-1] = 1

#Prints array in a matrix form
for rows in array:
    print(rows)
