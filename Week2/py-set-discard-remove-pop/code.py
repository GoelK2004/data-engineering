"""
Tasks described in task_part1.png and task_part2.png
"""


n = int(input())
s = set(map(int, input().split()))
number_commands = int(input())
for _ in range(number_commands):
    command = input().split()
    if command[0] == "remove" and int(command[1]) in s:
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
    elif len(s):
        s.pop()

print(sum(s))


"""
Thought Process:
	Input the total number of commands.
    For each command, check if it is remove, discard or pop.
    If it is command, check if number is present in set to avoid error.
    If it is pop, check if set is empty or not, to avoid error.
    Execute the operation.
    Print the sum of the set.
"""