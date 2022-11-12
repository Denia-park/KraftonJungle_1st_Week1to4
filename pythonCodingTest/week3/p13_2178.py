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


def is_right_coordinate(graph_infos, row, col):
    global ROW, COL

    return 0 <= row < ROW and 0 <= col < COL and graph_infos[row][col] == "1"


def bfs(graph_infos, row, col, deepth):
    global my_deque

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    deepth = 1
    graph_infos[row][col] = 0
    my_deque.append((row, col, deepth))

    while my_deque:
        temp_coordi = my_deque.popleft()

        temp_row = temp_coordi[0]
        temp_col = temp_coordi[1]
        temp_deepth = temp_coordi[2]

        for i in range(len(directions)):
            edit_row = temp_row + directions[i][0]
            edit_col = temp_col + directions[i][1]

            if is_right_coordinate(graph_infos, edit_row, edit_col):
                graph_infos[edit_row][edit_col] = temp_deepth + 1
                my_deque.append((edit_row, edit_col, temp_deepth + 1))


ROW, COL = list(map(int, sys.stdin.readline().split()))

graph_infos = [list(sys.stdin.readline().rstrip()) for _ in range(ROW)]

my_deque = deque()

bfs(graph_infos, 0, 0, 0)

print(graph_infos[ROW - 1][COL - 1])
