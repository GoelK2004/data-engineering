"""You are given a string S.
Your task is to find out whether S is a valid regex or not.
Input Format
	The first line contains integer , the number of test cases.
	The next  lines contains the string .
Output Format
	Print "True" or "False" for each test case without quotes.
Sample Input
	2
	.*\+
	.*+
Sample Output
	True
	False
Explanation
	.*\+ : Valid regex.
	.*+: Has the error multiple repeat. Hence, it is invalid.
"""


import re

n = int(input())
for _ in range(n):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)


"""
Thought Process:
	Take the input in each iteration,
    Check if it valid pettern using re.compile.
    If compilation is successfull we can safely print True.
    If error is raised, means pattern is incorrect. Print False
    
    NOTE: If you type .*+ directly in your terminal,
    	  Python reads it exactly as you typed it,
          and re.compile(".*+") will not raise an error — because,
          .*+ is actually valid in Python's regex engine.
          
          Error used to be true in older versions of Python (pre-3.6).
          But now, in modern versions (3.6+), Python accepts .*+ as a valid regex. It means:
		  match 1 or more of any character, as greedily as possible.
          
          If you are using Python 2, use raw_input() instead of input().
"""