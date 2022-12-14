import heapq
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


def dijkstra(graph_infos, start_city):
    global my_priority_q, cost_infos, visited

    start_city_arrrive_cost = 0
    cost_infos[start_city] = start_city_arrrive_cost
    heapq.heappush(my_priority_q, (start_city_arrrive_cost, start_city))

    while my_priority_q:
        temp_city_arrive_cost, temp_city = heapq.heappop(my_priority_q)

        # 방문처리를 해주지 않으면 쓸모없는 것에 for문으로 시간이 끌리면서
        # 시간 초과가 난다.
        if visited[temp_city]:
            continue

        visited[temp_city] = True

        for next_city_info in graph_infos[temp_city]:
            next_city_arrrive_cost, next_city = next_city_info

            if cost_infos[next_city] > temp_city_arrive_cost + next_city_arrrive_cost:
                cost_infos[next_city] = temp_city_arrive_cost + next_city_arrrive_cost
                heapq.heappush(my_priority_q, (cost_infos[next_city], next_city))


CITY_NUM = int(input())
ROAD_NUM = int(input())
problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(ROAD_NUM)]
START_CITY, DESTINATION_CITY = list(map(int, sys.stdin.readline().split()))

# 0번 인덱스는 사용하지 않는다.
graph_infos = [[] for _ in range(CITY_NUM + 1)]

cost_infos = [10**9] * (CITY_NUM + 1)
visited = [False] * (CITY_NUM + 1)

my_priority_q = []

for info in problem_infos:
    temp_start_city = info[0]
    temp_destination_city = info[1]
    temp_cost = info[2]

    graph_infos[temp_start_city].append((temp_cost, temp_destination_city))

dijkstra(graph_infos, START_CITY)

print(cost_infos[DESTINATION_CITY])
