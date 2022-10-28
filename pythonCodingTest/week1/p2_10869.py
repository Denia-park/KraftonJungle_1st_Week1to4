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

a = list(map(int, sys.stdin.readline().split()))

A = a[0]
B = a[1]

print(A + B)
print(A - B)
print(A * B)
print(A // B)  # 정수 나누기가 필요함
print(A % B)
