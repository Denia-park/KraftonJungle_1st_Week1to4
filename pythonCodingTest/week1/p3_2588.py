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

n = 2
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

num1 = a[0][0]
num2 = a[1][0]

for eachNum in str(num2)[::-1]:
    print(num1 * int(eachNum))

print(num1 * num2)
