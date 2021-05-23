# 상근이가 설탕 공장 배달 중
# 상근이가 N킬로그램 배달해야하는데
# 봉지는 3 5가 있음
# 상근이가 최대한 적게 들고 가려고 함

# 예로 18한다고 하면 5 3개 3 1개로 

# 만약 정확하게 나눌 수 없다면 -1를 출력하게

n = int( input())
# 봉지 갯수
count = 0

while True:
   # 만약 5로 나눴을때 나눴는데 나머지가 있어 근데 3으로 나눠떨어지지 않으면 -1
   # 5로 나눴는데 나머지가 있어 그래서 3으로 나눠떨어지면 횟수로 쳐야지
   # 5또는 3으로 나눴는데 나머지가 없다.
   if n % 5 == 0: 
      #  그럼 5또는 3으로 나눴을때
      # 몫을 카운트에 넣어주자
      count = count + n // 5
      break
   # 3으로도 5로도 나눠떨어지지 않는다면 3을 빼서 보자
   else:
      n -= 3
      count += 1
      if n < 0:
         count = -1
         break
print(count)
      # 만약 3으로 계속 뺐는데 11-3=8-3=5/5=1 이런경우가 아니라
   # 4같이 4-3=1-3

   # 근데 나머지가 생기지 않는 경우잖아 어차피 나머지가 생겼을 경우
      # 똑같이 몫을 카운트에 넣어주되
      # count = count + n // bongi
      # # 나머지를 만들어주자
      # namugi = n % bongi
      # 나머지 값이 나눠지는지 봐야지
      # 만약 나눠지지 않는다면 

#      # 이렇게 하면 몫이 횟수가 되니까
#    # 나머지로 3을 나눌 수 있는지 없는지 확인해야해
#    namugi = n % bongi
#    print(namugi)
#    if namugi % 3 != 0:
#       count = -1
#       break
#    else:
#       n = namugi
# print(count)
# while True:
#        if n // bonggi_type[0] == 0:
#       count = count + n // bonggi_type[0]
#    else:
#       n = n % bonggi_type[0]
#       count = count + n // bonggi_type[0]


# 나누는건 의미가 없다.
# # 빼는거로 가야한다
# def minuc_o():
#    global n
#    n -= 5

# def minuc_sam():
#    global n
#    n -=3


# while True:
#    if n >= 5:
#       minuc_o
#       count += 1
#       if n < 5:
         
#          count = -1
#          break

