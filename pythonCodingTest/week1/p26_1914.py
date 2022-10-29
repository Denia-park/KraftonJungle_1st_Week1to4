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
# https://study-all-night.tistory.com/6


def hanoi_move(block_count, start, end):
    if block_count == 1:
        print(f"{start} {end}")
        return

    hanoi_move(block_count - 1, start, 6 - start - end)
    hanoi_move(1, start, end)
    hanoi_move(block_count - 1, 6 - start - end, end)


block_num = int(input())

# 하노이 탑 에서 총 움직이는 수는 2^n - 1개 이다. , n 은 블럭의 수
print(2**block_num - 1)

if block_num < 21:
    hanoi_move(block_num, 1, 3)
