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


def dfs(left_val, right_val, l_count, r_count):
    if left_val > L or right_val > R:
        return
    elif left_val == L and right_val == R:
        print(l_count, r_count)
        return

    if left_val + right_val > max(L, R):
        return

    dfs(left_val + right_val, right_val, l_count + 1, r_count)
    dfs(left_val, left_val + right_val, l_count, r_count + 1)


L, R = list(map(int, sys.stdin.readline().split()))

init_count = 0

dfs(1, 1, init_count, init_count)
