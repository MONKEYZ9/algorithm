a = [0,0] + [1]*(123456)

for i in range(2,123457):
  if a[i]:
    for j in range(2*i, 123457, i):
        a[j] = 0
print(a)

# while True:
#     cnt = 0
#     n = int(input())
#     if n == 0:
#         break
#     for i in range(n+1, (2*n)+1):
#         if i in primes:
#             cnt+=1
#     print(cnt)