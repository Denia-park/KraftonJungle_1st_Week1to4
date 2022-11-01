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

n = int(input())  # 2
count_list = [0] * 10001
for i in range(n):
    temp_val = int(sys.stdin.readline())
    count_list[temp_val] += 1

for idx in range(1, len(count_list)):
    for _ in range(count_list[idx]):
        print(idx)
