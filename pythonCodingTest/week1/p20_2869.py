import sys
import math

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
n = list(map(int, sys.stdin.readline().split()))

A = n[0]
B = n[1]
V = n[2]

print(math.ceil((V - B) / (A - B)))

"""
cur_height = 0
count = 0

while True :
    cur_height += A
    if(cur_height > V):
        break
    else :
        cur_height -= B
    
    count += 1

print(count)
"""

"""
x일 기준
달팽이가 올라갈 수 있는 최대 높이 : x*A - (x-1)*B
"""
