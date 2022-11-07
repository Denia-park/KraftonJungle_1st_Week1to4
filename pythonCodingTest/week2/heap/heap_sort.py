"""
힙 정렬 (Heap Sort) 이란 , 최대 힙 트리 or 최소 힙 트리를 구성해 정렬을 하는 방법
내림차순 정렬을 위해서는 최대 힙을 구성하고 오름차순을 정렬 위해서는 최소 힙을 구성하며 된다.
"""

# 최소힙으로 오름차순 정렬을 구현한다.
# 내림차순을 원한다면 아래 코드에서 부등호 방향만 반대로 바꾸자.


def heapify(list, root_node_idx, list_length):
    left_node_idx = root_node_idx * 2
    right_node_idx = root_node_idx * 2 + 1
    change_idx = root_node_idx  # 맨 처음에 바꿔야 하는 인덱스는 root_node_idx로 초기화

    if left_node_idx <= list_length and list[change_idx] > list[left_node_idx]:
        change_idx = left_node_idx

    if right_node_idx <= list_length and list[change_idx] > list[right_node_idx]:
        change_idx = right_node_idx

    if change_idx != root_node_idx:
        list[root_node_idx], list[change_idx] = (
            list[change_idx],
            list[root_node_idx],
        )
        return heapify(list, change_idx, list_length)


def heap_sort(target_list, list_after_sort):
    list_length = len(target_list)  # 전체 길이를 구한다. ->
    # 아래 코드에서 맨 앞에 0을 붙여주기 때문에 , 전체 길이로 시작을 해도 된다.

    new_target_list = [0] + target_list  # 인덱스를 0부터 시작하는 것보다 1부터 시작하는게 계산하기가 좋다.

    # min heap 생성
    for leaf_node_idx in range(list_length, 0, -1):  # 0은 사용되지 않기 때문에 0까지 범위를 잡는다.
        heapify(new_target_list, leaf_node_idx, list_length)

    # min element extract & heap
    for leaf_node_idx in range(list_length, 0, -1):
        root_node_idx = 1
        list_after_sort.append(new_target_list[root_node_idx])
        new_target_list[root_node_idx], new_target_list[leaf_node_idx] = (
            new_target_list[leaf_node_idx],
            new_target_list[root_node_idx],
        )
        heapify(new_target_list, root_node_idx, leaf_node_idx - 1)


answer_list = []

problem_list = [10, 8, 6, 7, 9, 3, 5, 1, 4, 2]
heap_sort(problem_list, answer_list)

print(answer_list)
