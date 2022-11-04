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

quiz_num_list.sort()

count = 1


def bin_search_upper(list, start, key):
    end = len(list) - 1
    return_idx = -1

    while start <= end:
        mid = (start + end) // 2
        mid_val = list[mid]

        if mid_val > key:
            return_idx = mid
            end = mid - 1
        else:
            start = mid + 1

    return return_idx


start_cursor = 0
temp_min_val = quiz_num_list[0]

while True:
    search_idx = bin_search_upper(quiz_num_list, start_cursor, temp_min_val)

    if search_idx == -1:
        print(count)
        break
    else:
        start_cursor = search_idx
        temp_min_val = quiz_num_list[search_idx]
        count += 1
