import sys


def solve(quiz_num_str):
    origin_quiz_num_str = quiz_num_str

    if int(quiz_num_str) < 10:
        quiz_num_str = "0" + quiz_num_str

    count = 0

    while True:
        last_each_num = quiz_num_str[-1]

        each_num_sum = 0
        for each_num in quiz_num_str:
            each_num_sum += int(each_num)

        quiz_num_str = last_each_num + str(each_num_sum)[-1]

        count += 1

        if int(quiz_num_str) == int(origin_quiz_num_str):
            break

    return count


input_val = input()
print(solve(input_val))


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

# print("Q1 :", solve("26") == 4)
# print("Q2 :", solve("55") == 3)
# print("Q3 :", solve("1") == 60)
# print("Q4 :", solve("0") == 1)
# print("Q5 :", solve("71") == 12)
