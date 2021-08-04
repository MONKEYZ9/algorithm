# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.


# 먼저, 동적 계획법
# 반복문을 통한 방법
T = int(input())

fn = [0 for _ in range(T+1)]

fn[0], fn[1] = 0, 1

for i in range(2, T+1):
    fn[i] = fn[i-1] + fn[i-2]

print(fn[T])

# 재귀함수를 이용한 방법

def fibo(x):
    if x < 2:
        return x
    return fibo(x - 1) + fibo(x - 2)

T = int(input())
print(fibo(T))


# 재귀함수를 이용한 방법
# T = int(input())

# fn = [0 for _ in range(T+1)]

# def fibo(x):
#     fn[x] = fn[x-1] + fn[x-2]

#     return fibo(x)




# print(fibo(T))