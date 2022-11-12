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

NODE_NUM, EDGE_NUM = list(map(int, sys.stdin.readline().split()))
problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(EDGE_NUM)]

graph_sort_infos = []

for info in problem_infos:
    node1, node2, cost = info
    graph_sort_infos.append((cost, node1, node2))

# 가중치를 기준으로 sorting
graph_sort_infos.sort()

# 0은 사용하지 않음
parents = [0] * (NODE_NUM + 1)
# 부모를 자기 자신으로 초기화
for i in range(1, NODE_NUM + 1):
    parents[i] = i
cost_sum = 0


def find_parent(parents, element):
    if parents[element] != element:
        parents[element] = find_parent(parents, parents[element])

    return parents[element]


def union_parent(parents, ele1, ele2):
    ele1_parent = find_parent(parents, ele1)
    ele2_parent = find_parent(parents, ele2)

    if ele1_parent < ele2_parent:
        parents[ele2] = ele1_parent
    else:
        parents[ele1] = ele2_parent


for info in graph_sort_infos:
    cost, node1, node2 = info

    if find_parent(parents, node1) != find_parent(parents, node2):
        cost_sum += cost
        union_parent(parents, node1, node2)

print(cost_sum)
