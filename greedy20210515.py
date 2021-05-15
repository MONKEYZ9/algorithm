# 1이 될때까지 
# 어떤하느 수 N이 1이 될때까지 
# N - 1 하고 N // K 를 한다

N, K = map(int, input().split())

#  25, 5
# 를 받아서 빼고 나눠서 1을 만들자
# 그럼 최대한 많이 나누는게 중요할거 같다

# 25 // 5 = 5 
# 5 // 5 = 1

# 27 4 
# 27 - 1 - 1 - 1 = 24
# 24 // 4 = 6 
# 6 - 1 - 1 = 4 
# 4 // 4 = 1

# 27 3
# 27 // 3 = 9
# 9 // 3 = 3
# 3 // 3 = 1

# 일단 N이 K보다 크면 계속 나누고
# 작아지면 1을 빼자

# countN = 0
# countK = 0

# while True:
#     if N >= K:
#         N = N // K
#         countN += 1

#     elif N==1:
#         break
    
#     else:
#         N = N - 1
#         countN += 1
# print(countN)


# 이 코드는 나눠떨어지는 것을 생각하지 않는다 그러니까 나머지가 0일때를 고려하지 않은 것이다


countN = 0

while True:
    if N % K == 0:
        N = N // K
        countN += 1

    elif N==1:
        break
    
    else:
        N = N - 1
        countN += 1
print(countN)


