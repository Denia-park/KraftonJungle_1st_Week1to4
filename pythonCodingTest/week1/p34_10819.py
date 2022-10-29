import sys

"""
q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]

n = input()  #2
q = [sys.stdin.readline() for i in range(n)]  
# q = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]
"""
n = 2
len_list, quiz_num_list = [
    list(map(int, sys.stdin.readline().split())) for i in range(n)
]

length = len_list[0]
answer_list = []
check_arr = [False] * length


def calculate_list_method(list):
    sum = 0
    for i in range(len(list) - 1):
        cur = list[i]
        next = list[i + 1]

        sum += abs(cur - next)

    return sum


def dfs(list, depth):
    if depth >= length:
        answer_list.append(calculate_list_method(list))
        return

    for i in range(length):
        if not check_arr[i]:
            check_arr[i] = True
            list.append(quiz_num_list[i])
            dfs(list, depth + 1)
            list.pop()
            check_arr[i] = False


dfs([], 0)

print(max(answer_list))
