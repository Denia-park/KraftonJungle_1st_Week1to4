from collections import deque
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

TOP = 0
RIGHT = 1
BOT = 2
LEFT = 3


board_size_num = int(input())

apple_num = int(input())
str_apple_list = [list(sys.stdin.readline().split()) for _ in range(apple_num)]
coordi_apple_list = []

direc_num = int(input())
direction_infos = [list(sys.stdin.readline().split()) for _ in range(direc_num)]
direction_dict = dict()

for direction in direction_infos:
    direction_dict[int(direction[0])] = direction[1]

for coordi in str_apple_list:
    str_x = coordi[0]
    int_x = int(str_x) - 1
    str_y = coordi[1]
    int_y = int(str_y) - 1

    coordi_apple_list.append((int_x, int_y))


def change_coordi(coordi, direction):
    row = coordi[0]
    col = coordi[1]

    if direction == TOP:
        new_coordi = (row - 1, col)
    elif direction == RIGHT:
        new_coordi = (row, col + 1)
    elif direction == BOT:
        new_coordi = (row + 1, col)
    elif direction == LEFT:
        new_coordi = (row, col - 1)

    return new_coordi


def is_range_out(coordi):
    global board_size_num
    row = coordi[0]
    col = coordi[1]

    return row < 0 or row >= board_size_num or col < 0 or col >= board_size_num


snake_deque = deque()
snake_deque.append((0, 0))
snake_head_direc = RIGHT  # 1 , 2 , 3 , 4 => 1 top , 2 right , 3 bot , 4 left

time = 0

while True:
    time += 1

    snake_move_list = []

    new_deque = deque()
    head_coordi = snake_deque.popleft()
    new_head_coordi = change_coordi(head_coordi, snake_head_direc)
    new_deque.append(new_head_coordi)
    snake_move_list.append(new_head_coordi)

    body_coordi = 0

    for idx in range(len(snake_deque) - 1):
        body_coordi = snake_deque.popleft()
        new_deque.append(body_coordi)
        snake_move_list.append(body_coordi)

    snake_deque = new_deque

    if snake_deque[0] in coordi_apple_list:
        snake_deque.append(body_coordi)

    if is_range_out(snake_deque[0]):
        print(time)
        break

    if snake_deque[0] in snake_move_list[1:]:
        print(time)
        break

    if time in direction_dict:
        change_direction = direction_dict[time]
        if change_direction == "L":
            snake_head_direc = (snake_head_direc + 4 - 1) % 4
        elif change_direction == "D":
            snake_head_direc = (snake_head_direc + 4 + 1) % 4
