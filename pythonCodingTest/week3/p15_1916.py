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


def bfs(graph_infos, city):
    global my_deque, cost_infos

    cost = 0
    my_deque.append(city)
    cost_infos[city] = cost

    while my_deque:
        temp_city = my_deque.popleft()

        for next_city_info in graph_infos[temp_city]:
            next_city_num = next_city_info[0]
            next_city_cost = next_city_info[1]

            if cost_infos[next_city_num] > cost_infos[temp_city] + next_city_cost:
                cost_infos[next_city_num] = cost_infos[temp_city] + next_city_cost
                my_deque.append(next_city_num)


CITY_NUM = int(input())
ROAD_NUM = int(input())
problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(ROAD_NUM)]
START_CITY, DESTINATION_CITY = list(map(int, sys.stdin.readline().split()))

# 0번 인덱스는 사용하지 않는다.
graph_infos = [[] for _ in range(CITY_NUM + 1)]

cost_infos = [10**6] * (CITY_NUM + 1)

my_deque = deque()

for info in problem_infos:
    temp_start_city = info[0]
    temp_destination_city = info[1]
    temp_cost = info[2]

    graph_infos[temp_start_city].append((temp_destination_city, temp_cost))

bfs(graph_infos, START_CITY)

print(cost_infos[DESTINATION_CITY])
