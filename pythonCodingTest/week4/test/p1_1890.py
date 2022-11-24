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
    return row < 0 or row >= TABLE_SIZE or col < 0 or col >= TABLE_SIZE


TABLE_SIZE = int(input())

TABLE = [list(map(int, sys.stdin.readline().split())) for _ in range(TABLE_SIZE)]

dp = [[0] * TABLE_SIZE for _ in range(TABLE_SIZE)]

my_que = deque()

my_que.append((0, 0))

directions = [(0, 1), (1, 0)]

while my_que:
    c_r, c_c = my_que.popleft()
    jump_num = TABLE[c_r][c_c]

    # 오른쪽 , 아래쪽
    for move_direc in range(2):
        e_r = c_r + jump_num * directions[move_direc][0]
        e_c = c_c + jump_num * directions[move_direc][1]

        if is_out_of_table(e_r, e_c):
            continue

        if jump_num != 0:
            dp[e_r][e_c] += 1
            my_que.append((e_r, e_c))


print(dp[TABLE_SIZE - 1][TABLE_SIZE - 1])
