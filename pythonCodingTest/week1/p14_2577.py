import sys

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""
n = 3
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

answer_list = [0 for _ in range(10)]

check_str = 1
for sub_list in q:
    each_num = sub_list[0]
    check_str *= each_num

for i in str(check_str):
    idx = int(i)
    get = answer_list[idx]
    answer_list[idx] = get + 1

for sub_list in answer_list:
    print(sub_list)
