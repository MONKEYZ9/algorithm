import sys
# while True:
#     try:
#         A, B = map(int, sys.stdin.readline().rstrip().split())
#         if 0 < A < 10 or 0 < B < 10:
#             print(A + B)
#         else:
#             break
#     except:
#         break

# 26
N = input()
count = 0
if len(N) < 2:
    N = '0'+N
    start = str(int(N[0]) + int(N[1]))
    next_N = N[1] + start[-1]
    while True:    
        if N == next_N:
            count += 1
            break
        else:
            start = str(int(next_N[0]) + int(next_N[1]))
            next_N = next_N[1] + start[-1]
            count += 1

    print(count)
else:
    start = str(int(N[0]) + int(N[1]))
    next_N = N[1] + start[-1]
    while True:    
        if N == next_N:
            count += 1
            break
        else:
            start = str(int(next_N[0]) + int(next_N[1]))
            next_N = next_N[1] + start[-1]
            count += 1

    print(count)
