N = int(input())
n_list = list(map(int, input().split()))
cnt = 0
for i in n_list:
    if i == 1:
        pass
    elif i == 2:
        cnt += 1
    else:
        for j in range(2, i-1):
            if i % j == 0:
                break
        else:
            cnt += 1
print(cnt)

        
# print(8**(1/2))

# for i in range(round(8**(1/2))):
#     print(i)

# for j in range(2s1/2)))