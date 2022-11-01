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

n = int(input())  # 2
q_list = []
for _ in range(n):
    q_list.append(int(input()))
# q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]


def qsort(list, left, right):
    pl = left
    pr = right
    pivot_value = list[(left + right) // 2]

    while pl <= pr:
        while list[pl] < pivot_value:
            pl += 1
        while list[pr] > pivot_value:
            pr -= 1

        if pl <= pr:
            list[pl], list[pr] = list[pr], list[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(list, left, pr)

    if pl < right:
        qsort(list, pl, right)


def quick_sort(list, start_idx, leghth):
    qsort(list, start_idx, leghth - 1)


quick_sort(q_list, 0, len(q_list))
for val in q_list:
    print(val)
