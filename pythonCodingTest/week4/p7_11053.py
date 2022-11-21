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
# https://st-lab.tistory.com/137

NUMBER_COUNT = int(input())

nums_list = list(map(int, sys.stdin.readline().split()))

dp = [1] * NUMBER_COUNT

for check_idx in range(NUMBER_COUNT):
    for temp_idx in range(check_idx):
        if (
            nums_list[temp_idx] < nums_list[check_idx]
            and dp[check_idx] < dp[temp_idx] + 1
        ):
            dp[check_idx] = dp[temp_idx] + 1

print(max(dp))
