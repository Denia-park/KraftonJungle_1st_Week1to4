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

# 정답 참고
# https://sanghyu.tistory.com/36

TEST_CASE_NUM = int(input())

for _ in range(TEST_CASE_NUM):
    PEOPLE_NUM = int(input())
    test_infos = [
        list(map(int, sys.stdin.readline().split())) for _ in range(PEOPLE_NUM)
    ]
    count = 1

    test_infos.sort()

    pass_people = None

    max_rank = test_infos[0][1]

    for idx in range(1, len(test_infos)):
        cur_tester_max_rank = test_infos[idx][1]
        if max_rank > cur_tester_max_rank:
            count += 1
            max_rank = cur_tester_max_rank

    print(count)
