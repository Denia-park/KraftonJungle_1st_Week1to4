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
VERTICAL = "|"
HORIZONTAL = "-"


def bfs(r, c):
    global my_q

    visited[r][c] = True

    my_q.append((r, c))

    while my_q:
        t_r, t_c = my_q.popleft()

        floor_shape = floor_infos[t_r][t_c]

        # "-" 는 좌 우 로만
        if floor_shape == HORIZONTAL:
            l_move = (t_r, t_c - 1)
            r_move = (t_r, t_c + 1)
            # 왼쪽 확인
            if (
                0 <= t_c - 1 < COL
                and floor_infos[l_move[0]][l_move[1]] == HORIZONTAL
                and not visited[l_move[0]][l_move[1]]
            ):
                visited[l_move[0]][l_move[1]] = True
                my_q.append(l_move)
            # 오른쪽 확인
            if (
                0 <= t_c + 1 < COL
                and floor_infos[r_move[0]][r_move[1]] == HORIZONTAL
                and not visited[r_move[0]][r_move[1]]
            ):
                visited[r_move[0]][r_move[1]] = True
                my_q.append(r_move)
        # "|" 는 위 아래 로만
        else:
            u_move = (t_r - 1, t_c)
            d_move = (t_r + 1, t_c)
            # 위쪽 확인
            if (
                0 <= t_r - 1 < ROW
                and floor_infos[u_move[0]][u_move[1]] == VERTICAL
                and not visited[u_move[0]][u_move[1]]
            ):
                visited[u_move[0]][u_move[1]] = True
                my_q.append(u_move)
            # 아래쪽 확인
            if (
                0 <= t_r + 1 < ROW
                and floor_infos[d_move[0]][d_move[1]] == VERTICAL
                and not visited[d_move[0]][d_move[1]]
            ):
                visited[d_move[0]][d_move[1]] = True
                my_q.append(d_move)


ROW, COL = list(map(int, sys.stdin.readline().split()))

floor_infos = [list(sys.stdin.readline().rstrip()) for _ in range(ROW)]
visited = [[False for _ in range(COL)] for _ in range(ROW)]

count = 0
my_q = deque()

for r in range(ROW):
    for c in range(COL):
        if not visited[r][c]:
            count += 1
            bfs(r, c)

print(count)
