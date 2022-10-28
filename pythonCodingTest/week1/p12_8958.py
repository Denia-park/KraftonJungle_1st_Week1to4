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
q = [list(sys.stdin.readline().split()) for i in range(n)]

answer_list = list()

for i in q:
    quiz_str = i[0]

    temp_score = 0

    temp_save_score = 0
    temp_cur_score = 0

    for each_ch in quiz_str:
        if each_ch == "O":
            temp_cur_score = temp_save_score + 1
            temp_save_score += 1

            temp_score += temp_cur_score
        else:
            temp_save_score = 0

    answer_list.append(temp_score)

for i in answer_list:
    print(i)
