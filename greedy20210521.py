n, m = map(int, input().split())

# # 순서대로 북 동 남 서
# # position  = [0, 1, 2, 3]
# # 이걸 위치로 표현하면


# # 바라보는 방향에 따라 왼쪽이 달라진다
# # 북쪽을 바라볼때 왼쪽은 당연히 서쪽
# # 남쪽을 바라볼때 왼쪽은 당연히 동쪽
# # 서쪽을 바라볼때 왼쪽은 당연히 남쪽
# # 동쪽을 바라볼때 왼쪽은 당연히 북쪽

# # 거기가 가본 땅이면 왼쪽으로 돌고 1칸 전진
# # 아니라면 
# # 왼쪽으로만 방향을 돌리기
# # 만약 다 돌았는데 모두 가본칸이거나 바다로 되어있다면 바라보는 방향을 유지한채로 1단계 뒤로 가는데
# # 뒤쪽 방향이 바다면 움직임 홀드

# # direction 은 턴이 될 수록 1을 더하는데 그 값은 0~3을 반복해야함 3이 되면 0으로 바꿔줘야  함
# # 북쪽을 바라볼때 왼쪽은 당연히 서쪽
# # 0 일때 서쪽으로 한칸 가는 것은 dx를 -1하는거 dy는 0
# # 남쪽을 바라볼때 왼쪽은 당연히 동쪽
# # 1 일때 동쪽으로 한칸 가는 것은 dx를 +1하는거 dy는 0
# # 서쪽을 바라볼때 왼쪽은 당연히 남쪽
# # 2 일때 남쪽으로 한칸 가는 것은 dy를 +1하는거 dx는 0
# # 동쪽을 바라볼때 왼쪽은 당연히 북쪽
# # 3 일때 북쪽으로 한칸 가는 것은 dy를 -1하는거 dx는 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# for _ in range(n) 라고 하면 변수와는 상관없이 n번 반복하는거
# d = [[0] * 4] 하면 [[0, 0, 0, 0]]
# [1, 2, 3] * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
d = [[0] * m for _ in range(n)]
# print(d) 이렇게 함으로 지도에 가본적이 없는 곳으로 만들고

# 현재 캐릭터의 위치와 방향을 받아야해
x, y, direction = map(int, input().split())
d[x][y] = 1

game_map = []
for i in range(n):
       game_map.append(list(map(int, input().split())))

# class를 이용해서 했어야 해
# 왼쪽으로 돌기
def turn_left():
      #  전역변수 global로 direction 을 여기서도 이용해서 다시 지정한다는거야
   global direction
   direction -= 1
   if direction == -1:
      direction = 3
# 0 -> 1로 바꾼 횟수
# c처음 간 곳은 0->1로 바꿨으니 카운트 해줘야지
zeroToOne_count = 1
turn_time = 0

while True:
   # 왼쪽으로 회전하자
   turn_left()
   # 방향에 따른 걸 이렇게 하네 
   nx = x + dx[direction]
   ny = y + dy[direction]
   # 회전하고 나서 정면에 가보지 않은 칸이 있다면 이동하자
   if d[nx][ny] == 0 and game_map[nx][ny] == 0:
      d[nx][ny] = 1
      x = nx
      y = ny
      zeroToOne_count += 1
      # 회전하는 횟수가 4가되면 갈 곳이 없다는 것을 확인하는거지
      turn_time = 0
      continue
   # 회전하고 정면에 가본 칸이거나 바다인경우
   else:
      turn_time += 1
   if turn_time == 4:
      # 다시 돌아가자 원래 위치ㄱ로
      nx = x - dx[direction]
      ny = y - dy[direction] 

      # 뒤로 갈 수 있다면 이동하자
      if game_map[nx][ny] == 0:
         x = nx
         y = ny
      # 뒤가 바다인경우
      else:
         break
      # 다시 턴 타임을 0으로 바꿔주기
      turn_time = 0
print(zeroToOne_count)