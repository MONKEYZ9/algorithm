# 책 거스름돈 문제
coins = [ 500,100,50,10]
# 거스름돈 N
N = int(input())
# 동전갯수
count = 0
for coin in coins:
  while N >= coin:
    N -= coin
    count += 1
print(count)