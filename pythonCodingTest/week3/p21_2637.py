from collections import deque
import sys

sys.setrecursionlimit(10**6)

"""
n = input()  #2
a = [sys.stdin.readline() for _ in range(n)]  
# a = ["1 2 3", "4 5 6"]

n = input()  #2
q = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# q = [[472], [385]]

q = list(map(int, sys.stdin.readline().split()))
# q = [1, 2, 3, 4, 5]
"""
# 정답 참고
# https://dreamtreeits.tistory.com/155


def is_default_part(cur_part_idx):
    for idx in range(1, FINISH_NUM):
        if needs[cur_part_idx][idx] != 0:
            return False

    return True


FINISH_NUM = int(input())
LINE_NUM = int(input())

part_data_infos = [[] for _ in range(FINISH_NUM + 1)]
needs = [[0] * (FINISH_NUM + 1) for _ in range(FINISH_NUM + 1)]
indegree = [0] * (FINISH_NUM + 1)
my_q = deque()

for _ in range(LINE_NUM):
    next_part_idx, cur_part, need_num = list(map(int, sys.stdin.readline().split()))
    # 어떤 중간 부품을 만드는 데 어떤 부품들이 필요하다 의 접근이 아니라
    # 어떤 부품으로 어떤 중간 부품을 만드는지에 대해서 테이블을 작성
    part_data = (next_part_idx, need_num)
    part_data_infos[cur_part].append(part_data)
    indegree[next_part_idx] += 1  # next_part 는 필요한 부품 종류가 몇개인지 저장 => 기본 부품들을 찾기 위함

# 다른 부품 없이 만들 수 있는 기본 부품들을 큐에 넣고
# 해당 부품들을 대상으로 필요한 부품들을 업데이트 해서 최종 완제품에 도달하자.
for part_idx in range(1, FINISH_NUM + 1):
    if indegree[part_idx] == 0:
        my_q.append(part_idx)

# 큐를 돌면서 순차적으로 필요한 부품들을 업데이트 하자.
while my_q:
    cur_part_idx = my_q.popleft()

    # part_data_infos 에서 cur_part_idx 를 확인하면
    # 현재 부품을 몇개 사용해서 어떤 다음 부품을 만들 수 있는지 확인이 가능함.
    for info in part_data_infos[cur_part_idx]:
        next_part_idx, cur_part_need_num = info

        # 기본 부품이면 그냥 needs[next_part_idx][cur_part_idx] 에 추가하기.
        # 중간 부품이면 기본 부품들의 수량을 필요한 수만큼 곱해서 더해주기
        # 기본 부품들을 다 돌면서 추가하기 위해서 for문이 필요함
        if is_default_part(cur_part_idx):
            needs[next_part_idx][cur_part_idx] += cur_part_need_num
        else:
            for temp_idx in range(1, FINISH_NUM):
                needs[next_part_idx][temp_idx] += (
                    needs[cur_part_idx][temp_idx] * cur_part_need_num
                )

        # 기본 부품들의 내용을 needs로 업데이트 했기 때문에 indegree 의 값을 1 빼준다.
        indegree[next_part_idx] -= 1

        # indegree가 0이 됐으면 더 이상 영향을 받는 부품이 없기 때문에
        # my_q 에 넣어서 계산을 시작한다.
        if indegree[next_part_idx] == 0:
            my_q.append(next_part_idx)

# 모든 부품들의 내용이 다 업데이트가 되었으면
# 최종 완성품에 필요한 부품들도 다 업데이트가 된 것임

# 그러므로 needs 에 최종 완성품 인덱스를 확인하면
# 몇개의 기본 부품들이 필요한지 확인이 가능
# 중간 부품인 애들을 모두 기본 부품으로 변경했기 때문에 0인 애들만 제외하고 출력한다.
for idx in range(1, FINISH_NUM):
    if needs[FINISH_NUM][idx] != 0:
        print(f"{idx} {needs[FINISH_NUM][idx]}")
