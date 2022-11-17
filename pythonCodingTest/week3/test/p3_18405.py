from collections import deque
import heapq
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

# 예제는 다 맞는데
# indexError 나서 못 풀었습니다.
# 아무리 봐도 indexError 어디서 나는지 모르겠어요!!

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_out_of_map(r, c):
    return r < 0 or r >= ROW or c < 0 or c >= COL


def bfs():
    global wating_que, priority_que, my_time

    while priority_que:
        if my_time == TIME:
            break

        virus_num, temp_r, temp_c = heapq.heappop(priority_que)

        for direc in directions:
            edit_r = temp_r + direc[0]
            edit_c = temp_c + direc[1]

            if is_out_of_map(edit_r, edit_c):
                continue

            if map_data[edit_r][edit_c] == 0:
                map_data[edit_r][edit_c] = virus_num
                data = (virus_num, edit_r, edit_c)
                wating_que.append(data)

        if priority_que:
            my_time += 1
            while wating_que:
                heapq.heappush(priority_que, wating_que.popleft())


ROW, COL = list(map(int, sys.stdin.readline().split()))

map_data = [list(map(int, sys.stdin.readline().split())) for _ in range(ROW)]
TIME, NEED_ROW, NEED_COL = list(map(int, sys.stdin.readline().split()))

wating_que = deque()
priority_que = []
my_time = 0

for r in range(ROW):
    for c in range(COL):
        if map_data[r][c] != 0:
            data = (map_data[r][c], r, c)
            heapq.heappush(priority_que, data)

bfs()

print(map_data[NEED_ROW - 1][NEED_COL - 1])
