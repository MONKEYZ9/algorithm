A, B, V = map(int, input().split())
# 5  2-1 * n + 2  n은 3


# 6 = 5-1 * n + 5 n은 1

# V <= (A-B) *n + A
# (V-A)/(A-B) <= n
# if V == A:
#     print(1)
# else:    
#     if (V-A)//(A-B) <= 1:
#         print((V-A)//(A-B)+2)
#     else:
#         print((V-A)//(A-B)+1) 
if V == A:
    print(1)
else:    
    if (V-A)%(A-B) == 0:
        print((V-A)//(A-B)+1)
    else:
        print((V-A)//(A-B)+2) 