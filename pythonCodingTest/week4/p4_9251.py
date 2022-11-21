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
# https://st-lab.tistory.com/139

STR_1 = input()
STR_2 = input()

dp = [[0] * (len(STR_1) + 1) for _ in range(len(STR_2) + 1)]

for row in range(1, len(STR_2) + 1):
    for col in range(1, len(STR_1) + 1):
        if STR_2[row - 1] == STR_1[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[len(STR_2)][len(STR_1)])
