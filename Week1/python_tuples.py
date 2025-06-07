"""
Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers.
Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format
	The first line contains an integer, n, denoting the number of elements in the tuple.
	The second line contains n space-separated integers describing the elements in tuple .

Output Format
	Print the result of hash(t).

Sample Input 0
	2
	1 2
Sample Output 0
	3713081631934410656
"""

if __name__ == '__main__':
	# Enter your code here. Read input from STDIN. Print output to STDOUT
	total = input()
	list_int = input()
	list_int = [int(i) for i in list_int.split()]
	int_tuple = tuple(list_int)

	print(hash(int_tuple))

"""
NOTE: The hash() function in Python does not always return the same value for the same key across different executions of the program.
This behavior is due to a security feature called "hash randomization", which was introduced in Python 3.3.

Thought Process:
	Take input. Create the list of numbers using split() function using default delimiter(' ').
	Convert the elements to integers(as input is taken in the form of string).
	Convert into tuple using function: tuple()
	Print hash value.
"""