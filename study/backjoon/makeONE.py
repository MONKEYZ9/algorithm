# X = int(input())

# while X != 1:
#     if X % 3 == 0:
#         X //= 3
#         count += 1
#     elif X % 3 == 2:
#         X -= 1
#         count += 1
#         if X % 3 == 0:
#             X //= 3
#             count += 1
#     elif X % 3 == 1:
#         X -= 1
#         count += 1
# print(count)

n = int(input())

# 해당 값이 뭐 어떻게 구성될지 일단 0으로 쫙
dp = [0 for _ in range(n+1)]


for i in range(2, n+1):
    # 1을 뺐을때 5 -> 5 - 1 = 4가 됨으로 4의 횟수에 +1만하면 된다.
    # 처음에 바로 그전값보다 1을 더해준다.
    dp[i] = dp[i-1] + 1

    # 2로 나눠지거나, 해당 i의 배열값이 2로 나눈거보다 1더한거보다 크다면
    # 바로 dp[i-1] + 1보다 dp[i//2] + 1 이 더 크게 되면 2로 나누기전에 1로 뺀걸 뜻하게 된다.
    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1

    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
print(dp[n])