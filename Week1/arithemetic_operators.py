"""
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Example
    a = 3
    b = 5

Print the following:
	8
	-2
	15
"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a+b}")
    print(f"{a-b}")
    print(f"{a*b}")

"""
Thought Process:
    Take two number as input.
    Print their sum, difference and product.
"""