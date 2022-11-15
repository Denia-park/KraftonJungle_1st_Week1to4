from collections import deque
import math
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

# 정답 코드 참조
# https://st-lab.tistory.com/121

# 처음에 직접 dfs로 풀기는 했으나 계속해서 시간초과가 나서
# 정답을 확인함.

# 계산 과정을 따로 함수로 처리했더니 시간이 오래걸린 것 같다.
# 해결 방법 (둘 다 적용하거나 한개만 적용하거나 자유롭게)
# 1. dfs를 for문 대신에 4개로 분리하거나
# 2. 매개변수로 넘길때 계산을 하고 넘기는게 훨씬 빠르다.


def dfs_2(cur_val, deepth):
    global max_val, min_val

    if deepth == (NUMBER_NUM - 1):
        max_val = max(max_val, cur_val)
        min_val = min(min_val, cur_val)
        return

    for idx in range(4):
        if operartors_counts[idx] == 0:
            continue

        operartors_counts[idx] -= 1

        if idx == 0:  # +
            dfs_2(cur_val + numbers[deepth + 1], deepth + 1)
        elif idx == 1:  # -
            dfs_2(cur_val - numbers[deepth + 1], deepth + 1)
        elif idx == 2:  # *
            dfs_2(cur_val * numbers[deepth + 1], deepth + 1)
        elif idx == 3:  # //
            if cur_val / numbers[deepth + 1] < 0:
                dfs_2(math.ceil(cur_val / numbers[deepth + 1]), deepth + 1)
            else:
                dfs_2(math.floor(cur_val / numbers[deepth + 1]), deepth + 1)

        operartors_counts[idx] += 1


NUMBER_NUM = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
operartors_counts = list(map(int, sys.stdin.readline().split()))
max_val = -(10**9)
min_val = 10**9

dfs_2(numbers[0], 0)

print(max_val)
print(min_val)
