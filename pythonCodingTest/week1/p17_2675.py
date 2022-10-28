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
n = int(input())
q = [sys.stdin.readline().split() for i in range(n)]

for sub_list in q:
    num = int(sub_list[0])

    new_str = ""

    for ch in sub_list[1]:
        new_str += ch * num

    print(new_str)
