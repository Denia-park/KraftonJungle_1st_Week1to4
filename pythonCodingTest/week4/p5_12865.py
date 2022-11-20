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
# https://www.acmicpc.net/problem/12865

WEIGHT = 0
VALUE = 1

BAGAGE_NUM, WEIGHT_LIMIT = map(int, sys.stdin.readline().split())

BAGAGE_LIST = [list(map(int, sys.stdin.readline().split())) for _ in range(BAGAGE_NUM)]

dp = [[0] * (WEIGHT_LIMIT + 1) for _ in range(BAGAGE_NUM + 1)]

for cur_weight in range(1, WEIGHT_LIMIT + 1):
    for bagage_idx in range(1, BAGAGE_NUM + 1):
        if cur_weight < BAGAGE_LIST[bagage_idx - 1][WEIGHT]:
            dp[bagage_idx][cur_weight] = dp[bagage_idx - 1][cur_weight]
        else:
            dp[bagage_idx][cur_weight] = max(
                dp[bagage_idx - 1][cur_weight],
                dp[bagage_idx - 1][cur_weight - BAGAGE_LIST[bagage_idx - 1][WEIGHT]]
                + BAGAGE_LIST[bagage_idx - 1][VALUE],
            )

print(dp[BAGAGE_NUM][WEIGHT_LIMIT])
