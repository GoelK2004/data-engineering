"""
Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x amount of money
	only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format
	The first line contains X, the number of shoes.
	The second line contains the space separated list of all the
    	shoe sizes in the shop.
	The third line contains N, the number of customers.
	The next N lines contain the space separated values of the
    	shoe size desired by the customer and x, the price of the shoe.
Output Format
	Print the amount of money earned by Raghu.
Sample Input
	10
	2 3 4 5 6 8 7 6 5 18
	6
	6 55
	6 45
	6 55
	4 40
	18 60
	10 50
Sample Output
	200
Explanation
	Customer 1: Purchased size 6 shoe for $55.
	Customer 2: Purchased size 6 shoe for $45.
	Customer 3: Size 6 no longer available, so no purchase.
	Customer 4: Purchased size 4 shoe for $40.
	Customer 5: Purchased size 18 shoe for $60.
	Customer 6: Size 10 not available, so no purchase.
	Total money earned = 200
"""


from collections import Counter

total_shoes = int(input())
shoe_sizes = input()
customers = int(input())
shoe_desired = []
for i in range(customers):
    desired = input()
    to_append = desired.split()
    to_append[0] = int(to_append[0])
    to_append[1] = int(to_append[1])
    shoe_desired.append(to_append)

shoe_sizes = [int(shoe) for shoe in shoe_sizes.split()]
total_earned = 0
inventory = Counter(shoe_sizes)

for shoe in shoe_desired:
    if (inventory[shoe[0]] > 0):
        total_earned += shoe[1]
        inventory[shoe[0]] -= 1

print(total_earned)


"""
Thought Process:
	Input all the necessary information.
    Convert the strings into their corresponding list with int data type.
    Apply Counter class to convert the shoe_sizes list into:
		Corresponding dictionary with count of each shoe size
    Traverse the customer desired shoe size:
		If present, increment the earnings and decrement the inventory.
    Print the total earned.
"""