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

row_col_num = int(input())
paper_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(row_col_num)]

white_paper_num = 0
blue_paper_num = 0

BLUE_COLOR = 1
WHITE_COLOR = 0


def is_same_all_color(list_list, row, col, check_len):
    start_color = list_list[row][col]

    for r in range(row, row + check_len):
        for c in range(col, col + check_len):
            if list_list[r][c] != start_color:
                return False

    return True


def divide_and_conqure(list_list, row, col, check_len):
    global blue_paper_num, white_paper_num

    if is_same_all_color(list_list, row, col, check_len):
        start_color = list_list[row][col]
        if start_color == BLUE_COLOR:
            blue_paper_num += 1
        else:
            white_paper_num += 1

        return

    half_len = check_len // 2

    divide_and_conqure(list_list, row, col, half_len)
    divide_and_conqure(list_list, row, col + half_len, half_len)
    divide_and_conqure(list_list, row + half_len, col, half_len)
    divide_and_conqure(list_list, row + half_len, col + half_len, half_len)


divide_and_conqure(paper_infos, 0, 0, row_col_num)

print(white_paper_num)
print(blue_paper_num)
