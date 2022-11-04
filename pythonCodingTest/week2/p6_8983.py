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


def bisect_right(list, key):
    start_idx = 0
    end_idx = len(list)

    while start_idx < end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if list[mid_idx] <= key:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx

    return end_idx


shoot_position_num, animal_num, shoot_range = list(
    map(int, sys.stdin.readline().split())
)

shoot_position_list = list(map(int, sys.stdin.readline().split()))

animal_position = [
    list(map(int, sys.stdin.readline().split())) for i in range(animal_num)
]

count = 0
shoot_position_list.sort()

for animal_pos in animal_position:
    x = animal_pos[0]
    y = animal_pos[1]

    if y > shoot_range:
        continue

    bigger_idx = bisect_right(shoot_position_list, x)

    if bigger_idx >= len(shoot_position_list):
        bigger_idx = len(shoot_position_list) - 1

    if (
        abs(shoot_position_list[bigger_idx] - x) + y <= shoot_range
        or abs(shoot_position_list[bigger_idx - 1] - x) + y <= shoot_range
    ):
        print(x, y)
        count += 1

print(count)
