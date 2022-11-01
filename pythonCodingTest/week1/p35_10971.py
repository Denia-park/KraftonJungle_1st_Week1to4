import sys

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = int(input())  #2
q = [sys.stdin.readline() for i in range(n)]  
# q = ["1 2 3", "4 5 6"]

n = int(input())  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""
min_distance = 10000000
distance = 0

n = int(input())  # 2
graph_infos = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

visited = [False] * n


def dfs(start_node, cur_node, deepth):
    global distance, min_distance

    if deepth >= n:
        if graph_infos[cur_node][start_node] != 0:
            distance += graph_infos[cur_node][start_node]
            if min_distance > distance:
                min_distance = distance
            distance -= graph_infos[cur_node][start_node]
            return
        else:
            return

    for target_node in range(n):
        if (
            not visited[target_node]
            and graph_infos[cur_node][target_node] != 0
            and distance < min_distance
        ):
            visited[target_node] = True
            distance += graph_infos[cur_node][target_node]
            dfs(start_node, target_node, deepth + 1)
            distance -= graph_infos[cur_node][target_node]
            visited[target_node] = False


for start_node in range(n):
    distance = 0

    visited[start_node] = True
    dfs(start_node, start_node, 1)
    visited[start_node] = False

print(min_distance)
