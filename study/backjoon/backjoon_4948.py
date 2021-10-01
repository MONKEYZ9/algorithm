
def get_prime(n):
  a = [0,0] + [1]*(n*2)

  for i in range(2,(n*2)):
    if a[i]==1:
      for j in range(2*i, (n*2)+1, i):
          a[j] = 0
  return a

while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    else:
      a = get_prime(n)
      for i in range(n+1, (2*n)+1):
          if a[i] == 1:
              cnt+=1
      print(cnt)



# a = [0,0] + [1]*(1234567*2)

# for i in range(2,(1234567*2)):
#   if a[i]==1:
#     for j in range(2*i, (1234567*2), i):
#         a[j] = 0

# while True:
#     cnt = 0
#     n = int(input())
#     if n == 0:
#         break
#     for i in range(n+1, (2*n)+1):
#         if a[i] == 1:
#             cnt+=1
#     print(cnt)