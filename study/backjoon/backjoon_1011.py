T = int(input())
# 1=> 1
# 2=> 11
# 3=> 111
# 4=> 121 2^2 2*2-1 = 4 2

# 5=> 1211
# 6=> 1221
# 7=> 1211
# 8=> 12311
# 9=> 12321 3^2 3*2-1 = 5 3

# 10=>123211
# 11=>123221
# 12=>123321
# 13=>1233221
# 14=>1233221
# 15=>1233321
# 16=>1234321 4^2 4*2-1 = 7 4


for i in range(T):
    x, y = map(int, input().split())
    cha = y-x
    n = 1
    while True:
        if n**2 <= cha < (n+1)**2:
            speed = n
            cnt = 2*n -1
            if (cha-(n**2))%speed > 0:
                cnt += (cha-(n**2))//speed+1
                break
            else:
                cnt += (cha-(n**2))//speed
                break
        else:
            n += 1
    print(cnt)



# 최소한의 warp로 최대로 갈 수 있는 법은

# 차수	설명	최대거리	이 때 워프한 회수	최고속도
# 1	1	1	1	1
# 2	121	4	3	2
# 3	12321	9	5	3
# 4	1234321	16	7	4
# 5	123454321	25	9	5
# ...				
# i	1..i..1	i^2	2i-1	i
# 입니다.

# 남은 거리는 최고속도보다 빠르게 갈 수 없습니다.

# (거리의 나머지를 최고속도로 나눠서 올림하시면 
# 추가로 가야 하는 회수가 나옵니다.)

# 예) 23
# 16보다 크지만, 25보다 작음 
# - 최대워프거리 16, 워프회수 7,  최고속도 4
# - 나머지 거리7 (23-16)
# - 7은 최고속도 4로 1.75회 → 2회 더 가야함







# for i in range(T):
#     x, y = map(int, input().split())
#     # 무조건 마지막은 1광년 날아야 하니까 카운트 한번하고
#     cha = y-x
#     # 3과 4의 차이부터
#     f = 7
#     b = 10
#     # 방법수
#     cnt = 3
#     if cha == 1 or cha == 2:
#         print(cha)
#     elif 3<= cha <= 4:
#         print(cnt)
#     elif 5<= cha <= 6:
#         print(cnt+1)
#     else:
#         cnt = 4
#         while True:
#             if f <= cha <= b:
#                 break
#             else:
#                 f += cnt
#                 b += cnt+1
#                 cnt += 1
#         print(cnt+1)    



                


    # while True:
    #     if y-x == cnt:
    #         cnt += 1
    #         break
    #     else:

    #         cnt+=1
        

    
        


# 수기로 작성해보자

#  1 50
# 1 3 
# 2 3
    # while True:
    #     print('y : ',y)
    #     y = y-cnt
    #     print('y-cnt : ', y)
    #     print('cnt :', cnt)
    #     cnt +=1
    #     print('cnt + 1 :', cnt)
    #     if y-x-cnt < cnt+2:
    #         cnt +=1
    #         break