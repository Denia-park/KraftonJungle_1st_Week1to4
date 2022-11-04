import sys

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

n = 2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

need_length = q[0][1]
q[1].sort()
tree_list = q[1]
max_tree_height = tree_list[-1]

start_height = 0
end_height = max_tree_height

max_height = 0

while True:
    mid_height = (start_height + end_height) // 2
    temp_sum = 0
    for each_tree in tree_list:
        # temp_sum = temp_sum + (each_tree - mid_height)
        diff_height = each_tree - mid_height
        if diff_height > 0:
            temp_sum += diff_height

    if temp_sum >= need_length:
        max_height = mid_height
        start_height = mid_height + 1
    else:
        end_height = mid_height - 1

    if start_height > end_height:
        break

print(max_height)
