"""
is_ok_on(nth_row) : 해당 row에 들어가 있는 값이 그 위의 row들에 대해서 공격받지 않는지 확인
    - 같은 열에 존재하는지 확인.
    - 대각선에 존재하는지 확인 => x 좌표 차이 와 y 좌표 차이가 두개 모두 다 동일하다면 대각선에 위치한다.
        -- 둘중에 한개라도 해당되면 놓으면 안되는 배치 => False 반환
        -- 둘 다 해당하지 않으면 놓아도 되는 배치 => True 반환

n_queen(nth_row) : 재귀를 타면서 총 n개의 queen이 배치 되었는지 확인
    - nth_row가 필요한 queen 수만큼이 되면 queen 을 모두 배치한 것이므로 재귀를 종료
    - 종료조건이 되지 않는다면, queen 배치를 바꿔가면서 is_ok_on 메서드를 호출하여 True가 Return 되면 재귀를 이어나간다. 
"""


def is_ok_on(nth_row):
    for i in range(nth_row):
        if (put_queen_each_row[nth_row] == put_queen_each_row[i]) or (
            nth_row - i == abs(put_queen_each_row[nth_row] - put_queen_each_row[i])
        ):
            return False

    return True


def n_queen(nth_row):
    global answer_count

    if nth_row >= needed_quene_num:
        answer_count += 1
        return

    for col in range(needed_quene_num):
        if not is_possible_put_queen_each_row[col]:
            continue

        put_queen_each_row[nth_row] = col

        if nth_row == 0:
            is_possible_put_queen_each_row[col] = False
            n_queen(nth_row + 1)
            is_possible_put_queen_each_row[col] = True

        elif is_ok_on(nth_row):
            is_possible_put_queen_each_row[col] = False
            n_queen(nth_row + 1)
            is_possible_put_queen_each_row[col] = True


needed_quene_num = int(input())

put_queen_each_row = [-1] * needed_quene_num
is_possible_put_queen_each_row = [True] * needed_quene_num

answer_count = 0

n_queen(0)

print(answer_count)
