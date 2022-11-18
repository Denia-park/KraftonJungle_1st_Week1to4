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

n = int(input())

dp = [0] * (n + 1)

if n == 1 or n == 2:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1

    for idx in range(3, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

    print(dp[n])
