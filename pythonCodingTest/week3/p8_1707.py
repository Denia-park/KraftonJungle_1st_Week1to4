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
RED = 1
BLUE = 0
test_case_num = 0


def dfs(graph, cur_node, cur_color):
    global test_case_num

    for next_node in graph[cur_node]:
        if visited[next_node] == cur_color:
            answer[test_case_num] = "NO"
            return
        elif visited[next_node] == -1:
            next_color = cur_color ^ 1
            visited[next_node] = next_color
            dfs(graph, next_node, next_color)


TEST_CASE_NUM = list(map(int, sys.stdin.readline().split()))[0]
answer = ["YES"] * TEST_CASE_NUM

for cur_test_case_num in range(TEST_CASE_NUM):
    test_case_num = cur_test_case_num
    NODE_NUM, EDGE_NUM = list(map(int, sys.stdin.readline().split()))
    problem_infos = [
        list(map(int, sys.stdin.readline().split())) for _ in range(EDGE_NUM)
    ]
    graph = [[] for _ in range(NODE_NUM + 1)]
    visited = [-1] * (NODE_NUM + 1)

    for info in problem_infos:
        node_a, node_b = info
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    # ★★★ 모든 노드들에 대해서 고려를 해줘야 한다. ★★★
    for temp_start_noed in range(1, NODE_NUM):
        if visited[temp_start_noed] == -1:
            temp_color = RED
            visited[1] = temp_color
            dfs(graph, temp_start_noed, temp_color)

for temp_answer in answer:
    print(temp_answer)
