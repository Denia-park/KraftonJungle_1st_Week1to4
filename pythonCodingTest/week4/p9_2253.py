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


TARGET_NUM, BAN_NUM = list(map(int, sys.stdin.readline().split()))

BAN_LIST = [int(input()) for _ in range(BAN_NUM)]

dp = [0] * 10001

for ban_idx in BAN_LIST:
    dp[ban_idx] = -1

dp[2] = 1

jump_num = 2
jump_num_count = 0

for next_stone in range(3, TARGET_NUM + 1):
    if jump_num_count == jump_num:
        jump_num_count = 0
        jump_num += 1

    dp[next_stone] = jump_num
    jump_num_count += 1


if dp[TARGET_NUM] == 0:
    print(-1)
else:
    print(dp[TARGET_NUM])
