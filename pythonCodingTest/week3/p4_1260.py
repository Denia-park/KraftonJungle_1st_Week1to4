from collections import deque
import sys

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

N, M, V = list(map(int, sys.stdin.readline().split()))

problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 0번째 인덱스는 사용하지 않고 비워둘 예정
graph_infos = [list() for _ in range(N + 1)]

for info in problem_infos:
    start_node = info[0]
    end_node = info[1]
    graph_infos[start_node].append(end_node)
    graph_infos[end_node].append(start_node)

for graph in graph_infos:
    graph.sort()


def dfs(graph_infos, start_node):
    global visited, answer_list

    if not visited[start_node]:
        visited[start_node] = True
        answer_list.append(start_node)

    for next_node in graph_infos[start_node]:
        if not visited[next_node]:
            visited[next_node] = True
            answer_list.append(next_node)
            dfs(graph_infos, next_node)


def bfs(graph_infos, start_node):
    global visited, answer_list, my_queue

    visited[start_node] = True
    my_queue.append(start_node)
    answer_list.append(start_node)

    while my_queue:
        temp_node = my_queue.popleft()

        for next_node in graph_infos[temp_node]:
            if not visited[next_node]:
                visited[next_node] = True
                answer_list.append(next_node)
                my_queue.append(next_node)


visited = [False] * (N + 1)
answer_list = []
my_queue = deque()
dfs(graph_infos, V)
print(*answer_list)

visited = [False] * (N + 1)
answer_list = []
my_queue = deque()
bfs(graph_infos, V)
print(*answer_list)
