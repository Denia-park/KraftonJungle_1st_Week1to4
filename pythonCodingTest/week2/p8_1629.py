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

A, B, C = list(map(int, sys.stdin.readline().split()))

new_A = A
multiply_count = 0
while multiply_count < B:
    new_A *= A
    multiply_count += 1

    new_A %= C

print(new_A)
