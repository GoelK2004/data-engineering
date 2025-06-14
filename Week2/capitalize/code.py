"""
You are asked to ensure that the first and last names of people begin
	with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
Input Format
	A single line of input containing the full name, S.
Constraints
	The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized.
	Example 12abc when capitalized remains 12abc.
Output Format
	Print the capitalized string, S.

Sample Input
	chris alan
Sample Output
	Chris Alan
"""


import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ""
    new_word = True
    
    for char in s:
        if char.isspace():
            new_word = True
            result += " "
        elif new_word:
            result += char.capitalize()
            new_word = False
        else:
            result += char
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)

    fptr.write(result + '\n')
    fptr.close()



"""
Thought Process:
    We can use the capitalize() function 
    However, it capitalize the first letter of the whole string.
    We can use the title() built-in function in place of capitalize().
    It capitalizes first letter of each word.
    However, it makes 12g to 12G, which is not the expected output.
    
    Therefore, we manually loop over the string.
    The first letter of each word is capitalized using capitalize()
    Insert the characters in a new string.
    Return the string.
"""