N = int(input())

array = list(map(int, input().split()))

array.sort()

result = 0
array2 = []
for i in range(N):
    result += array[i]
    array2.append(result)
print(sum(array2))
