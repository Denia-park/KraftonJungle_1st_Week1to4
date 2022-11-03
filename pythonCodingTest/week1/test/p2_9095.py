import sys

sys.setrecursionlimit(10000)

def dfs(quiz_num, cur_sum):
    global count, use_num_list
    if cur_sum == quiz_num:
        count += 1
        return

    for i in use_num_list:
        if cur_sum + i <= quiz_num:
            dfs(quiz_num, cur_sum + i)


def solve(quiz_num):
    global count, answer_list
    count = 0

    dfs(quiz_num, 0)
    
    answer_list.append(count)


n = int(input())
quiz_num_list_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

answer_list = []
use_num_list = [1, 2, 3]
count = 0

for quiz_num_list in quiz_num_list_list:
    quiz_num = quiz_num_list[0]
    solve(quiz_num)

for i in answer_list:
    print(i)

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
