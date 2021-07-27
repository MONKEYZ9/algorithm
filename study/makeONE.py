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

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
        
print(dp[n])