import sys

sys.setrecursionlimit(10**6)

"""
n = input()  #2
a = [sys.stdin.readline() for _ in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

l_val, r_val = list(map(int, sys.stdin.readline().split()))

l_c = 0
r_c = 0

while True:
    if l_val == 1 and r_val == 1:
        break

    if r_val > l_val:
        r_val = r_val - l_val
        r_c += 1
    elif r_val < l_val:
        l_val = l_val - r_val
        l_c += 1

print(l_c, r_c)
