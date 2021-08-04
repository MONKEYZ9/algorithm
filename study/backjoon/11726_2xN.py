n = int(input())

# 2 * 1 => 1
# 2 * 2 => 2
# 2* 3 => 3
# 2 * 4 => 5

# def getM(n):
#     if n <= 2:
#         return n
#     return (getM(n-1) + getM(n-2))%10007

# print(getM(n))

dp = []

dp.append(1)
dp.append(2)
for i in range(2, n):
    if n <= 2:
        print(n%10007)
    dp.append(dp[i-1] + dp[i-2])
print(dp[n-1]%10007)