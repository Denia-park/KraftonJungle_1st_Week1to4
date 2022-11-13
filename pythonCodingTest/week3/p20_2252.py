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

# 진입 차수가 0인 애들을 큐에 넣고, 진출 차수를 1씩 빼주자.
def topology_sort(graph_infos):
    result = []
    q = deque()

    for stu_idx in range(1, STUDENT_NUM + 1):
        if indegree[stu_idx] == 0:
            q.append(stu_idx)

    while q:
        temp_stu_idx = q.popleft()
        result.append(temp_stu_idx)

        for next_sut_idx in graph_infos[temp_stu_idx]:
            indegree[next_sut_idx] -= 1

            if indegree[next_sut_idx] == 0:
                q.append(next_sut_idx)

    return result


STUDENT_NUM, DIFF_NUM = list(map(int, sys.stdin.readline().split()))
problem_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(DIFF_NUM)]

# 0번 인덱스는 사용하지 않는다.
graph_infos = [[] for _ in range(STUDENT_NUM + 1)]
indegree = [0] * (STUDENT_NUM + 1)

for info in problem_infos:
    small_student = info[0]
    big_student = info[1]

    graph_infos[small_student].append(big_student)
    indegree[big_student] += 1


print(*topology_sort(graph_infos))
