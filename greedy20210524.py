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


n, k = map(int, input().split())
coin = 0
coin_List = []
while True:
   if coin == 50000:
      break
   coin = int(input())
   coin_List.append(coin)

coin_List.reverse()

count = 0
for ans in coin_List:
   if k == 0:
      break
   count += 1
   k -= ans
print(count)


