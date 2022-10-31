quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def selection_sort(list):
    list_len = len(list)

    for count in range(list_len - 1):
        max_val_idx = 0

        for i in range(list_len - count):
            if list[i] > list[max_val_idx]:
                max_val_idx = i

        list[list_len - 1 - count], list[max_val_idx] = (
            list[max_val_idx],
            list[list_len - 1 - count],
        )


print("Befor Sorting : ", quiz_list)

selection_sort(quiz_list)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
