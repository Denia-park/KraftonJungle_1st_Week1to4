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

# 정답 참고
# https://ddiyeon.tistory.com/72

n = int(input())
mat = [tuple(map(int, input().split())) for i in range(n)]

dp = [[0] * n for i in range(n)]
for cnt in range(n - 1):
    for i in range(n - 1 - cnt):
        j = i + cnt + 1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j], dp[i][k] + dp[k + 1][j] + mat[i][0] * mat[k][1] * mat[j][1]
            )
print(dp[0][-1])
