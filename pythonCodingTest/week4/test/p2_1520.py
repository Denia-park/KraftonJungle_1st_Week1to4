from collections import deque
import sys

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


def is_out_of_table(row, col):
    return row < 0 or row >= ROW or col < 0 or col >= COL


ROW, COL = map(int, sys.stdin.readline().split())
TABLE = [list(map(int, sys.stdin.readline().split())) for _ in range(ROW)]

my_que = deque()

my_que.append((0, 0))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

count = 0

while my_que:
    c_r, c_c = my_que.popleft()

    if c_r == ROW - 1 and c_c == COL - 1:
        count += 1
        continue

    # 오른쪽 , 아래쪽
    for move_direc in range(len(directions)):
        e_r = c_r + directions[move_direc][0]
        e_c = c_c + directions[move_direc][1]

        if is_out_of_table(e_r, e_c):
            continue

        cur_height = TABLE[c_r][c_c]
        next_height = TABLE[e_r][e_c]

        if cur_height > next_height:
            my_que.append((e_r, e_c))


print(count)
