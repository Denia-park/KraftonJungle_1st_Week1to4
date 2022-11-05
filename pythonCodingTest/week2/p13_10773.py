from collections import deque
import sys

"""
n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

n = int(input())  # 2
command_list = [sys.stdin.readline().rstrip() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

my_stack = deque()

for command in command_list:

    if command == "0":
        my_stack.pop()
    else:
        my_stack.append(int(command))

print(sum(my_stack))
