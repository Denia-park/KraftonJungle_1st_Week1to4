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
# https://st-lab.tistory.com/141

WEIGHT = 0
VALUE = 1

BAGAGE_NUM, WEIGHT_LIMIT = map(int, sys.stdin.readline().split())

BAGAGE_LIST = [list(map(int, sys.stdin.readline().split())) for _ in range(BAGAGE_NUM)]

# BAGAGE_LIST.sort()

dp1 = [0] * (WEIGHT_LIMIT + 1)
dp2 = [0] * (WEIGHT_LIMIT + 1)

# 내꺼 => 중복이 생김 (내가 먼저 계산을 했던 값이 한번 더 들어감)
for bagage_idx in range(1, BAGAGE_NUM + 1):
    for cur_weight in range(BAGAGE_LIST[bagage_idx - 1][WEIGHT], WEIGHT_LIMIT + 1):
        dp1[cur_weight] = max(
            dp1[cur_weight],
            dp1[cur_weight - BAGAGE_LIST[bagage_idx - 1][WEIGHT]]
            + BAGAGE_LIST[bagage_idx - 1][VALUE],
        )

print(dp1[WEIGHT_LIMIT])

# 정답 => 중복이 생길수가 없음 (큰 값부터 처리하기 때문에)
for bagage_idx in range(1, BAGAGE_NUM + 1):
    for cur_weight in range(WEIGHT_LIMIT, BAGAGE_LIST[bagage_idx - 1][WEIGHT] - 1, -1):
        dp2[cur_weight] = max(
            dp2[cur_weight],
            dp2[cur_weight - BAGAGE_LIST[bagage_idx - 1][WEIGHT]]
            + BAGAGE_LIST[bagage_idx - 1][VALUE],
        )

print(dp2[WEIGHT_LIMIT])

"""
확인한 반례
3 6
3 14
2 8
3 9
 
정답: 23
출력: 22
"""