import sys

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""
n = 9
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

max = -1

for tuple_val in enumerate(q):
    idx = tuple_val[0] + 1
    val = tuple_val[1][0]

    if max < val:
        max = val

        answer = (max, idx)

print(answer[0])
print(answer[1])
