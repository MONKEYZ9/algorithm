N, M = map(int, input().split())
# 각 행 에서 가장 작은 것들 중 가장 큰거


# 행렬을 받자
# # 행렬 안 배열
# hangrul = []
# for i in range(N):
#   hangrul2 = list(map(int, input().split()))
#   hangrul.append(hangrul2)

# hangrul.sort()
# # 행렬 중 가장 작은 배열을 뽑아내고 거기서 가장 큰걸 뽑아내면 되지
# print(hangrul)
# print(min(hangrul))
# print(max(min(hangrul)))


# 답을 보고 깨달은 것
# 애초에 뽑아낼 때 가장 작은 것들을 묶어주고
# 그 중에서 가장 큰걸 뽑아주면 되네
result = 0
for i in range(N):
  data = list(map(int, input().split()))

  # 여기서 가장 작은걸 따로 저장하자
  min_data = min(data)

  # 결과 값에다가 결과 값과 비교해서 넣어주면 돼
  result = max(result, min_data)

print(result)