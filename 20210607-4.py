N = int(input())

dataN = []
for i in range(N):
    dataN.append(int(input()))
dataN = sorted(dataN, reverse=True)

for i in dataN:
    print(i, end=' ')
