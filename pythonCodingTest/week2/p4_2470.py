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
# https://ansohxxn.github.io/boj/2470/

quiz_num_count = int(input())
quiz_num_list = list(map(int, sys.stdin.readline().split()))
quiz_num_list.sort()

start_cursor = 0
end_cursor = quiz_num_count - 1
answer_list = []

min_sum = 10_000_000

while start_cursor <= end_cursor:
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
