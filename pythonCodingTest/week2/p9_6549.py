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
스택의 꼭대기 원소(top)가 가리키는 index의 막대 높이보다 현재 막대의 높이가 작은 경우 현재 막대의 높이보다 크거나 같은 원소는 모두 삭제(pop)하고, 그 다음 현재 막대의 index를 넣는다.(push)

넓이는 ?
"현재 막대의 높이보다 크거나 같은 원소는 모두 삭제(pop)" 이 과정에서 삭제하면서 넓이를 구한다.
"""

# 스택


def get_area(len):
    global height_list
    my_stack = []

    max_area = 0

    for idx in range(len):
        #  이전 체인의 높이보다 현재 히스토그램 높이가 작거나 같을경우
        #  i번째 막대보다 작은 이전 체인들을 pop하면서 최대 넓이를 구해준다.

        while my_stack and height_list[my_stack[-1]] >= height_list[idx]:
            height = height_list[my_stack.pop()]  # 이전 체인의 높이

            # pop한 뒤 그 다음의 이전체인이 만약 없다면 0번째 index 부터 (i-1)번째 인덱스까지가
            # 유일한 폭이 된다. (폭은 i가 됨)
            # 반면 스택이 비어있지 않다면 이는 pop한 높이보다 더 작은 높이를 갖는
            # 체인이 들어있다는 것이므로 (i-1)번째 index에서 그 다음 이전 체인의 index를
            # 빼준 것이 폭이 된다.

            if not my_stack:
                width = idx
            else:
                width = idx - 1 - my_stack[-1]

            max_area = max(max_area, height * width)  # 최대 넓이 값 갱신

        my_stack.append(idx)

    # 위 과정이 끝나고 Stack에 남아있는 체인들이 존재할 수 있으므로 나머지도 위와같은 과정을 거친다.
    while my_stack:
        height = height_list[my_stack.pop()]

        # 만약 pop하고 난 뒤 스택이 비어있다면 이는 남아있는 체인이 없다는 뜻이고
        # 고로 0 ~ (len - 1) 까지인 전체 폭이 width가 되는 것이다.

        if not my_stack:
            width = len
        else:
            width = len - 1 - my_stack[-1]

        max_area = max(max_area, height * width)  # 최대 넓이 값 갱신

    return max_area


while True:
    quiz_list = list(map(int, sys.stdin.readline().split()))

    n = quiz_list[0]

    if n == 0:
        break

    height_list = quiz_list[1:]

    print(get_area(n))
