#  일단 N과K를 받아야지
# n, k = map(int, input().split())
# coin = 0
# coin_List = []
# while True:
#    if coin == 50000:
#       break
#    coin = int(input())
#    coin_List.append(coin)

# coin_List.reverse()

# count = 0
# for ans in coin_List:
#    while k >= ans:
#       count += 1
#       k -= ans      
# print(count)
# 이렇게 하면 런타임 오류가 난다 너무 오래 걸린다는 건가


# n, k = map(int, input().split())
# coin = 0
# coin_List = []
# while True:
#    if coin == 50000:
#       break
#    coin = int(input())
#    coin_List.append(coin)

# coin_List.reverse()

# count = 0
# for ans in coin_List:
#    if k == 0:
#       break
#    count+=k//ans
#    k%=ans
# print(count)
#동전과 값 입력받기
n,k=map(int,input().split())
#동전을 입력받을 리스트 초기화하기
coin=[]

#동전 종류 입력받기
for i in range(n):
  coin.append(int(input()))

#동전개수 셀 변수 초기화
count = 0

#동전 내림차순으로 정렬하기
coin.reverse()

#동전 개수 구하기
for i in coin:
  if k == 0:
     break
  count += k // i
  k %= i


print(count)