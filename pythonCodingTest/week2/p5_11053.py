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

quiz_num_count = int(input())
quiz_num_list = list(map(int, sys.stdin.readline().split()))


def bin_search_left(list, key):
    start = 0
    end = len(list)

    while start < end:
        mid = (start + end) // 2
        mid_val = list[mid]

        if mid_val >= key:
            end = mid
        else:
            start = mid + 1

    return end


answer_list = [quiz_num_list[0]]

for i in range(1, len(quiz_num_list)):
    cur_val = quiz_num_list[i]
    if answer_list[-1] < cur_val:
        answer_list.append(cur_val)
    else:
        change_idx = bin_search_left(answer_list, cur_val)
        answer_list[change_idx] = cur_val

print(len(answer_list))
