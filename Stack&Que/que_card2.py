from collections import deque
# N개의 카드
N = int(input())

n_list = [i for i in range(1, N+1)]
deque_n_list = deque(n_list)
print(deque_n_list)

for i in range(N-1):
    # 첫번째 숫자 기억
    first_n = deque_n_list[1]

    deque_n_list.popleft()
    deque_n_list.popleft()
    
    deque_n_list.append(first_n)
print(deque_n_list)

# 6
# 123456

# 23456
# 34562

# 4562
# 5624

# 624
# 246

# 46
# 64

# 6
# 4

# 먼저 인덱스를 지정해놓고 값을 옮겨주는 방법으로 간다..? => 시간복잡도가 너무 높다

# 그냥 맨 뒤를 leftpop으로 지우고 append해주는 방법으로가자
# deque의 