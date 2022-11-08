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

# 정답 코드 참조
# https://1-7171771.tistory.com/71

n = int(input())  # 2
tower_list = list(map(int, sys.stdin.readline().split()))

answer = [0] * n

front_tower_stack = list()

for cur_tower_idx, cur_tower_height in enumerate(tower_list):
    while front_tower_stack:
        pre_tower = front_tower_stack[-1]
        pre_tower_idx = pre_tower[0]
        pre_tower_height = pre_tower[1]

        if pre_tower_height < cur_tower_height:
            front_tower_stack.pop()
        else:
            answer[cur_tower_idx] = str(pre_tower_idx + 1)
            front_tower_stack.append((cur_tower_idx, cur_tower_height))
            break

    if not front_tower_stack:
        answer[cur_tower_idx] = "0"
        front_tower_stack.append((cur_tower_idx, cur_tower_height))

print(" ".join(answer))
