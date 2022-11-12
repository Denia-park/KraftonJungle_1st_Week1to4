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

NODE_NUM = list(map(int, sys.stdin.readline().split()))[0]
EDGE_NUM = NODE_NUM - 1

problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(EDGE_NUM)]

# 0번 인덱스는 사용하지 않는다.
graph_infos = [[] for _ in range(NODE_NUM + 1)]

visited = [0] * (NODE_NUM + 1)

my_deque = deque()

for temp_node_infos in problem_infos:
    temp_node1 = temp_node_infos[0]
    temp_node2 = temp_node_infos[1]

    graph_infos[temp_node1].append(temp_node2)
    graph_infos[temp_node2].append(temp_node1)


def bfs(graph_infos, start_node):
    global visited, my_deque

    visited[start_node] = 1
    my_deque.append(start_node)

    while my_deque:
        temp_node = my_deque.popleft()

        for next_node in graph_infos[temp_node]:
            if visited[next_node] == 0:
                visited[next_node] = temp_node
                my_deque.append(next_node)


START_NODE = 1
bfs(graph_infos, START_NODE)

for idx in range(2, NODE_NUM + 1):
    print(visited[idx])
