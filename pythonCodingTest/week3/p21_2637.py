from collections import deque
import sys

sys.setrecursionlimit(10**6)

"""
n = input()  #2
a = [sys.stdin.readline() for _ in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

FINISH_NUM = int(input())
LINE_NUM = int(input())

part_data_infos = [[] for _ in range(FINISH_NUM + 1)]
# answer = [[0] * (FINISH_NUM + 1) for _ in range(FINISH_NUM + 1)]
answer = [0] * (FINISH_NUM + 1)

mid_part_min = 101
for _ in range(LINE_NUM):
    PART_NUM, ORIGIN_PART_NUM, NEED_NUM = list(map(int, sys.stdin.readline().split()))
    mid_part_min = min(PART_NUM, mid_part_min)
    part_data_infos[PART_NUM].append((ORIGIN_PART_NUM, NEED_NUM))

for info in part_data_infos[FINISH_NUM]:
    temp_part_num, temp_need_num = info
    answer[temp_part_num] += temp_need_num

for idx in range(FINISH_NUM - 1, mid_part_min - 1, -1):
    while answer[idx] > 0:
        answer[idx] -= 1
        for info in part_data_infos[idx]:
            temp_part_num, temp_need_num = info
            answer[temp_part_num] += temp_need_num

for idx in range(1, mid_part_min):
    print(f"{idx} {answer[idx]}")
