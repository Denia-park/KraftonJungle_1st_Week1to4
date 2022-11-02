quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def merge_sort(list):
    def _merge_sort(list, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(list, left, center)  # 배열 앞부분을 병합 정렬
            _merge_sort(list, center + 1, right)  # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = list[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= list[i]:
                    list[k] = buff[j]
                    j += 1
                else:
                    list[k] = list[i]
                    i += 1
                k += 1

            while j < p:
                list[k] = buff[j]
                k += 1
                j += 1

    n = len(list)
    buff = [None] * n  # 작업용 배열을 생성
    _merge_sort(list, 0, n - 1)  # 배열 전체를 병합
    del buff  # 작업용 배열을 소멸


print("Befor Sorting : ", quiz_list)

merge_sort(quiz_list)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
