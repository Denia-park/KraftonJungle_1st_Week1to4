import sys

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
problem = sys.stdin.readline().rstrip()

min_val = 0

temp_save_char = ""
minus_flag = False


def calculate_value(minus_flag):
    global min_val

    if minus_flag:
        min_val -= int(temp_save_char)
    else:
        min_val += int(temp_save_char)


for each_char in problem:
    if each_char == "-":
        calculate_value(minus_flag)
        minus_flag = True
        temp_save_char = ""

    elif each_char == "+":
        calculate_value(minus_flag)

        temp_save_char = ""
    else:
        temp_save_char += each_char


calculate_value(minus_flag)

print(min_val)
