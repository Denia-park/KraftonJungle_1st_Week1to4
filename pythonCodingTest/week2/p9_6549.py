import sys

"""
n = input()  #2
a = [sys.stdin.readline() for i in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""

# 정답 참고
# https://st-lab.tistory.com/255

"""
가운데를 기준으로 분할하여 풀이 할 때 아래 4가지 과정만 유의하여 작성하면 된다. (구간 범위 [lo : hi])

1. 가운데 위치를 구한다. ( mid = (lo + hi) / 2 )

2. 가운데 위치를 기준으로 분할하여 왼쪽 구간의 넓이([lo : mid])와 오른쪽 구간의 넓이([mid : hi])를 구한다.

3. 왼쪽과 오른쪽 중 큰 넓이를 변수에 저장한다.

4. 변수에 저장된 넓이와 두 구간을 합친 구간([lo : hi])의 가장 큰 넓이를 구해 두 개 중 가장 큰 넓이를 반환한다.
"""

# 분할 정복


def get_mid_area(lo, hi, mid):
    global height_list

    to_left = mid  # 중간 지점으로부터 왼쪽으로 갈 변수
    to_right = mid  # 중간 지점으로부터 오른쪽으로 갈 변수

    height = height_list[mid]  # 높이

    # 초기 넓이 (구간 폭이 1)
    max_area = height * 1

    def get_max_area(max_area, height, to_left, to_right):
        return max(max_area, height * (to_right - to_left + 1))

    # 양 끝 범위를 벗어나기 전까지 반복
    while lo < to_left and to_right < hi:
        # 양쪽 다음칸의 높이 중 높은 값을 선택
        # 갱신되는 height는 기존 height보다 작거나 같은 값

        if height_list[to_left - 1] < height_list[to_right + 1]:
            to_right += 1
            height = min(height, height_list[to_right])
        else:
            to_left -= 1
            height = min(height, height_list[to_left])

        # 최대 넓이 갱신
        max_area = get_max_area(max_area, height, to_left, to_right)

    while to_right < hi:
        to_right += 1
        height = min(height, height_list[to_right])
        max_area = get_max_area(max_area, height, to_left, to_right)

    while lo < to_left:
        to_left -= 1
        height = min(height, height_list[to_left])
        max_area = get_max_area(max_area, height, to_left, to_right)

    return max_area


def get_area(lo, hi):
    global height_list

    # 막대 폭(넓이)이 1일경우 높이가 넓이가 되므로 바로 반환
    if lo == hi:
        return height_list[lo]

    # 1번 과정
    mid = (lo + hi) // 2  # 중간 지점

    # 2번 과정
    # mid를 기점으로 양쪽으로 나눈다.
    # 양쪽 구간 중 큰 넓이를 저장한다.
    # 왼쪽 : lo ~ mid
    # 오른쪽 : mid + 1 ~ hi

    left_area = get_area(lo, mid)
    right_area = get_area(mid + 1, hi)

    # 3번 과정
    max_area = max(left_area, right_area)

    # 4번 과정
    # 반드시 분할되어 구해진 넓이가 최대값이라는 보장이 없다 => 양쪽 구간을 합친 구간내에서
    # mid를 기준으로 양쪽으로 뻗어나가면서 두 구간 사이의 겹친 넓이를 탐색해야함

    max_area = max(max_area, get_mid_area(lo, hi, mid))

    return max_area


while True:
    quiz_list = list(map(int, sys.stdin.readline().split()))

    n = quiz_list[0]

    if n == 0:
        break

    height_list = quiz_list[1:]

    print(get_area(0, len(height_list) - 1))
