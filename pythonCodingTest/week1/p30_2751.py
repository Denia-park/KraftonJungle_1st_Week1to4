import sys

n = int(input())  # 2
q_list = [int(sys.stdin.readline()) for i in range(n)]

q_list.sort()

for val in q_list:
    print(val)
