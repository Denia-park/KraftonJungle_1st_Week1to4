import sys

sys.setrecursionlimit(10**6)

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
q = [sys.stdin.readline() for i in range(n)]  
# q = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""


def dfs(row, col):
    global temp_graph, temp_count

    if row < 0 or row >= n or col < 0 or col >= n or temp_graph[row][col] == 0:
        return

    temp_graph[row][col] = 0

    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row + 1, col)
    dfs(row, col - 1)


def change_water_height(water_height):
    for row in range(n):
        for col in range(n):
            if answer_graph[row][col] <= water_height:
                temp_graph[row][col] = 0
            else:
                temp_graph[row][col] = 1


n = int(input())  # 2
answer_graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

max_count = 0
temp_count = 0
temp_graph = []

temp_max_height_list = []

for rows in answer_graph:
    temp_max_height_list.append(max(rows))

max_height = max(temp_max_height_list)

for i in range(n):
    temp_row = [0] * n
    temp_graph.append(temp_row)

for water in range(1, max_height):
    change_water_height(water)
    temp_count = 0
    for row in range(n):
        for col in range(n):
            if temp_graph[row][col] == 1:
                temp_count += 1
                dfs(row, col)
                if temp_count > max_count:
                    max_count = temp_count

print(max_count)
