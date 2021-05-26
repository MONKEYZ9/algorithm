# N(1 ≤ N ≤ 100,000)개의 로프가 있다. 
# 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 
# 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. 
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

N = int(input())
# 로프 두개를 받자
ropes = []

for rope in range(N):
  rope = int(input())
  ropes.append(rope)

# rope들 중 가장 작은 수를 뽑아내고
# 그걸 rope 갯수대로 곱하면 들 수 있는 총 무게

# min_rope = min(ropes)
# print(min_rope)
# answer = min_rope * N

# print(answer)

# 내가 구한건 최대 중량이 아니라 최소 중량이구나

ropes.sort(reverse=True)

# 각각의 무게를 담는 리스트 만들자
weight = []
# 각각의 무게를 다시 한번 체크 해봐야지
for i in range(len(ropes)):
  weight.append(ropes[i] * (i+1))

print(max(weight))
