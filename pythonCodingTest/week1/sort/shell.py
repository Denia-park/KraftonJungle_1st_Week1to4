quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def shell_sort(list):
    list_len = len(list)
    h = list_len // 2

    while h > 0:
        for i in range(h, list_len):
            j = i - h
            tmp = list[i]
            while j >= 0 and list[j] > tmp:
                list[j + h] = list[j]
                j -= h
            list[j + h] = tmp
        h //= 2


print("Befor Sorting : ", quiz_list)

shell_sort(quiz_list)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
