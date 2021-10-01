import sys

# N = int(input())
# for i in range(1, 10):
#     print(f'{N} * {i} = {N*i}')

# for _ in range(N):
#     A, B = map(int, sys.stdin.readline().rstrip().split())
#     print(A + B)

# print(int(N*(N+1)/2))

# for i in range(1, N+1):
#     A, B = map(int, sys.stdin.readline().rstrip().split())
#     print(f"Case #{i}: {A} + {B} = {A+B}" )


# for i in range(1, N+1):
#     print(f"{' '*(N-i)}{'*'*i}")

N, X = map(int, (input().split()))
a_list = list(map(int, (input().split())))
strA = ''
for i in a_list:
    if i < X:
        strA += str(i) + ' '
print(strA)
