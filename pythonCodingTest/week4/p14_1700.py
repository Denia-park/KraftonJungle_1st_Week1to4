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
# https://ideadummy.tistory.com/21

TAP_NUM, PRODUCT_NUM = map(int, sys.stdin.readline().split())
PRODUCT_LIST = list(map(int, sys.stdin.readline().split()))

plugged = []

answer_count = 0

for cur_idx in range(len(PRODUCT_LIST)):
    continue_flag = False

    # 이미 사용중인 제품인가?
    if PRODUCT_LIST[cur_idx] in plugged:
        continue

    if len(plugged) < TAP_NUM:
        plugged.append(PRODUCT_LIST[cur_idx])
        continue

    # 이후에 나오지 않는 제품이라면 빼고
    # 그런 경우가 없다면 현재 시점 이후, 첫번째로 나오는 시점이 가장 늦는 제품을 뺀다.
    unplug_idx = -1
    save_last_idx = -1
    for plug_idx in range(len(plugged)):
        temp_last_idx = PRODUCT_NUM + 1  # 앞으로 나오지 않는 제품일 경우 대비
        for next_idx in range(cur_idx + 1, PRODUCT_NUM):
            if plugged[plug_idx] == PRODUCT_LIST[next_idx]:  # 앞으로 사용할 목록 중에 찾았다.
                temp_last_idx = next_idx
                break

        if save_last_idx < temp_last_idx:
            save_last_idx = temp_last_idx
            unplug_idx = plug_idx

    answer_count += 1
    plugged[unplug_idx] = PRODUCT_LIST[cur_idx]

print(answer_count)
