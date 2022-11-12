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
    global my_priority_q, cost_infos

    start_city_arrrive_cost = 0
    cost_infos[start_city] = start_city_arrrive_cost
    heapq.heappush(my_priority_q, (start_city_arrrive_cost, start_city))

    while my_priority_q:
        temp_city_arrive_cost, temp_city = heapq.heappop(my_priority_q)

        # 이미 큐에 temp_city 관련 내용들이 많이 들어가 있는 상태에서
        # cost_infos[temp_city]가 업데이트 되면 그 쓸모없는 애들의 for문을
        # 거를수가 없기 때문에 시간초과가 나는 듯 하다.
        if cost_infos[temp_city] < temp_city_arrive_cost:
            continue

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

my_priority_q = []

for info in problem_infos:
    temp_start_city = info[0]
    temp_destination_city = info[1]
    temp_cost = info[2]

    graph_infos[temp_start_city].append((temp_cost, temp_destination_city))

dijkstra(graph_infos, START_CITY)

print(cost_infos[DESTINATION_CITY])
