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
# 정답 참조
# https://etst.tistory.com/194

shoot_position_num, animal_num, shoot_range = list(
    map(int, sys.stdin.readline().split())
)

shoot_position_list = list(map(int, sys.stdin.readline().split()))

animal_position = [
    list(map(int, sys.stdin.readline().split())) for i in range(animal_num)
]

count = 0
shoot_position_list.sort()


def is_animal_x_in_shoot_range(animal_x, my_shoot_pos, max_x_distance):
    return (animal_x == my_shoot_pos) or (
        animal_x - max_x_distance
    ) <= my_shoot_pos <= (animal_x + max_x_distance)


for animal_pos in animal_position:
    animal_x = animal_pos[0]
    animal_y = animal_pos[1]

    if animal_y > shoot_range:
        continue

    max_x_distance = shoot_range - animal_y

    start = 0
    end = shoot_position_num - 1

    while start <= end:
        mid = (start + end) // 2
        my_shoot_pos = shoot_position_list[mid]
        if is_animal_x_in_shoot_range(animal_x, my_shoot_pos, max_x_distance):
            count += 1
            break
        elif animal_x < my_shoot_pos:
            end = mid - 1
        else:
            start = mid + 1

print(count)
