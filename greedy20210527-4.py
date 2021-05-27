# 1이 될때까지
N, K  = map(int, input().split())
# 17 - 1 = 16 / 4 = 4 / 4 = 1
# N을 K로 나눴을때 나머지가 0이면 나누고 세고 
# 아니면 1을 빼면 되겠네
count = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        count += 1
        N //= K
    else:
        count += 1
        N -= 1
print(count)