# 1 1/1 0
# 2 1/2 2/1 1 
# 3 3/1 2/2 1/3 2 
# 4 1/4 2/3 3/2 4/1 3
# 5 5/1 4/2 3/3 2/4 1/5 4 
# 6 1/6 2/5 3/4 4/3 5/2 6/1 5
X = int(input())

if X == 1:
    print('1/1')
else:
    for n in range(1, X):
        fn = n*(n+1) // 2 + 1
        bn = (n+1)*(n+1+1) // 2

        if fn <= X <= bn:
            if n % 2 ==0:
                cn1 = X - fn
                cn2 = bn - X
                print(str(n+1-cn1)+'/'+str(n+1-cn2))
            else:
                cn1 = X - fn
                cn2 = bn - X
                print(str(n+1-cn2)+'/'+str(n+1-cn1))
            break



