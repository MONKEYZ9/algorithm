coins = [500, 100, 50, 10, 5, 1]

charge_money = 1000 - int(input())
# taro_money = 1000
# changes = taro_money - price
# count = 0

# for coin in coins:
#   while True:
#     if changes >= coin:
#       changes -= coin
#       count += 1
#     else:
#       break
# print(count)


# 재귀로 풀어봐라
def calc_coin(i, coins, charge_money):
    if i == len(coins):
        return 0
    cnt = 0
    cnt = cnt + charge_money // coins[i]

    return cnt + calc_coin(i+1, coins, charge_money % coins[i])
print(calc_coin(0, coins, charge_money))