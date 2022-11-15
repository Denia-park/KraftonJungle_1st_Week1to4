from collections import deque
import math
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


def bfs(graph, start_node):
    global my_q

    visited[start_node] = True
    my_q.append(start_node)

    temp_count = 0

    while my_q:
        temp_node = my_q.popleft()

        for next_node in graph[temp_node]:
            if inside_places[next_node] == INSIDE:
                temp_count += 1
            else:
                if not visited[next_node]:
                    visited[next_node] = True
                    my_q.append(next_node)

    temp_total_walking_route = temp_count * (temp_count - 1)

    return temp_total_walking_route


INSIDE = 1
OUTSIDE = 0

NODE_NUM = int(input())
temp_inside_places = list(map(int, list(sys.stdin.readline().split()[0])))
EDGE_NUM = len(temp_inside_places) - 1
inside_places = [0] + temp_inside_places

graph = [[] for _ in range(NODE_NUM + 1)]
visited = [False] * (NODE_NUM + 1)

my_q = deque()

count = 0

for _ in range(EDGE_NUM):
    n_a, n_b = list(map(int, sys.stdin.readline().split()))

    if inside_places[n_a] == 1 and inside_places[n_b] == 1:
        count += 2

    graph[n_a].append(n_b)
    graph[n_b].append(n_a)

for start_node in range(1, NODE_NUM + 1):
    if inside_places[start_node] == OUTSIDE and not visited[start_node]:
        count += bfs(graph, start_node)

print(count)
