T = int(input())

dp = [1,2,4]
n_list = []

for i in range(T):
    n_list.append( int(input()) )

for i in range(3, int(n_list[i])):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in n_list:
    print(dp[i])


T = int(input())

dp = {2: 2, 3 : 4, 4 : 7}

for i in range(5, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for _ in range(T):
    n = int(input())
    print(dp[n])

# 구현으로 다가가면
# 일단 1만 쭉 더하는건 

# 6 => 24
# 1 1 1 1 1 1 * 1
# 1 1 1 1 2 * 5
# 1 1 1 3 * 4
# 1 1 2 2 * 6
# 1 2 3 * 6
# 2 2 2 * 1 
# 3 3 * 1


# 5 = > 13
# 1 1 1 1 1 * 1
# 1 1 1 2 * 4
# 1 1 3 * 3
# 2 1 2 * 3
# 2 3 * 2


# 4  => 7
# 1 1 1 1 * 1
# 1 1 2 * 3
# 1 3 * 2
# 2 2 * 1


# 3 => 4
# 1 1 1 * 1
# 1 2 * 2
# 3 * 1

# 2 => 2
# 1 1
# 2

# 1 => 1
