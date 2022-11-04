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

n = 4
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

list_len = q[0][0]
q[1].sort()
num_list = q[1]
check_num_list_len = q[2][0]
check_num_list = q[3]


# def bin_search(list, key):
#     pl = 0
#     pr = len(list) - 1

#     while True:
#         pc = (pl + pr) // 2

#         center_val = list[pc]

#         if center_val == key:
#             return 1
#         elif center_val < key:
#             pl = pc + 1
#         elif center_val > key:
#             pr = pc - 1

#         if pl > pr:
#             break

#     return 0


for key in check_num_list:
    try:
        temp_idx = num_list.index(key)
        print(1)
    except ValueError:
        print(0)
