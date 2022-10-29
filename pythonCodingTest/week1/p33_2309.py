import sys

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
q = [sys.stdin.readline() for i in range(n)]  
# q = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""

n = 9
q_list = [int(input()) for i in range(n)]

q_list.sort()

visit = [False] * 9

answer_list = []


def dfs(list, idx):
    global answer_list
    if len(list) >= 7:
        if sum(list) == 100:
            answer_list = list.copy()

        return

    for i in range(idx, 9):
        if not visit[i]:
            visit[i] = True
            list.append(q_list[i])
            dfs(list, i + 1)
            list.pop()
            visit[i] = False


dfs([], 0)

for i in answer_list:
    print(i)
