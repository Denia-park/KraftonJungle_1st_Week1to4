import sys

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""
n = int(input())
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

answer_list = list()

for sub_list in q:
    student_num = sub_list[0]
    sub_list_avr = sum(sub_list[1:]) / student_num

    count = 0
    for idx in range(1, student_num + 1):
        if sub_list[idx] > sub_list_avr:
            count += 1

    answer_list.append(f"{(count / student_num * 100):.3f}%")

for sub_list in answer_list:
    print(sub_list)
