"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format
The input consists of three lines. The first line contains the integer N, denoting the length of the list.
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format
Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.
"""

from itertools import combinations

if __name__ == "__main__":
    _ = input()
    list_char = input()
    n_group = int(input())
    list_char = list_char.split()
    
    count = 0
    total = 0
    for group in combinations(list_char, n_group):
        total += 1
        if 'a' in group:
            count += 1
    
    print(count/total)
    
"""
itertools.combinations(iterable, r)
	Return r length subsequences of elements from the input iterable.
Source: https://docs.python.org/3/library/itertools.html#itertools.combinations

Thought Process:
	Take input, split it into list using default space(' ') delimiter.
    Create combinations of every element present in the list in groups of K.
    If 'a' is present in the group increment the count.
    At the end, return average.
"""