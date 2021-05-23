
#  일단 받은 리스트를 만들어서 해결하자
# p를 배열을 정리하자

# 걸리는 시간을 순서대로 더하게 하는게 중요하네

def solution():
   time = 0
   alltime = 0
   for customer in p:
      time = time + customer
      alltime += time
   print(alltime)

n = int(input())
p = list(map(int, input().split()))
p.sort()
solution()