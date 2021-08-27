N = int(input())

def factorial(N):
    if N == 1:
        return N
    return N * factorial(N-1)


if N == 0:
    print(1)
else:
    print(factorial(N))