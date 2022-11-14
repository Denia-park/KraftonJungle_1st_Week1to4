import sys
import heapq

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


def is_out_of_table(row, col):
    return row < 0 or ROW_COL_NUM <= row or col < 0 or ROW_COL_NUM <= col


# 이미 지나감 = -1
# 뚫린 길 = 1
# 막힌 길 = 0
def bfs():
    global my_q

    bk_room = 0
    graph[0][0] = VISITED
    heapq.heappush(my_q, (-VISITED, 0, 0))  # 최대 힙

    while my_q:
        open_state, cur_r, cur_c = heapq.heappop(my_q)  # 최대 힙

        open_state = -open_state  # 최대 힙이라서 - 곱해줌
        cur_r = -cur_r  # 최대 힙이라서 - 곱해줌
        cur_c = -cur_c  # 최대 힙이라서 - 곱해줌

        if cur_r == ROW_COL_NUM - 1 and cur_c == ROW_COL_NUM - 1:
            print(bk_room)
            return

        if open_state == BLOCKED:
            bk_room += 1

        for direc in directions:
            v_r, v_c = direc

            e_r = cur_r + v_r
            e_c = cur_c + v_c

            if is_out_of_table(e_r, e_c):
                continue

            if graph[e_r][e_c] != VISITED:
                heapq.heappush(my_q, (-graph[e_r][e_c], -e_r, -e_c))  # 최대 힙
                graph[e_r][e_c] = VISITED


ROW_COL_NUM = int(input())
VISITED = -1
BLOCKED = 0
OPEN = 1
graph = [
    list(map(int, list(sys.stdin.readline().split()[0]))) for _ in range(ROW_COL_NUM)
]

# 우선 순위 큐 , 최대 힙
my_q = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

bfs()
