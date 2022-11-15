from collections import deque
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


def is_out_of_table(row, col):
    return row < 0 or TOTAL_ROW <= row or col < 0 or TOTAL_COL <= col


def is_ok_move_water(row, col):
    map_data = map[row][col]
    return map_data == EMPTY


def is_ok_move_animal(row, col):
    map_data = map[row][col]
    return map_data == EMPTY or map_data == DESTINATION


def bfs(my_s_r, my_s_c):
    global my_q

    hour = 0

    temp_list = deque()

    my_q.append((ANIMAL, my_s_r, my_s_c))

    while my_q:
        water_animal_flag, cur_r, cur_c = my_q.popleft()

        if map[cur_r][cur_c] == DESTINATION:
            return hour

        for direc in directions:
            v_r, v_c = direc

            e_r = cur_r + v_r
            e_c = cur_c + v_c

            if is_out_of_table(e_r, e_c):
                continue

            if water_animal_flag == ANIMAL:
                if is_ok_move_animal(e_r, e_c):
                    if map[e_r][e_c] != DESTINATION:
                        map[e_r][e_c] = water_animal_flag

                    temp_list.append((water_animal_flag, e_r, e_c))
            else:
                if is_ok_move_water(e_r, e_c):
                    map[e_r][e_c] = water_animal_flag
                    temp_list.append((water_animal_flag, e_r, e_c))

        if len(my_q) == 0:
            hour += 1
            while temp_list:
                my_q.append(temp_list.popleft())

    return -1


DESTINATION = "D"
ANIMAL = "S"
EMPTY = "."
WATER = "*"
STONE = "X"

TOTAL_ROW, TOTAL_COL = list(map(int, sys.stdin.readline().split()))
map = [list(sys.stdin.readline().split()[0]) for _ in range(TOTAL_ROW)]

my_q = deque()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

my_s_r = -1
my_s_c = -1
w_r = -1
w_c = -1

for t_r in range(TOTAL_ROW):
    for t_c in range(TOTAL_COL):
        if map[t_r][t_c] == ANIMAL:
            my_s_r = t_r
            my_s_c = t_c
        elif map[t_r][t_c] == WATER:
            my_q.append((WATER, t_r, t_c))

rtval = bfs(my_s_r, my_s_c)

if rtval == -1:
    print("KAKTUS")
else:
    print(rtval)
