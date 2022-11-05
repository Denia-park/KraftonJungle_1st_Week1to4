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
tower_list = list(map(int, sys.stdin.readline().split()))

answer_list = ["0"] * n
for i in range(len(tower_list) - 1, -1, -1):
    cur_tower_height = tower_list[i]
    for j in range(i - 1, -1, -1):
        if tower_list[j] >= cur_tower_height:
            answer_list[i] = str(j + 1)
            break

print(" ".join(answer_list))
