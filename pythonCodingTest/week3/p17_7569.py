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
# 0 : 안익음
# 1 : 영향을 줄 놈
# 2 : 1때매 영향을 받은 놈
# -1 : 토마토 없음

# -1은 무시해야함
# 맨 처음에는 1이 영향을 줌 -> 다음에는 2만 따라가면 됨


def print_result(day_count):
    for t_h in range(TOTAL_HEIGHT):
        for t_r in range(TOTAL_ROW):
            for t_c in range(TOTAL_COL):
                if problem_infos[t_h][t_r][t_c] == 0:
                    return print(-1)

    if check_count == 0:
        return print(0)
    else:
        return print(day_count - 1)


def is_out_of_table(height, row, col):
    return (
        height < 0
        or TOTAL_HEIGHT <= height
        or row < 0
        or TOTAL_ROW <= row
        or col < 0
        or TOTAL_COL <= col
    )


def bfs():
    global check_count, my_q, day_count

    for t_h in range(TOTAL_HEIGHT):
        for t_r in range(TOTAL_ROW):
            for t_c in range(TOTAL_COL):
                if problem_infos[t_h][t_r][t_c] == day_count:
                    my_q.append((t_h, t_r, t_c, day_count))

    while my_q:
        cur_h, cur_r, cur_c, cur_day = my_q.popleft()

        for direc in directions:
            v_h, v_r, v_c = direc

            e_h = cur_h + v_h
            e_r = cur_r + v_r
            e_c = cur_c + v_c

            if is_out_of_table(e_h, e_r, e_c):
                continue

            if problem_infos[e_h][e_r][e_c] == 0:
                day_count = cur_day + 1
                check_count += 1
                problem_infos[e_h][e_r][e_c] = day_count
                my_q.append((e_h, e_r, e_c, day_count))


TOTAL_COL, TOTAL_ROW, TOTAL_HEIGHT = list(map(int, sys.stdin.readline().split()))
problem_infos = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(TOTAL_ROW)]
    for _ in range(TOTAL_HEIGHT)
]

# 6방향을 고려해야 한다. 상 하 좌 우 윗층 아랫층
# 변화가 없는 날이 종료되는 날
check_count = 0
day_count = 1
my_q = deque()
directions = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]

bfs()

print_result(day_count)
