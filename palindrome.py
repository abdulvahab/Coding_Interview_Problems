#!/usr/bin/env python
'''This script detect if given string is palindrome or not
Authoured By :Abdulvahab Kharadi
Date: 20/07/2018'''

string = input('Enter your string: ')            # get user string
length = len(string)                             # calculate length
result = ''
for i in range(0, length // 2):                  # loop through string to check for mismatch
    # comapre letter from front and back untill you reach in the middle
    if string[i] != string[length-(i+1)]:
        # as soon as you found a mismatch exit with print
        print(f"'{string}' is not a palindrome")
        break
else:
    # if you survive through loop you are palindrome
    print(f"'{string}' is a palindrome")


    
