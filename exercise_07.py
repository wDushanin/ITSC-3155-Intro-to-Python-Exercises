# Title: Module_01 Exercise_07
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: January 18, 2022

# Description: Take in integers until the user types "QUIT" and
# store the numbers in an array. Assume any input other than "QUIT"
# is a valid integer. Create another array of just the even numbers and print it.

# References: 
# https://www.codesdope.com/discussion/take-integer-inputs-from-user-until-heshe-presses-/
# https://careerkarma.com/blog/python-break-and-continue/
# https://www.tutorialspoint.com/python-program-to-print-even-numbers-in-a-list


#empty lists to store inputs
list_01 = []
list_02 = []

#While loop will continue to take inputs until false
while True:
    number = (input('Enter an integer or QUIT to quit: '))
    if number == 'quit':
        break #exits loop
    else:
        list_01.append(int(number)) #adds integer to list_01

for elem in list_01: #iterages through list_01
    if elem % 2 == 0: #checks if number is even
        list_02.append(elem)#even numbers added to list_02

print(list_02)