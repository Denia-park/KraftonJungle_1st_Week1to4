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

# 정답 참조
# https://st-lab.tistory.com/237

A, B, C = list(map(int, sys.stdin.readline().split()))


def divide_pow(base_num, pow_num, mod_num):
    if pow_num == 0:
        return 1
    elif pow_num == 1:
        return base_num % mod_num

    if pow_num % 2 == 0:
        temp_val = divide_pow(base_num, pow_num // 2, mod_num)
        return (temp_val * temp_val) % mod_num
    else:
        pow_num = pow_num - 1
        temp_val = divide_pow(base_num, pow_num // 2, mod_num)
        return ((base_num % mod_num) * temp_val * temp_val) % mod_num


print(divide_pow(A, B, C))
