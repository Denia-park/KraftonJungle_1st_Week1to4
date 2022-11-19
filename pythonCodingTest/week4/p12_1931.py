import heapq
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

MEETING_NUM = int(input())
MEETING_LIST = [
    list(map(int, sys.stdin.readline().split())) for _ in range(MEETING_NUM)
]

count = 0

new_list = []

for meeting_info in MEETING_LIST:
    start_time, end_time = meeting_info
    data = (end_time, start_time)
    heapq.heappush(new_list, data)

while new_list:
    end_time, start_time = heapq.heappop(new_list)

    if count == 0:
        count += 1  # 처음 꺼내는 애는 무조건 꺼내기 때문에 1개를 올린다.
        save_end_time = end_time
        continue

    if save_end_time > start_time:
        continue

    save_end_time = end_time
    count += 1

print(count)
