N = int(input())


move = list(input().split())

# R R R U D D
print(move)

# 현재 있는 위치 표시하자
position  = [1, 1]
# LRUD가 뭔지 표시하자
L = [0,-1]
R = [0, 1]
U = [-1, 0]
D= [1, 0]

# print(position[0] + L[0])
# print(position[1])
for i in range(len(move)):
    if move[i] == 'L':
        position[1] += L[1]
        if position[1] == 0 or position[1] == N:
            position[1] -= L[1] 
    elif move[i] == 'R':
        position[1] += R[1]
        if position[1] == 0 or position[1] == N:
            position[1] -= R[1] 
    elif move[i] == 'U':
        position[0] += U[0]
        if position[0] == 0 or position[0] == N:
            position[0] -= U[0] 
    else:
        position[0] += D[0]
        if position[0] == 0 or position[0] == N:
            position[0] -= D[0] 
print(position[0], position[1])
