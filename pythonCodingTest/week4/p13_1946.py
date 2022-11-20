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

for _ in range(TEST_CASE_NUM):
    PEOPLE_NUM = int(input())
    test_infos = [
        list(map(int, sys.stdin.readline().split())) for _ in range(PEOPLE_NUM)
    ]
    count = 1

    test_infos.sort()

    pass_people = []

    for tester_info in test_infos:
        if not pass_people:
            pass_people.append(tester_info)
        else:
            temp_count = 0
            for pass_info in pass_people:
                if pass_info[0] < tester_info[0] and pass_info[1] < tester_info[1]:
                    break
                temp_count += 1

            if len(pass_people) == temp_count:
                pass_people.append(tester_info)

    print(len(pass_people))
