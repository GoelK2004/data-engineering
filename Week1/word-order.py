"""
Hackerrank link was not provided.
Counts and displays the number of occurrences of each word while preserving their input order.
"""

if __name__ == "__main__":
	input_str = input()
	inp_list = input_str.split()

	dict = {}
	for word in inp_list:
		if word not in dict:
			dict[word] = inp_list.count(word)
	
	for word, count in dict.items():
		print(f"{word}: {count}")

"""
Thought Process:
	Input string and split it into list with default delimiter, i.e, space(' ')
	Initialise a dictionary to store the word and its occurrence
	Loop over the elements of the list, if the word has not been processed, insert it into the dictionary along with its count.
	Using: List method count()
"""