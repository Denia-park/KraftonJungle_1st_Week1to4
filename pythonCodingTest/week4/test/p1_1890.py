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
dp[0][0] = 1

for row in range(TABLE_SIZE):
    for col in range(TABLE_SIZE):
        jump_num = TABLE[row][col]
        if jump_num == 0:
            continue

        # 아래쪽
        edit_row = row + jump_num
        edit_col = col
        if not is_out_of_table(edit_row, edit_col):
            dp[edit_row][edit_col] += dp[row][col]

        # 오른쪽
        edit_row = row
        edit_col = col + jump_num
        if not is_out_of_table(edit_row, edit_col):
            dp[edit_row][edit_col] += dp[row][col]

print(dp[TABLE_SIZE - 1][TABLE_SIZE - 1])
