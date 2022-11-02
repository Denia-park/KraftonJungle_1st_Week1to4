quiz_list = [10, 8, 7, 4, 3, 9, 6, 5, 2, 1]

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def heap_sort(list):
    def down_heap(list, left, right):
        temp = list[left]  # 루트

        parent = left

        while parent < (right + 1) // 2:
            cl = parent * 2 + 1  # 왼쪽 자식
            cr = cl + 1  # 오른쪽 자식
            child = cr if cr <= right and list[cl] < list[cr] else cl  # 큰 값을 선택
            if temp >= list[child]:
                break
            list[parent] = list[child]
            parent = child

        list[parent] = temp

    n = len(list)

    for i in range((n - 1) // 2, -1, -1):
        down_heap(list, i, n - 1)  # list[i] ~ list[n-1]을 힙 만들기

    for i in range(n - 1, 0, -1):
        list[0], list[i] = list[i], list[0]  # 최댓값인 list[0] 와 마지막 원소를 교환
        down_heap(list, 0, i - 1)  # list[0] ~ list[i-1] 을 힙으로 만들기


print("Befor Sorting : ", quiz_list)

heap_sort(quiz_list)

print("After Sorting : ", quiz_list)

print(answer_list)
print("Sort Result :", quiz_list == answer_list)
