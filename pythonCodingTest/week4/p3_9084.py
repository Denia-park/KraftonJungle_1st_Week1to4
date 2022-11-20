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

# 정답 참조
# https://yabmoons.tistory.com/491


def solve_coin(dp_arr):
    for coin_idx in range(COIN_NUM):
        for money_idx in range(COINS[coin_idx], TARGET_MONEY + 1):
            dp_arr[money_idx] = dp_arr[money_idx] + dp_arr[money_idx - COINS[coin_idx]]


TEST_CASE_NUM = int(input())

for _ in range(TEST_CASE_NUM):
    COIN_NUM = int(input())
    COINS = list(map(int, sys.stdin.readline().split()))
    TARGET_MONEY = int(input())
    dp_arr = [0] * (TARGET_MONEY + 1)
    dp_arr[0] = 1

    solve_coin(dp_arr)
    print(dp_arr[TARGET_MONEY])
