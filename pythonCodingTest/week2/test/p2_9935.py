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

my_stack = []

n = 2  # 2
total_str, boom_str = [sys.stdin.readline().rstrip() for i in range(n)]

for each_str in total_str:
    my_stack.append(each_str)

    temp_idx_count = 0
    temp_count = 0

    for j in range(len(boom_str) - 1, -1, -1):
        stack_len = len(my_stack) - 1

        if stack_len - temp_idx_count < 0:
            break

        if my_stack[stack_len - temp_idx_count] != boom_str[j]:
            break

        temp_count += 1
        temp_idx_count += 1

    if temp_count == len(boom_str):
        for _ in range(len(boom_str)):
            my_stack.pop()

if not my_stack:
    print("FRULA")

print("".join(my_stack))
