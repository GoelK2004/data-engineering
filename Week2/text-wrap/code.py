"""
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
Function Description
	Complete the wrap function in the editor below.
wrap has the following parameters:
	string string: a long string
	int max_width: the width to wrap to
Returns
	string: a single string with newline characters ('\n') where the breaks should be
Input Format
	The first line contains a string, string.
	The second line contains the width, max_width.
Sample Input 0
	ABCDEFGHIJKLIMNOQRSTUVWXYZ
	4
Sample Output 0
	ABCD
	EFGH
	IJKL
	IMNO
	QRST
	UVWX
	YZ
"""


import textwrap

def wrap(string, max_width):
    """Uses the manual approach to implements the learnt string methods"""
    
    string_array = list(string)
    pos = 0
    total_characters = len(string_array)
    
    while pos < total_characters:
        string_array.insert(max_width + pos, '\n')
        pos += max_width + 1
        
    return ''.join(string_array)


def wrap_textwrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


"""
Thought Process:
	We were asked to use the textwrap library.
    It is implemented in the wrap_textwrap function().
    It uses the fill() method provided in textwrap library.
    
    Since, we also learned the string and lists in python,
    I tried manual approach as well.
    First convert the string to python lists.
    Insert newline after max_width position iteratively using insert().
    Convert it back to string.
    Return the new string.
"""