"""
Task defined in task_part1.png, task_part2.png, task_part3.png
"""


def merge_the_tools(string, k):
    # your code goes here
    
    kth_strings = []
    pos = 0
    
    while pos < len(string):
        kth_strings.append(string[pos:pos+k])
        pos += k
          
    for pos in range(len(kth_strings)):
        str_new = ""
        for char in kth_strings[pos]:
            if char not in str_new:
                str_new += char
        kth_strings[pos] = str_new
    
    print('\n'.join(kth_strings))
                
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


"""
Thought Process:
	Split the string into k substring and insert them in a list.
    For each substring in the list, create a new string,
		with unique elements in the order they appear.
    Replace the string with new string
    Print the list elements in new line.

    Not used set because it is unordered,
        it can change the order of elements internally.
"""