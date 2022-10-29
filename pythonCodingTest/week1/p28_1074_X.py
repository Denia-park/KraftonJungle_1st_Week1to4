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
sys.setrecursionlimit(10**8)  # 10^8 까지 늘림.

count = 0


def z_function(table, row0, col0, row_len, col_len):
    global count

    if row_len == 2 and col_len == 2:
        table[row0][col0] = count
        count += 1
        table[row0][col0 + 1] = count
        count += 1
        table[row0 + 1][col0] = count
        count += 1
        table[row0 + 1][col0 + 1] = count
        count += 1

        return
    else:
        half_row = row_len // 2
        half_col = col_len // 2

        z_function(table, row0, col0, half_row, half_col)
        z_function(table, row0, col0 + half_col, half_row, half_col)
        z_function(table, row0 + half_row, col0, half_row, half_col)
        z_function(table, row0 + half_row, col0 + half_col, half_row, half_col)


N, r, c = list(map(int, sys.stdin.readline().split()))

row_size = 2**N
col_size = 2**N

table = [[-1] * col_size for _ in range(row_size)]

z_function(table, 0, 0, row_size, col_size)

print(table[r][c])
