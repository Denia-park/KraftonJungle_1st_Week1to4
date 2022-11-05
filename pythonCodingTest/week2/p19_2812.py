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

n, max_delete_count = list(map(int, sys.stdin.readline().split()))
quiz_num = sys.stdin.readline().rstrip()

my_stack = deque()

start_num = 0
cur_delete_count = 0


def is_empty(my_stack):
    return len(my_stack) <= 0


for cur_num_str in quiz_num:
    cur_num = int(cur_num_str)

    if cur_delete_count >= max_delete_count:
        my_stack.append(cur_num)
        continue

    while True:
        if is_empty(my_stack):
            my_stack.append(cur_num)
            break

        top_data = my_stack.pop()

        if top_data < cur_num:
            cur_delete_count += 1
            if cur_delete_count >= max_delete_count:
                my_stack.append(cur_num)
                break
        else:
            my_stack.append(top_data)
            my_stack.append(cur_num)
            break


my_str = ""
for cur_num in my_stack:
    my_str += str(cur_num)

print(my_str[: len(my_stack) - (max_delete_count - cur_delete_count)])
