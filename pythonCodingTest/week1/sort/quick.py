quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list.append


def quick_sort(list, start_cursor, end_cursor):
    pl = start_cursor
    pr = end_cursor
    pivot_idx = (start_cursor + end_cursor) // 2

    while pl <= pr:
        while list[pl] < list[pivot_idx]:
            pl += 1
        while list[pr] > list[pivot_idx]:
            pr -= 1

        if pl <= pr:  # 조건문 추가
            list[pl], list[pr] = list[pr], list[pl]
            pl += 1
            pr -= 1

    if start_cursor < pr:  # 조건문 추가
        quick_sort(list, start_cursor, pr)
    if pl < end_cursor:  # 조건문 추가
        quick_sort(list, pl, end_cursor)


print("Befor Sorting : ", quiz_list)

quick_sort(quiz_list, 0, len(quiz_list) - 1)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
