N = int(input())
#  5가 찍히면
# 04시 59분 59초까지 

count = 0
for i in range(N+1):
    for i2 in range(60):
        for i3 in range(60):
            times = str(i)+ str(i2)+ str(i3)
            if '3' in times:
                count += 1
print(count)