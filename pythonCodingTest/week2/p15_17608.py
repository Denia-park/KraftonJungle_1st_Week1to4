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
stick_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]

my_stack = deque()
for i in stick_list:
    my_stack.append(i)

cur_height = stick_list.pop()
count = 1

for _ in range(len(stick_list)):
    stick_height = stick_list.pop()

    if stick_height > cur_height:
        count += 1
        cur_height = stick_height

print(count)
