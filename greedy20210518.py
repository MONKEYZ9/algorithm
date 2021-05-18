# 왕실 나이트 
# 나이트가 움직을 수 있는 방법 
# 수평으로 두칸 이동하고 수직으로 한칸 이동 
# 수직으로 두칸이동한 뒤에 수평으로 한칸 이동하기

# 나이트가 움직일 수 있는 방법 수를 보면
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 나이트가 있는 위치를 파악해야해
# a1이라고 하면 (1,1) 이라고 치환해야해

# 일단 입력을 받자
# knight_position = input()

# # 나이트 위치를 치환하자
# # 일단 하나씩 띄어보자
# # print(knight_position[0])
# # print(knight_position[1])

# knight_row = int(knight_position[1]) # int로 바꿔줬다.
# knight_colum = knight_position[0]
# # 이 방법으로는 8 * 8 은 할 수 있어도 다른 건 안된다는 사실을 깨달았다

# if knight_position[0] == 'a':
#     knight_colum = 1
# elif knight_position[0] == 'b':
#     knight_colum = 2
# elif knight_position[0] == 'c':
#     knight_colum = 3
# elif knight_position[0] == 'd':
#     knight_colum = 4
# elif knight_position[0] == 'e':
#     knight_colum = 5
# elif knight_position[0] == 'f':
#     knight_colum = 6
# elif knight_position[0] == 'g':
#     knight_colum = 7
# elif knight_position[0] == 'h':
#     knight_colum = 8

# print(knight_colum)
# print(knight_row)
# print('---------------------')
# result = 0
# for step in steps:
#     colum = knight_colum + step[0]
#     row = knight_row + step[1]
#     if colum >= 1 and colum <= 8 and row >= 1 and row <= 8:
#         result += 1

# print(result)

# print(type(ord('a')))
# print(chr(97))

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
knight_position = input()

row = ord(knight_position[0]) - ord('a') + 1
colum = int(knight_position[1])
print(colum)
print('----------------')

result = 0
for step in steps:
    next_colum = colum + step[0]
    next_row = row + step[1]
    if next_colum >= 1 and next_colum <= 8 and next_row >= 1 and next_row <= 8:
        result += 1

print(result)