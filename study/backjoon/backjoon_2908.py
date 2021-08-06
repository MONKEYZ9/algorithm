n, m = input().split()

re_n, re_m = n[-1::-1], m[-1::-1]

if re_n > re_m:
    print(re_n)
else:
    print(re_m)
