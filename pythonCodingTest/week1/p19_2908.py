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
n = sys.stdin.readline().split()

answer_list = list()

for i in n:
    temp_str = ""
    for j in i[::-1]:
        temp_str += j
    answer_list.append(int(temp_str))

print(max(answer_list))
