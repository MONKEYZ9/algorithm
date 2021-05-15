# 먼저 배열을 찍자
n, m = map(int, input().split());

result = 0

for i in range(n):
    dataN = list(map(int, input().split()));
    # 현재줄에서 가장 작은걸 찾아라
    min_value = min(dataN)
    result = max(result, min_value)

print(result)