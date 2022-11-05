from bisect import bisect_left
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


shoot_position_num, animal_num, shoot_range = list(
    map(int, sys.stdin.readline().split())
)

shoot_position_list = list(map(int, sys.stdin.readline().split()))

animal_position = [
    list(map(int, sys.stdin.readline().split())) for i in range(animal_num)
]

count = 0
shoot_position_list.sort()


def my_bisect_right(list, key):
    start = 0
    end = len(list)
    while start < end:
        mid = (start + end) // 2
        if list[mid] < key:
            start = mid + 1
        else:
            end = mid

    return end


for animal_pos in animal_position:
    x = animal_pos[0]
    y = animal_pos[1]

    if y > shoot_range:
        continue

    max_x_distance = shoot_range - y

    bigger_idx = my_bisect_right(shoot_position_list, x - max_x_distance)

    if shoot_position_list[bigger_idx] <= (x + max_x_distance):
        count += 1
        # print(x, y)

print(count)
