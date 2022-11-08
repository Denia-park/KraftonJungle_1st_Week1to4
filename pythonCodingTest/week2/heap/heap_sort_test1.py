def heapify(target_list, root_node_idx, list_length):
    left_node_idx = root_node_idx * 2
    right_node_idx = root_node_idx * 2 + 1

    change_idx = root_node_idx

    if (
        left_node_idx <= list_length
        and target_list[change_idx] > target_list[left_node_idx]
    ):
        change_idx = left_node_idx

    if (
        right_node_idx <= list_length
        and target_list[change_idx] > target_list[right_node_idx]
    ):
        change_idx = right_node_idx

    if change_idx != root_node_idx:
        target_list[root_node_idx], target_list[change_idx] = (
            target_list[change_idx],
            target_list[root_node_idx],
        )
        heapify(target_list, change_idx, list_length)


def heap_sort(target_list, list_after_sort):
    list_length = len(target_list)
    new_target_list = [0] + target_list  # 0을 추가함으로써 idx 계산을 편하게 할 수 있음

    # leaf Node 부터 모두 최소 heap 상태로 정렬한다.
    for idx in range(list_length, 0, -1):
        temp_root_node_idx = idx
        heapify(new_target_list, temp_root_node_idx, list_length)

    for idx in range(list_length, 0, -1):
        root_node_idx = 1
        root_value = new_target_list[root_node_idx]
        list_after_sort.append(root_value)

        last_node_idx = idx
        new_target_list[root_node_idx], new_target_list[last_node_idx] = (
            new_target_list[last_node_idx],
            new_target_list[root_node_idx],
        )
        heapify(new_target_list, root_node_idx, last_node_idx - 1)


answer_list = []

problem_list = [10, 8, 6, 7, 9, 3, 5, 1, 4, 2]
heap_sort(problem_list, answer_list)
print(answer_list)
