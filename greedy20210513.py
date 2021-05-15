# 큰 수의 법칙
n, m, k = map(int, input().split());

# 자연수가 N개로 주어진다... 이 말은 그냥 data라고 하고 빈 리스트를 만든다고 생각하면 된다
dataN = list(map(int, input().split()));

# dataN을 정렬해주자
dataN.sort();
# dataN.reverse();

# 그리고 가장 큰수가 뭔지 그다음으로 작은 수가 뭔지 정해놓자
first = dataN[n - 1]
second = dataN[n - 2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)