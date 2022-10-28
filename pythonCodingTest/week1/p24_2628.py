import sys
import math

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
q = [sys.stdin.readline() for i in range(n)]  
# q = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""

# 백준 2628 종이자르기 (파이썬)
# https://velog.io/@shon4bw/%EB%B0%B1%EC%A4%80-2628-%EC%A2%85%EC%9D%B4%EC%9E%90%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

width_height = list(map(int, sys.stdin.readline().split()))
n = int(input())
cutting = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

width = width_height[0]
height = width_height[1]

row_cut_list = [0, height]
col_cut_list = [0, width]

# 0 : 가로 , 1 : 세로
CUT_HORIZONTAL = 0
CUT_VERTICAL = 1

for cut_elem in cutting:
    row_col_flag = cut_elem[0]
    cut_coordi = cut_elem[1]

    if row_col_flag == CUT_HORIZONTAL:
        row_cut_list.append(cut_coordi)
    else:
        col_cut_list.append(cut_coordi)

row_cut_list.sort()
col_cut_list.sort()

max_width = 0
max_height = 0

for idx in range(len(row_cut_list) - 1):
    temp_height = row_cut_list[idx + 1] - row_cut_list[idx]
    if temp_height > max_height:
        max_height = temp_height

for idx in range(len(col_cut_list) - 1):
    temp_width = col_cut_list[idx + 1] - col_cut_list[idx]
    if temp_width > max_width:
        max_width = temp_width

print(max_width * max_height)
