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

n, k = list(map(int, sys.stdin.readline().split()))
quiz_num = sys.stdin.readline().rstrip()

my_stack = deque()

start_num = 0
delete_num = 0
for num_str in quiz_num:
    num = int(num_str)

    if delete_num >= k:
        my_stack.append(num)
        continue

    while True:
        if len(my_stack) != 0:
            top_data = my_stack.pop()
            if top_data < num:
                delete_num += 1
                if delete_num >= k:
                    my_stack.append(num)
                    break
                else:
                    continue
            else:
                my_stack.append(top_data)
                my_stack.append(num)
                break
        else:
            my_stack.append(num)
            break

my_str = ""
for num in my_stack:
    my_str += str(num)

print(my_str[: len(my_stack) - (k - delete_num)])
