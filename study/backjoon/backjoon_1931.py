n = int(input())

conference_times = []

for i in range(n):
  conference_time = tuple(map(int, input().split()))
  conference_times.append(conference_time)

conference_times.sort()
conference_times.sort(key=lambda x:x[1])

cnt = 1
s, e = conference_times[0]

for n_s, n_e in conference_times[1:]:
  if e <= n_s:
    cnt += 1
    e = n_e
print(cnt)
