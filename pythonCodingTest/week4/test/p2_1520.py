import sys

sys.setrecursionlimit(10**9)
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

dp = [[-1] * COL for _ in range(ROW)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(row, col):

    if row == ROW - 1 and col == COL - 1:
        return 1

    if dp[row][col] != -1:
        return dp[row][col]

    dp[row][col] = 0

    for direc in directions:
        edit_row = row + direc[0]
        edit_col = col + direc[1]

        if is_out_of_table(edit_row, edit_col):
            continue

        if TABLE[row][col] > TABLE[edit_row][edit_col]:
            if dp[edit_row][edit_col] == -1:
                dp[row][col] += dfs(edit_row, edit_col)
            else:
                dp[row][col] += dp[edit_row][edit_col]

    return dp[row][col]


dfs(0, 0)

print(dp[0][0])
