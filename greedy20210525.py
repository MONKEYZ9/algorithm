# N개의 회의에 대하여 회의실 사용표
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
#  단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다
n = int(input())

conference_times = []

for i in range(n):
  conference_time = tuple(map(int, input().split()))
  conference_times.append(conference_time)
# 새로운 튜플 안에 있는 것에 튜플을 다시 넣을 수 없다.
# 차라리 리스트에 넣어보자
# [(1, 4), (2, 3)]

# count = 0

# # 그럼 보자
# for i in conference_times:
#   if i[1] > i+1[0]:
#     continue
#   elif i[1] <= i+1[0]:
#     count += 1
# 리스트를 정렬을 해줘야해
conference_times.sort()
conference_times.sort(key=lambda x:x[1])
# print(conference_times)

count = 1

start, end = conference_times[0]
for i in conference_times[1:]:
  x,y = i
  if end <= x:
    end = y
    count += 1

print(count)
