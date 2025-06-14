"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a, 
	and the boundary has the Nth alphabet letter (in alphabetical order).
Function Description
	Complete the rangoli function in the editor below.
rangoli has the following parameters:
	int size: the size of the rangoli
Returns
	string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format
	Only one line of input containing size, the size of the rangoli.
Sample Input
	5
Sample Output
	--------e--------
	------e-d-e------
	----e-d-c-d-e----
	--e-d-c-b-c-d-e--
	e-d-c-b-a-b-c-d-e
	--e-d-c-b-c-d-e--
	----e-d-c-d-e----
	------e-d-e------
	--------e--------
"""


def print_rangoli(size):
    """Prints the RANGOLI pattern of 'size'"""
    
    if (size == 1):
        print("a")
        return
    
    rangoli = []
    for pos in range(1, size+1):
        rangoli_part = ""
        
        for i in range(size-pos):
            rangoli_part += '--'
        for i in range(pos):
            rangoli_part += f"{chr(97+size-i-1)}-"
        rangoli_part += rangoli_part[-4::-1]
        
        rangoli.append(rangoli_part)
    
    rangoli.extend(rangoli[-2::-1])
    print('\n'.join(rangoli))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


"""
Thought Process:
	If the size is 1, we only print "a" because there are no surrounding letters.
    Else,
		Loop from start to the given size.
			Insert the initial '-', apppriopriate number of times, i.e,
				2*(remaining_letters) times.
			Insert the letters in reverse order with '-' as seperator, i.e,
				insert the letters starting from maximum size
			Extend the string by inserting the reversed part of same string,
				excluding the last three characters
			Insert the string in the list
        Extend the list by reinserting the first size-1 string in reverse order
		Print each list element in new line.
"""