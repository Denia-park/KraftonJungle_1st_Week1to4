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

NODE_NUM, LINE_NUM = list(map(int, sys.stdin.readline().split()))

problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(LINE_NUM)]

# 0번 인덱스는 사용하지 않는다.
graph_infos = [[] for _ in range(NODE_NUM + 1)]

count = 0

visited = [False] * (NODE_NUM + 1)

for temp_node_infos in problem_infos:
    temp_node1 = temp_node_infos[0]
    temp_node2 = temp_node_infos[1]

    graph_infos[temp_node1].append(temp_node2)
    graph_infos[temp_node2].append(temp_node1)


def dfs(graph_infos, start_node):
    global visited

    for next_node in graph_infos[start_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(graph_infos, next_node)


for start_node in range(1, NODE_NUM + 1):
    if not visited[start_node]:
        visited[start_node] = True
        dfs(graph_infos, start_node)
        count += 1

print(count)
