quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def insertion_sort(list):
    list_len = len(list)

    for start_idx in range(1, list_len):
        start_val = list[start_idx]

        change_idx = start_idx

        for cur_idx in range(start_idx - 1, -1, -1):
            if start_val < list[cur_idx]:
                list[cur_idx + 1] = list[cur_idx]
                change_idx = cur_idx
            else:
                break

        list[change_idx] = start_val


print("Befor Sorting : ", quiz_list)

insertion_sort(quiz_list)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
