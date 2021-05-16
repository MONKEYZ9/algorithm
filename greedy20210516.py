n = int(input())
# print(N)
x, y = 1, 1
plans = input().split()
# print(plans)

move_types = ['L', 'R', 'U', 'D']

movetype_x = [0, 0, -1, 1]
movetype_y = [-1, 1, 0, 0]


# # 그럼 N의 숫자대로 움직여야 하는거니까
for i in range(0,n):

    # print(plans[i])
    if plans[i] == 'L':
        y -= 1
        x += 0
        if y == 0:
            y += 1
    elif plans[i] == 'R':
        y += 1
        x += 0
    elif plans[i] == 'U':
        y += 0
        x -= 1
        if x == 0:
            x += 1
    elif plans[i] == 'D':
        y += 0
        x += 1

print(x, y)




# for plan in plans:
#     # 이동후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + movetype_x[i]
#             ny = y + movetype_y[i]
#         #  공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n > n:
#         continue
#     x, y = nx, ny
# print(x, y)