"""
Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of
	all the plants with distinct heights in her greenhouse.
Function Description
	Complete the average function in the editor below.
average has the following parameters:
	int arr: an array of integers
Returns
	float: the resulting float value rounded to 3 places after the decimal
Input Format
	The first line contains the integer, N, the size of arr.
	The second line contains the N space-separated integers, arr[i].
Sample Input
	STDIN                                    Function
	-----                                    --------
	10                                       arr[] size N = 10
	161 182 161 154 176 170 167 171 170 174  arr = [161, 181, ..., 174]
Sample Output
	169.375
"""


def average(array):
    # your code goes here
    
    height_set = set(array)
    total_distinct_heights = len(height_set)
    sum_heights = 0
    
    for height in height_set:
        sum_heights += height
    
    return float(sum_heights) / total_distinct_heights

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


"""
Thought Process:
	We first convert the array into a set using set() constructor.
	Store the total elements present in the set.
    Loop over the elements in the set to sum distinct heights.
    Return average.
"""