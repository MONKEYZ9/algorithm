from collections import deque

# 1 2 3 4 5 6
# 첫번째 방법
# _ 2 3 4 5 6
# 왼쪽으로 움직이기
# 2 3 4 5 6 1
# 오른쪽으로 움직이기
# 6 1 2 3 4 5


# 큐의 크기가 10이면
# 1 2 3 4 5 6 7 8 9 10 이렇게 있는데

# 2 3 4 5 6 7 8 9 10 1 1
# 3 4 5 6 7 8 9 10 1 2
# 4 5 6 7 8 9 10 1 3 3
# 5 6 7 8 9 10 1 3 4 4
# 6 7 8 9 10 1 3 4 5 5
# 7 8 9 10 1 3 4 5 6 6
# 8 9 10 1 3 4 5 6 7 7
# 9 10 1 3 4 5 6 7 8 8
# 10 1 3 4 5 6 7 8 
# 1 3 4 5 6 7 8 10 
# 3 4 5 6 7 8 10 1 
# 4 5 6 7 8 10 1 3 
# 5 6 7 8 10 1 3 4 
# 6 7 8 10 1 3 4 


# 해당 원소의 인덱스를 뽑아내고
# 그리고 그 인덱스와 첫번째와 마지막인덱스를 비교하고 어디에 더 가까운지 보고
# 가까운 쪽으로 가자
# 1 2 3 4 5 6 7 8 9 10
# 2 3 4 5 6 7 8 9 10 1 -1
# 3 4 5 6 7 8 9 10 1
# 1 3 4 5 6 7 8 9 10 -2
# 10 1 3 4 5 6 7 8 9 -3
# 9 10 1 3 4 5 6 7 8 -4
# 10 1 3 4 5 6 7 8
#-... + 4


# 해당 원소의 값의 인덱스를 해당 큐에서 확인하고
# 거기로 가는 방법이 첫번째와 마지막 인덱스까지 가는 방법 중에 

# 큐의 크기 N, 뽑아내려고 하는 수의 개수 M
N, M = map(int, (input().split()))
# 뽑아줄 인덱스 고르자
num_idx =list(map(int, (input().split())))

10-2 > 5

# 1
# 2 1 -1*(0-1)+10-2     2-1 1 
# 9 3 -1*(0-2)+10-9     9-2 7 
# 5 4 -1*(0-9)+10-5               5-9 => - 
# 걍 첫번째 인덱스에서 두번째 원소의 인덱스 까지 어떻게 갈지만 고민하면 되네
count = 0
idx = 1

for num in range(len(num_idx)):
    # idx가 7인데 num이 2야 그럼 2-7 5냐 10-2+2 5냐 
    # idx가 1인데 num이 2야 그럼 2-1 1냐 10-2+1

    if N-num == num-idx:
        





