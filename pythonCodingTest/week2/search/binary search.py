quiz_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def bin_search(list, key):
    """
    ★ : 이진 검색에서는 검색 대상인 배열이 오름차순으로 정렬되어 있어야 한다.
    시퀀스 list에서 key 와 일치하는 원소를 이진 검색
    """
    pl = 0
    pr = len(list) - 1

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        center_value = list[pc]

        if center_value == key:
            return pc  # 검색 성공
        elif center_value < key:
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        elif center_value > key:
            pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘

        if pl > pr:
            break  # pl 이 pr 을 가로지르면 종료

    return -1  # 검색 실패


my_key = 5
search_idx = bin_search(quiz_list, my_key)
print(f"내가 찾는 값 {my_key} : {quiz_list[search_idx]}")

my_key = 8
search_idx = bin_search(quiz_list, my_key)
print(f"내가 찾는 값 {my_key} : {quiz_list[search_idx]}")

my_key = 11
search_idx = bin_search(quiz_list, my_key)
print(f"내가 찾는 값 {my_key} : {search_idx}")
