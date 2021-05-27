# 큰수의 법칙
N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))
# 문제를 다시 해석하면
# 총 더하는 횟수는 M
# 하나의 수가 K번을 초과해서 더해질 수 는 없어
# N은 number의 크기

# 그럼 일단 큰거로 배열을 정리해줘야 겠다

numbers.sort(reverse=True)

# 다 더했을때 답을 배출해줘야 해
answer = 0
# 더하는 횟수가 K를 초과할 수 없어
plusSu = 0
# 총 더하는 횟수가 M
for i in range(M):
  if K > plusSu:
    plusSu += 1
    answer += numbers[0]
  else:
    plusSu = 0
    answer += numbers[1]
print(answer)

  
