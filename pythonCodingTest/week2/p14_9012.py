from collections import deque
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

n = int(input())  # 2
braket_str_list = [sys.stdin.readline().rstrip() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

my_stack = deque()

for braket_str in braket_str_list:
    check_flag = True
    my_stack.clear()

    for braket in braket_str:
        if len(my_stack) == 0:
            my_stack.append(braket)
        elif braket == "(":
            my_stack.append(braket)
        elif braket == ")":
            if len(my_stack) == 0:
                check_flag = False
                break
            else:
                my_peek_data = my_stack.pop()
                if my_peek_data != "(":
                    check_flag = False
                    break

    if check_flag == True and len(my_stack) == 0:
        print("YES")
    else:
        print("NO")
