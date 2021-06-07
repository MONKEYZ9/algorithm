# stack = []

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop() # 끝에 수를 지워주는 것으로 알고 있다.

# print(stack)
# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(list(queue))
# queue.reverse()
# print(queue)

def recursive_funtion(i):
    if i == 10:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출한다')
    recursive_funtion(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

# recursive_funtion(1)

def factorial_funtion(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(result)
    print(result)
    return result


# factorial_funtion(5)



def fatorical_recursive(n):
    if n <= 1:
        return 1
    # n! = n*n(n-1)!를 그대로 코드로 작성하기
    return n * fatorical_recursive(n-1)
# print(fatorical_recursive(2))
# print(fatorical_recursive(3))
# print(fatorical_recursive(4))
# print(fatorical_recursive(5))


INF = 999999999
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
    ]
# print(graphdlsqwjq)
