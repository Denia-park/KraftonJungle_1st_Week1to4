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

q_r_list.sort()
q_r_list.sort(key=len)

for val in q_r_list:
    print(val)
