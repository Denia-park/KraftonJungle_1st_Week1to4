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
count = 0


def z_function(row0, col0, row_len, col_len):
    global count, r, c

    if row_len == 2 and col_len == 2:
        if row0 == r and col0 == c:
            print(count)
        elif row0 == r and col0 + 1 == c:
            print(count + 1)
        elif row0 + 1 == r and col0 == c:
            print(count + 2)
        elif row0 + 1 == r and col0 + 1 == c:
            print(count + 3)
        return

    else:
        half_row = row_len // 2
        half_col = col_len // 2

        if row0 <= r < row0 + half_row:
            if col0 <= c < col0 + half_col:
                # 2사분면
                count += (half_row * half_col) * 0
                z_function(row0, col0, half_row, half_col)
            else:
                # 1사분면
                count += (half_row * half_col) * 1
                z_function(row0, col0 + half_col, half_row, half_col)

        else:
            if col0 <= c < col0 + half_col:
                # 3사분면
                count += (half_row * half_col) * 2
                z_function(row0 + half_row, col0, half_row, half_col)
            else:
                # 4사분면
                count += (half_row * half_col) * 3
                z_function(row0 + half_row, col0 + half_col, half_row, half_col)


N, r, c = list(map(int, sys.stdin.readline().split()))

row_size = 2**N
col_size = 2**N

z_function(0, 0, row_size, col_size)
