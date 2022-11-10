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

n = int(input())  # 2
problem_array = [sys.stdin.readline().rstrip() for _ in range(n)]

answer_list = []

def divide_and_conqure(problem_array, row, col, length):
    if length == 0:
        return

    start_number = problem_array[row][col]

    stop_flag = False

    for temp_row in range(length):
        for temp_col in range(length):
            if start_number != problem_array[row + temp_row][col + temp_col]:
                stop_flag = True
                break
        if stop_flag:
            break

    if stop_flag:
        answer_list.append("(")
    else:
        answer_list.append(start_number)
        return

    half_length = length // 2

    divide_and_conqure(problem_array, row, col, half_length)
    divide_and_conqure(problem_array, row, col + half_length, half_length)
    divide_and_conqure(problem_array, row + half_length, col, half_length)
    divide_and_conqure(problem_array, row + half_length, col + half_length, half_length)

    answer_list.append(")")


divide_and_conqure(problem_array, 0, 0, n)
print("".join(answer_list))
