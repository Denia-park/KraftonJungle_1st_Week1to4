import math
import sys

"""
n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

# 투포인터
# https://ansohxxn.github.io/boj/2470/

quiz_num_count = int(input())
quiz_num_list = list(map(int, sys.stdin.readline().split()))
quiz_num_list.sort()

start_cursor = 0
end_cursor = quiz_num_count - 1
answer_list = []

min_sum = math.inf

# 두개의 용액을 선택해야함 (= 같은 용액을 2번 선택하면 안됨)
while start_cursor < end_cursor:
    small_val = quiz_num_list[start_cursor]
    big_val = quiz_num_list[end_cursor]

    sum_val = small_val + big_val

    if sum_val == 0:
        answer_list = [small_val, big_val]
        break
    elif abs(sum_val) < min_sum:
        min_sum = abs(sum_val)
        answer_list = [small_val, big_val]

    if sum_val < 0:
        start_cursor += 1
    else:
        end_cursor -= 1

print(answer_list[0], answer_list[1])

# 이분탐색
# https://latte-is-horse.tistory.com/316

# n = int(input())
# arr = sorted(map(int, input().split()))  # 정렬된 용액들


# def binary_search(s, target):
#     global arr
#     res = n
#     start, end = s, n - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] >= target:
#             res = mid
#             end = mid - 1
#         else:
#             start = mid + 1
#     return res


# def solution():
#     global arr
#     v1, v2 = 0, 0
#     best_sum = 10**10
#     for i in range(n):
#         # 이분 탐색 수행: 현재 위치(i) 이후의 용액에서 탐색, 찾는 값은 (현재 용액 * -1)
#         res = binary_search(i + 1, -arr[i])

#         # 찾은 용액의 왼쪽 용액 확인
#         if i + 1 <= res - 1 < n and abs(arr[i] + arr[res - 1]) < best_sum:
#             best_sum = abs(arr[i] + arr[res - 1])
#             v1, v2 = arr[i], arr[res - 1]

#         # 찾은 용액 확인
#         if i + 1 <= res < n and abs(arr[i] + arr[res]) < best_sum:
#             best_sum = abs(arr[i] + arr[res])
#             v1, v2 = arr[i], arr[res]

#     print(v1, v2)  # i 번째 용액을 확인할 때 i + 1번 용액부터 확인하기 때문에 항상 v1 <= v2 이다.


# solution()
