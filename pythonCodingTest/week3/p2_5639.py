from collections import deque
import sys

sys.setrecursionlimit(10**6)

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
# https://velog.io/@yujng/%EB%B0%B1%EC%A4%80-5639%EB%B2%88%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

"""
입력값
50
30
24
5
28
45
98
52
60
"""

nums = []

while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break


def postorder(start_idx, end_idx):
    global nums

    if start_idx > end_idx:
        return

    root_node_idx = start_idx

    temp_end_idx = end_idx + 1

    for idx in range(root_node_idx + 1, end_idx + 1):
        if nums[idx] > nums[root_node_idx]:
            temp_end_idx = idx
            break

    postorder(root_node_idx + 1, temp_end_idx - 1)
    postorder(temp_end_idx, end_idx)

    print(nums[start_idx])


root_node_idx = 0
end_node_idx = len(nums) - 1
postorder(root_node_idx, end_node_idx)
