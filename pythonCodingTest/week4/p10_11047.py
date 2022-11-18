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

COIN_NUM, NEED_MONEY = list(map(int, sys.stdin.readline().split()))
COINS = [int(sys.stdin.readline().rstrip()) for _ in range(COIN_NUM)]

min_count = 0
check_money = NEED_MONEY

for idx in range(COIN_NUM - 1, -1, -1):
    cur_coin_val = COINS[idx]
    while check_money >= cur_coin_val:
        min_count += check_money // cur_coin_val
        check_money = check_money % cur_coin_val

print(min_count)
