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

# 집의 수 , 설치해야 하는 공유기 수 초기화
house_num, wifi_num = list(map(int, sys.stdin.readline().split()))
# 집들의 x 좌표 List
distance_list = []
# for문을 돌면서 x 좌표를 저장
for i in range(house_num):
    distance_list.append(int(input()))

# x 좌표들을 정렬
distance_list.sort()

# 공유기의 설치 간격은 시작 집 , 끝 집 의 거리를 기준으로 잡음
start_distance = distance_list[0]
end_distance = distance_list[-1]

# 공유기 설치 최대 간격은 0으로 초기화
max_distance = 0

# 이분 탐색을 진행하는데 항상 조건은 시작점이 끝점을 지나치기 전까지 진행한다.
while start_distance <= end_distance:
    # 공유기 설치 거리는 시작 집, 끝 집 거리 차이의 절반으로 시작
    wifi_distance = (start_distance + end_distance) // 2
    # 집들간의 거리를 최대로 하기 위해서는 시작 집에다가 설치를 해야함
    pre_house_distance = distance_list[0]
    # 시작 집에 설치를 했으므로 일단 공유기 설치 대수는 1부터 시작
    wifi_count = 1

    # for문을 돌면서 공유기 설치 집들 사이의 간격을 비교한다.
    for idx in range(1, len(distance_list)):
        cur_house_distance = distance_list[idx]

        # 우리가 정한 공유기 설치 거리를 넘는 집들은 공유기 설치 가능
        if (cur_house_distance - pre_house_distance) >= wifi_distance:
            # 공유기 설치 대수 + 1
            wifi_count += 1
            # 공유기 설치 했으므로 다음 집 과 비교할 때 기준이 된다.
            pre_house_distance = distance_list[idx]

    # 공유기 설치 대수가 우리가 정한 대수 이상이면 해당 거리는 가능
    if wifi_count >= wifi_num:
        # 기존에 정한 거리보다 현재 거리가 더 크면 기존에 정한 거리를 현재의 값으로 업데이트
        if max_distance < wifi_distance:
            max_distance = wifi_distance

        # 거리를 더 늘려서 다시 확인을 해야 하므로 start_distance 를 수정
        start_distance = wifi_distance + 1
    else:
        # 거리를 더 좁혀서 다시 확인을 해야 하므로 end_distance 를 수정
        end_distance = wifi_distance - 1

# 최대 거리를 print
print(max_distance)
