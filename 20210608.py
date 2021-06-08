N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a를 정렬하는거야
a.sort()
# b도 정렬해야해
b.sort(reverse=True)

# k번 횟수만큼 바꿔야 해
for i in range(K):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))