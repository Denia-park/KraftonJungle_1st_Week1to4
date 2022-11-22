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
# https://rccode.tistory.com/155

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    nums = list(map(int, input().split()))
    for _ in range(N - 1):
        _, c = map(int, input().split())
        nums.append(c)

    # DP
    dp = [[0] * N for _ in range(N)]
    for d in range(1, N):
        for i in range(N - d):
            j = i + d

            dp[i][j] = float("inf")
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1],
                )

    print(dp[0][-1])
