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
# 정답 참조
# https://art-coding3.tistory.com/44

n = int(input())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

left_max_q = []
right_min_q = []
answer = []

for num in num_list:
    if len(left_max_q) == len(right_min_q):
        heapq.heappush(left_max_q, (-num, num))
    else:
        heapq.heappush(right_min_q, (num, num))

    if right_min_q and left_max_q[0][1] > right_min_q[0][1]:
        left_data = heapq.heappop(left_max_q)
        right_data = heapq.heappop(right_min_q)

        # left 와 right 각각의 heap 은 우선순위가 반대이므로 -를 곱해줘서 순서를 반대로 해야한다.
        edit_left_data = (-left_data[0], left_data[1])
        edit_right_data = (-right_data[0], right_data[1])

        heapq.heappush(left_max_q, edit_right_data)
        heapq.heappush(right_min_q, edit_left_data)

    answer.append(left_max_q[0][1])

for i in answer:
    print(i)
