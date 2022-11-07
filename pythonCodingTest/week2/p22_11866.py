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


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity):
        self.capacity = capacity  # 큐의 크기
        self.no = 0  # 현재 데이터 개수
        self.front_cursor = 0  # 큐의 맨 앞 원소 커서
        self.rear_cursor = 0  # 큐의 맨 끝 원소 커서
        self.queue = [None] * capacity  # 큐의 본체

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def get_size(self):
        return self.no

    def push(self, value):
        if self.is_full():
            return -1
            # raise FixedQueue.Full  # 큐가 가득 차 있는 경우 예외 처리 발생
        self.queue[self.rear_cursor] = value
        self.rear_cursor += 1
        self.no += 1
        if self.rear_cursor == self.capacity:
            self.rear_cursor = 0

    def pop(self):
        if self.is_empty():
            return -1
            # raise FixedQueue.Empty  # 큐가 비어있는 경우 예외 처리 발생
        rtval = self.queue[self.front_cursor]
        self.front_cursor += 1
        self.no -= 1
        if self.front_cursor == self.capacity:
            self.front_cursor = 0
        return rtval

    def front(self):
        if self.is_empty():
            return -1
            # raise FixedQueue.Empty  # 큐가 비어있는 경우 예외 처리 발생
        return self.queue[self.front_cursor]

    def back(self):
        if self.is_empty():
            return -1
            # raise FixedQueue.Empty  # 큐가 비어있는 경우 예외 처리 발생
        return self.queue[self.rear_cursor - 1]


people_num, delete_count = list(map(int, sys.stdin.readline().split()))

my_queue = FixedQueue(1001)

answer_list = []

for i in range(1, people_num + 1):
    my_queue.push(i)

while my_queue.get_size():
    for _ in range(delete_count - 1):
        take_num = my_queue.pop()
        my_queue.push(take_num)

    answer_list.append(str(my_queue.pop()))

print(f"<{', '.join(answer_list)}>")
