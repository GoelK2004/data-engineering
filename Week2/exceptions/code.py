"""
Task
You are given two values a and b.
Perform integer division and print a/b.

Input Format
	The first line contains T, the number of test cases.
	The next  lines each contain the space separated values of a and b.
Output Format
	Print the value of a/b.
	In the case of ZeroDivisionError or ValueError, print the error code.
Sample Input
	3
	1 0
	2 $
	3 1
Sample Output
	Error Code: integer division or modulo by zero
	Error Code: invalid literal for int() with base 10: '$'
	3

Note: For integer division in Python 3 use //.
"""


number_test_cases = int(input())
cases = []
for it in range(number_test_cases):
    try:
        nums = input()
        num1, num2 = [int(num) for num in nums.split()]
        print(num1//num2)
    except Exception as e:
        print(f"Error Code: {e}")
        

"""
Thought Process:
	Use try-except block,
    Input the number. Extract numbers from input and print answer.
	If error found, print the error code.
"""