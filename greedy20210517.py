n = int(input())

# 그러니까 정리를 해보면 
#  00시 00분 00초 부터 n시 59분 59초 안에 3이 몇번 들어가냐를 찾는거네 
# 그럼 00시 00분 00초 부터 00시 59분 59초 까지 3이 들어가는게 몇번인지 찾으면 되겠네
count = 0
time = ''
# 출력부터 해보자
for i3 in range(n+1):
    for i in range(60):
        for i2 in range(60):
            time  = str(i3) + str(i) + str(i2)
            if '3' in time:
                count += 1
# print(count * (n+1)) 내 생각으로는 그냥 00시 그렇게 생각했는데 
# 0시 1시 2시 3시 4시 5시 6번을 곱하면 된다고 생각했는데 아닌가

# 생각의 오류가 있다 3시 로 시작하면 모두다 포함해야한다
print(count)