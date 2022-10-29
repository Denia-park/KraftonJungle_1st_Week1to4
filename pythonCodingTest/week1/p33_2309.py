import itertools
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

combi_list = list(itertools.combinations(q_list, 7))

for sub_list in combi_list:
    if sum(sub_list) == 100:
        for e in sub_list:
            print(e)
        break
