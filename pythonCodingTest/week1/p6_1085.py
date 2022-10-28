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
q = list(map(int, sys.stdin.readline().split()))

x = q[0]
y = q[1]
w = q[2]
h = q[3]

width_list = [x, abs(w - x)]
height_list = [y, abs(h - y)]

print(min(width_list + height_list))
