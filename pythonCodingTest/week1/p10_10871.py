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
n = 2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

answer_list = []
for i in q[1]:
    if i < q[0][1]:
        print(i, end=" ")