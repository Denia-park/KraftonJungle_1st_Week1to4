import sys
import heapq

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

n = int(input())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

heap = []

sum = 0

for num in num_list:
    heapq.heappush(heap, num)

while len(heap) != 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)

    count = num1 + num2

    sum += count

    heapq.heappush(heap, count)

print(sum)
