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
    q_list.append(input())
# q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

q_list_set = set(q_list)
q_r_list = list(q_list_set)


def voca_compare(a, b):
    if len(a) != len(b):
        return 0

    a_list = [a_v for a_v in a]
    b_list = [b_v for b_v in b]

    for i in range(len(a_list)):
        if ord(a_list[i]) > ord(b_list[i]):
            return 1
        elif ord(a_list[i]) < ord(b_list[i]):
            return -1
    else:
        return 0


def qsort(list, left, right):
    pl = left
    pr = right
    pivot_value = len(list[(left + right) // 2])

    while pl <= pr:
        while len(list[pl]) < pivot_value:
            pl += 1
        while len(list[pr]) > pivot_value:
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


quick_sort(q_r_list, 0, len(q_r_list))

change = 1
while change != 0:
    change = 0
    for i in range(len(q_r_list) - 1):
        flag = voca_compare(q_r_list[i], q_r_list[i + 1])
        if flag == 1:
            q_r_list[i], q_r_list[i + 1] = q_r_list[i + 1], q_r_list[i]
            change = 1

for val in q_r_list:
    print(val)
