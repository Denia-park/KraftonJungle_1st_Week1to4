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

quene_num = int(input())

answer = 0


def n_queen(list, depth):
    global answer
    if len(list) == quene_num:
        answer += 1
        return

    temp_depth = depth
    check_list = [True] * (quene_num + 1)

    for i in list:
        my_pos = i
        check_list[my_pos] = False

        left = i - temp_depth
        right = i + temp_depth
        temp_depth -= 1

        if 1 <= left <= quene_num:
            check_list[left] = False

        if 1 <= right <= quene_num:
            check_list[right] = False

    for i in range(1, quene_num + 1):
        if check_list[i]:
            list.append(i)
            n_queen(list, depth + 1)
            list.pop()


n_queen(list(), 0)

print(answer)
