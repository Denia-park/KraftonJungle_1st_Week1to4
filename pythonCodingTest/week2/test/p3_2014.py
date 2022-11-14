import heapq
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

primes_len, find_count = list(map(int, sys.stdin.readline().split()))
start_primes = list(map(int, sys.stdin.readline().split()))

answer_list = []

for i in start_primes:
    heapq.heappush(answer_list, i)


play_flag = True

for i in range(find_count):
    answer = heapq.heappop(answer_list)

    for j in start_primes:
        push_value = answer * j

        heapq.heappush(answer_list, push_value)

        if answer % j == 0:
            break

print(answer)
