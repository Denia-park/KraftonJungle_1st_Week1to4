import heapq
import sys

"""
n = input()  #2
a = [sys.stdin.readline() for _ in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

TEST_CASE_NUM = int(input())

priority_que = []
# max_score_people

for _ in range(TEST_CASE_NUM):
    PEOPLE_NUM = int(input())
    test_infos = [
        list(map(int, sys.stdin.readline().split())) for _ in range(PEOPLE_NUM)
    ]
    count = 1

    for info in test_infos:
        a_rank, b_rank = info
        sum_rank = a_rank + b_rank

        data = (sum_rank, a_rank, b_rank)
        heapq.heappush(priority_que, data)

    sum_rank, a_rank, b_rank = heapq.heappop(priority_que)

    standard_man = (a_rank, b_rank)

    while priority_que:
        next_man_sum_rank, next_man_a_rank, next_man_b_rank = heapq.heappop(
            priority_que
        )

        if a_rank > next_man_a_rank or b_rank > next_man_b_rank:
            count += 1

    print(count)
