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

n = 2
q = [sys.stdin.readline() for i in range(n)]

num_list = list(map(int, q[1].split()))

count = 0

# 에라토스테네스의 체
def is_prime_num(num):
    if num == 1:
        return False

    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


for i in num_list:
    if is_prime_num(i):
        count += 1

print(count)
