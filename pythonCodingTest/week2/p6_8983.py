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

for animal_pos in animal_position:
    x = animal_pos[0]
    y = animal_pos[1]

    if y > shoot_range:
        continue

    smaller_idx = bisect_left(shoot_position_list, x)

    if (
        abs(shoot_position_list[smaller_idx] - x) + y <= shoot_range
        or abs(shoot_position_list[smaller_idx + 1] - x) + y <= shoot_range
    ):
        print(x, y)
        count += 1

print(count)
