N = int(input())

road =  list(map(int, input().split()))

price = list(map(int, input().split()))


# 처음 도시에서는 길이 만큼 곱해서 가야해
answer = 0

answer += road[0] * price[0]
# 이거는 무조건 해야해 그래야 갈 수 있어 다음도시로
# 두번째 도시에서 3번째 도시로 갈건데 이때 첫번째 도시의 기름이 더 싸면 첫번째 도시에서 넣고 아니라면 2번째 도시에서 넣어야 해
for i in range(0,N-2):
  if price[i] >= price[i+1]:
    answer += price[i+1] * road[i+1]
  else:
    answer += price[i] * road[i+1]


print(answer)

# for i in range(0,N-2):
#       if price[i+1] > price[i]:
#     answer += price[i] * road[i+1]
#   else:
#     answer += price[i+1] * road[i+1]   