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
    global my_deque, visited, NEED_DISTANCE, answers

    distance = 0
    visited[city] = distance
    my_deque.append((city, distance))

    while my_deque:
        temp_city_info = my_deque.popleft()
        temp_city_num = temp_city_info[0]
        temp_distance = temp_city_info[1]
        next_distance = temp_distance + 1

        for next_city in graph_infos[temp_city_num]:
            if visited[next_city] == -1 and next_distance <= NEED_DISTANCE:
                visited[next_city] = next_distance
                my_deque.append((next_city, next_distance))

                if next_distance == NEED_DISTANCE:
                    answers.append(next_city)


CITY_NUM, ROAD_NUM, NEED_DISTANCE, START_CITY = list(
    map(int, sys.stdin.readline().split())
)

problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(ROAD_NUM)]

# 0번 인덱스는 사용하지 않는다.
graph_infos = [[] for _ in range(CITY_NUM + 1)]

visited = [-1] * (CITY_NUM + 1)

my_deque = deque()

for info in problem_infos:
    temp_start_city = info[0]
    temp_destination_city = info[1]

    graph_infos[temp_start_city].append(temp_destination_city)

my_deque = deque()
answers = []

bfs(graph_infos, START_CITY)

if not answers:
    print(-1)
else:
    answers.sort()

    for i in answers:
        print(i)
