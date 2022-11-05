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


class FixedStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.cursor = 0

    def get_size(self):
        return self.cursor

    def is_empty(self):
        return self.cursor <= 0

    def is_full(self):
        return self.cursor >= self.size

    def push(self, value):
        if self.is_full():
            return -1

        self.stack[self.cursor] = value
        self.cursor += 1
        return 0

    def pop(self):
        if self.is_empty():
            return -1

        self.cursor -= 1
        return self.stack[self.cursor]

    def top(self):
        if self.is_empty():
            return -1

        return self.stack[self.cursor - 1]


n = int(input())  # 2
command_list = [sys.stdin.readline().rstrip() for i in range(n)]
# a = ["1 2 3", "4 5 6"]

my_stack = FixedStack(100000)

for command in command_list:

    command_split_list = command.split()

    if command_split_list[0] == "push":
        my_stack.push(command_split_list[1])

    elif command_split_list[0] == "pop":
        print(my_stack.pop())

    elif command_split_list[0] == "size":
        print(my_stack.get_size())

    elif command_split_list[0] == "empty":
        if my_stack.is_empty():
            print(1)
        else:
            print(0)

    elif command_split_list[0] == "top":
        print(my_stack.top())
