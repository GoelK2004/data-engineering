"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
For a better understanding of the problem, check the explanation.
Input Format
	A single line of input consisting of the string .
Output Format
	A single line of output consisting of the modified string.

Sample Input
	1222311
Sample Output
	(1, 1) (3, 2) (1, 3) (2, 1)
"""

from itertools import groupby

if __name__ == "__main__":
    string = input()

    str_format = ""

    for key, group in groupby(string):
        str_format += f"({len(list(group))}, {int(key)}) "

    print(str_format)
    
"""
Thought Process:
	Take the string input.
    Iterate over the input using groupby() that returns the list of element with length as the number of times it is being repeated consecutively.
    Format the new string with the total consecutive length and the character being repeated.
"""