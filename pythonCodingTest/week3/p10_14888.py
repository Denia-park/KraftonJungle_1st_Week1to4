from collections import deque
import math
import sys

sys.setrecursionlimit(10**6)

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

NUMBER_NUM = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
operartors_counts = list(map(int, sys.stdin.readline().split()))

my_numbers_deque = deque()
for value in numbers:
    my_numbers_deque.append(value)

default_op = ["+", "-", "*", "//"]
operators = []
visited = [False] * (NUMBER_NUM - 1)

for idx, count in enumerate(operartors_counts):
    op = default_op[idx]
    for _ in range(count):
        operators.append(op)

# plus_num, minus_num, multiply_num, divide_num
def calculate_q(original_q):
    global answer, my_numbers_deque

    my_q = original_q.copy()
    temp_numbers_deque = my_numbers_deque.copy()

    while len(temp_numbers_deque) != 1:
        value1 = temp_numbers_deque.popleft()
        value2 = temp_numbers_deque.popleft()
        operator = my_q.popleft()

        if operator == "+":
            temp_value = value1 + value2
        elif operator == "-":
            temp_value = value1 - value2
        elif operator == "*":
            temp_value = value1 * value2
        elif operator == "//":
            if (value1 / value2) <= 0:
                temp_value = math.ceil(value1 / value2)
            else:
                temp_value = math.floor(value1 / value2)

        temp_numbers_deque.appendleft(temp_value)

    return temp_numbers_deque.popleft()


def dfs(my_q):
    global answer

    if len(my_q) == (NUMBER_NUM - 1):
        answer.append(calculate_q(my_q))
        return

    for cur_op_idx in range(len(operators)):
        if not visited[cur_op_idx]:
            visited[cur_op_idx] = True
            my_q.append(operators[cur_op_idx])
            dfs(my_q)
            visited[cur_op_idx] = False
            my_q.pop()


my_q = deque()
answer = []
dfs(my_q)

answer.sort()

print(answer[-1])
print(answer[0])
