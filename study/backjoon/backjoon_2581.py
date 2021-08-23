m= int(input())
n= int(input())

a = [0,0] + [1]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    if i >= m:
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = 0
if primes == []:
    print(-1)
else:
    print(sum(primes),primes[0], sep='\n')