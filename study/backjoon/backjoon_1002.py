import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 중심간 거리
    d = math.sqrt(((y2-y1)**2)+((x2-x1)**2))
    # 중심이 같을때
    if d == 0 and r1-r2 == 0:
        print(-1)

    #  두점에서 만날때
    if d != 0 and r1 - r2 < d < r1 + r2:
        print(2)
    
    # 한점에서 만날때
    elif d != 0 and ( r1+r2 == d or r1-r2 == d):
        print(1)
    
    # 한점도 만나지 않을때
    elif (d == 0 and r1 - r2 != 0) or (d != 0 and (r1 + r2) < d)or (d != 0 and (r1 - r2) > d):
        print(0)

#     조금 조건문을 과하게 생각하신 것 같습니다.

# 계산한 거리는 반지름으로 r1, r2(r1 > r2)

# 두 중심간의 거리를 d라고 가정할 때

# 두 점에서 만나는 경우

# d != 0 and r1 - r2 < d < r1 + r2

# 한 점에서 만나는 경우

# d != 0 and { r1+r2 = d (외접) r1-r2 = d(내접)}

# 한 점에서도 만나지 않을 경우

# d = 0 and r1 - r2 != 0

# d != 0 and r1 + r2 > d

# 무수히 많은 점에서 만날 경우

# d = 0 and r1 - r2 = 0




    # 중심은 같은경우
    # if x1 == x2 and y1 == y2:
    #     # 중심은 같으나, 반지름이 다른 경우
    #     if r1 != r2:
    #         print(0)
    #     # 중심도 같고 반지름도 같은 경우
    #     else:
    #         print(-1)

    # # 중심이 다른 경우
    # else:
    #     if x1 == x2 and y1 != y2:
    #         print('y만 다른경우')
    #         if abs(y2-y1) == r2+r1:
    #             print(1)
    #         else:
    #             if abs(y2-y1) > r2+r1:
    #                 print(0)
    #             elif abs(y2-y1) == r2+r1:
    #                 print(1)
    #             elif abs(y2-y1) < r2+r1:
    #                 if r1 > r2:
    #                     if r1 > abs(y2-y1)+r2:
    #                         print(0)
    #                     elif r1 == abs(y2-y1)+r2:
    #                         print(1)
    #                     elif r1 < abs(y2-y1)+r2:
    #                         print(2)
    #                 elif r2 > r1:
    #                     if r2 > abs(y2-y1)+r1:
    #                         print(0)
    #                     elif r2 == abs(y2-y1)+r1:
    #                         print(1)
    #                     elif r2 < abs(y2-y1)+r1:
    #                         print(2)
    #                 else:
    #                     print(2)
    #                 if r1 > r1:
    #                     if r1 > abs(y2-y1)+r1:
    #                         print(0)
    #                     elif r1 == abs(y2-y1)+r1:
    #                         print(1)
    #                     elif r1 < abs(y2-y1)+r1:
    #                         print(2)
    #                 elif r1 > r1:
    #                     if r1 > abs(y2-y1)+r1:
    #                         print(0)
    #                     elif r1 == abs(y2-y1)+r1:
    #                         print(1)
    #                     elif r1 < abs(y2-y1)+r1:
    #                         print(2)
    #                 else:
    #                     print(2)
    #     elif y1 == y2  and x1 != x2:
    #         print('x만 다른경우')
    #         if abs(x2-x1) == r2+r1:
    #             print(1)
    #         elif abs(x2-x1) > r2+r1:
    #             print(0)
    #         elif abs(x2-x1) < r2+r1:
    #             if r1 > r2:
    #                 if r1 > abs(x2-x1)+r2:
    #                     print(0)
    #                 elif r1 == abs(x2-x1)+r2:
    #                     print(1)
    #                 elif r1 < abs(x2-x1)+r2:
    #                     print(2)
    #             elif r2 > r1:
    #                 if r2 > abs(x2-x1)+r1:
    #                     print(0)
    #                 elif r2 == abs(x2-x1)+r1:
    #                     print(1)
    #                 elif r2 < abs(x2-x1)+r1:
    #                     print(2)
    #             else:
    #                 print(2)
    #             if r1 > r1:
    #                 if r1 > abs(x2-x1)+r1:
    #                     print(0)
    #                 elif r1 == abs(x2-x1)+r1:
    #                     print(1)
    #                 elif r1 < abs(x2-x1)+r1:
    #                     print(2)
    #             elif r1 > r1:
    #                 if r1 > abs(x2-x1)+r1:
    #                     print(0)
    #                 elif r1 == abs(x2-x1)+r1:
    #                     print(1)
    #                 elif r1 < abs(x2-x1)+r1:
    #                     print(2)
    #             else:
    #                 print(2)
    #     else:
    #         print('중심이 아예다름')
    #         # 중심이 아예 다름
    #         # ((y2-y1)**2)+((x2-x1)**2) == r1+r2
    #         if ((y2-y1)**2)+((x2-x1)**2) == r1+r2:
    #             print(1)
    #         elif ((y2-y1)**2)+((x2-x1)**2) > r1+r2:
    #             print(2)
            
    #         # 원이 다른 원을 피해가거나 더 크게 돌아서 한번 만날때 구분
    #         elif ((y2-y1)**2)+((x2-x1)**2) < r1+r2:
    #             if r1 < r2:
    #                 if r1+((y2-y1)**2)+((x2-x1)**2) == r2*2:
    #                     print(1)
    #                 else:
    #                     print(0)
    #             elif r1 > r2:
    #                 if r2+((y2-y1)**2)+((x2-x1)**2) == r1*2:
    #                     print(1)
    #                 else:
    #                     print(0)
           