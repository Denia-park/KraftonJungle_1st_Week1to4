import itertools
import sys

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
n = 2
len_list, quiz_num_list = [
    list(map(int, sys.stdin.readline().split())) for i in range(n)
]

length = len_list[0]


def calculate_list_method(list):
    sum = 0
    for i in range(len(list) - 1):
        cur = list[i]
        next = list[i + 1]

        sum += abs(cur - next)

    return sum


nPr = itertools.permutations(quiz_num_list, length)
per_list = list(nPr)

max_val = -1

for temp_list in per_list:
    rtval = calculate_list_method(temp_list)
    if max_val < rtval:
        max_val = rtval

print(max_val)
