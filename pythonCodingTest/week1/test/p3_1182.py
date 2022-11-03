import sys

sys.setrecursionlimit(10000)


def dfs(quiz_num, deepth, cur_idx, cur_sum):
    global count, visited, quiz_element_list, n

    if deepth != 0 and cur_sum == quiz_num:
        count += 1
    elif deepth >= n:
        return

    for idx in range(cur_idx, len(quiz_element_list)):
        # visited[idx] = True
        each_element = quiz_element_list[idx]

        dfs(quiz_num, deepth + 1, cur_idx + 1, cur_sum + each_element)


def solve(quiz_num):
    global count
    count = 0

    dfs(quiz_num, 0, 0, 0)

    return count


n, quiz_num = list(map(int, sys.stdin.readline().split()))
quiz_element_list = list(map(int, sys.stdin.readline().split()))

visited = [False] * n

count = 0

print(solve(quiz_num))

"""
n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

# print("Q1 :", solve(4) == 7)
# print("Q2 :", solve(7) == 44)
# print("Q3 :", solve(10) == 274)
