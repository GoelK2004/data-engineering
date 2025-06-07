"""
Given an integer, , print the following values for each integer 1 from n to :
	Decimal
	Octal
	Hexadecimal (capitalized)
	Binary
    
Function Description
	Complete the print_formatted function in the editor below.
	print_formatted has the following parameters:
		int number: the maximum value to print
Prints
	The four values must be printed on a single line in the order specified above for each i from 1 to n.
    Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

Input Format
	A single integer denoting .
    
Sample Input
	17
Sample Output
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec_str = str(i).rjust(width)
        oct_str = oct(i)[2:].rjust(width)
        hex_str = hex(i)[2:].upper().rjust(width)
        bin_str = bin(i)[2:].rjust(width)
        print(dec_str, oct_str, hex_str, bin_str)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
"""
Thought Process:
	Python provides bin(), hex() and oct() functions to convert the integer values to binary, hexadecimal and octal values respectively.
    To make the output right aligned, as shown in the above example, we count the max width, which will be equal to binary value of given number.
    Apply the right alignment using method: rjust()
    Convert the letters to uppercase using upper().
    Print the values in a loop for each number.
"""