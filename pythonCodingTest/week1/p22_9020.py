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

# https://yoonsang-it.tistory.com/31

# 에라토스테네스의 체
def get_prime_list(num):
    check_prime_list = [False, False] + [True] * (num - 1)

    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if check_prime_list[i]:
            for j in range(i + i, num + 1, i):
                check_prime_list[j] = False

    return check_prime_list


n = int(input())
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

check_prime_list = get_prime_list(10000)

for sub_list in q:
    num = sub_list[0]

    prime1 = num // 2
    prime2 = prime1

    while True:
        if check_prime_list[prime1] and check_prime_list[prime2]:
            print(f"{prime1} {prime2}")
            break

        prime1 -= 1
        prime2 += 1
