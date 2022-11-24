from heapq import heappush, heappop

# 정답 참고
# https://yunny-p.tistory.com/m/entry/1379

n = int(input())
end_time_priority_que = []
lect_num_room = [0] * (n + 1)
lect_info_list = []

for _ in range(n):
    lect_num, start, end = map(int, input().split())
    lect_info_list.append([start, end, lect_num])

lect_info_list = sorted(lect_info_list, key=lambda x: (x[0]))

room_num = 0

for cur_start, cur_end, cur_lect_num in lect_info_list:
    if end_time_priority_que:
        first_end_lecture = end_time_priority_que[0]
        first_end_time = first_end_lecture[0]
        if first_end_time <= cur_start:
            occupied_lect_num = first_end_lecture[2]

            lect_num_room[cur_lect_num] = lect_num_room[occupied_lect_num]
            heappop(end_time_priority_que)
        else:
            room_num += 1
            lect_num_room[cur_lect_num] = room_num
    else:
        room_num += 1
        lect_num_room[cur_lect_num] = room_num

    heappush(end_time_priority_que, [cur_end, cur_start, cur_lect_num])

print(room_num)
for i in lect_num_room[1:]:
    print(i)
