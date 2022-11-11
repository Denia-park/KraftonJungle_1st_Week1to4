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

# 시간이 부족해서 다 풀지 못 했습니다 ㅠㅠ.

primes_len, find_count = list(map(int, sys.stdin.readline().split()))
start_primes = list(map(int, sys.stdin.readline().split()))

save_primes1 = []
save_primes2 = []

answer_list = []

for i in start_primes:
    heapq.heappush(save_primes1, i)
    heapq.heappush(answer_list, i)
    heapq.heappush(save_primes1, i * i)
    heapq.heappush(answer_list, i * i)

play_flag = True
while play_flag:
    if save_primes1:
        small_value = heapq.heappop(save_primes1)

        while save_primes1:
            next_small_value = heapq.heappop(save_primes1)

            if small_value * next_small_value > 2**31:
                play_flag = False
                break

            heapq.heappush(save_primes2, small_value * next_small_value)
            heapq.heappush(answer_list, small_value * next_small_value)
    else:
        small_value = heapq.heappop(save_primes2)

        while save_primes2:
            next_small_value = heapq.heappop(save_primes2)

            if small_value * next_small_value > 2**31:
                play_flag = False
                break

            heapq.heappush(save_primes1, small_value * next_small_value)
            heapq.heappush(answer_list, small_value * next_small_value)

print_list = []

for _ in range(find_count):
    print_list.append(heapq.heappop(answer_list))

print(print_list[-1])
