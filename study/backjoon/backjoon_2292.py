N = int(input())

# print((N+1)//6)
# print((N+1)%6)
# 1 1
# 2-7 5 2 5 (6-1) 2(1+1) 7(1+6)
# 8-19 11 6 12  8 (1+1+6) 19 (1+6+12)
# 20-37 17 12 18 20 (1+1+6+12) 37 (1+6+12+18)
# 38-61 23 18 24 38 (1+1+6+12+18) 61 (1+6+12+18+24)
# 62-91 29 6 29 (30-1) 30 36

f_n = 2
b_n = 1
cnt = 1
if N == 1:
    print(cnt)
else:
    while True:
        f_n = 1 + b_n
        b_n = f_n + (6*cnt-1)
        # print(f_n, '...', b_n)
        cnt += 1
        if f_n <= N <= b_n:
            break
    print(cnt)