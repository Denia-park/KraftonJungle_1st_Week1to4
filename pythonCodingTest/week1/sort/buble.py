quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def buble_sort(list):
    for count in range(len(list) - 1):
        for idx in range(len(list) - count - 1):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]


print("Befor Sorting : ", quiz_list)

buble_sort(quiz_list)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
