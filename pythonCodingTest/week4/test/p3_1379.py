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

LECTURE_NUM = int(input())

LECTURE_LIST = [
    list(map(int, sys.stdin.readline().split())) for _ in range(LECTURE_NUM)
]

priority_que = []

answer_idx_list = []

lect_infos = [None] * (LECTURE_NUM + 1)
room_infos = [None] * (LECTURE_NUM + 1)

for lect in LECTURE_LIST:
    lect_num, start, end = lect

    heapq.heappush(priority_que, (start, lect_num, end))

    answer_idx_list.append(lect_num)

sorted_lecture_list = sorted(LECTURE_LIST, key=lambda x: x[1])

max_room_idx = 0

while priority_que:
    start, lect_num, end = heapq.heappop(priority_que)

    for room_idx in range(1, len(room_infos)):
        if room_infos[room_idx] is None:
            room_infos[room_idx] = (lect_num, end)
            lect_infos[lect_num] = room_idx
            max_room_idx = max(max_room_idx, room_idx)
            break
        else:
            if room_infos[room_idx][1] <= start:
                room_infos[room_idx] = (lect_num, end)
                lect_infos[lect_num] = room_idx
                max_room_idx = max(max_room_idx, room_idx)
                break

print(max_room_idx)
for idx in answer_idx_list:
    print(lect_infos[idx])
