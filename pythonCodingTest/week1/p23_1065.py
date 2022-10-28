import sys
import math

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
q = [sys.stdin.readline() for i in range(n)]  
# q = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""

# 한수
# https://ooyoung.tistory.com/65


def is_hansu(num):
    if num < 100:
        return True

    num_list = list(map(int, str(num)))

    if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        return True


n = int(input())

count = 0

for i in range(1, n + 1):
    if is_hansu(i):
        count += 1

print(count)
