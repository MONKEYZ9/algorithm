T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 중심은 같은경우
    if x1 == x2 and y1 == y2:
        # 중심은 같으나, 반지름이 다른 경우
        if r1 != r2:
            print(0)
        # 중심도 같고 반지름도 같은 경우
        else:
            print(-1)

    # 중심이 어느 하나가 같은 경우
    elif x1 == x2 or y1 == y2:
        if x1 == x2 and y1 != y2:
            if abs(y2-y1) == r2+r1:
                print(1)
            elif abs(y2-y1) > r2+r1:
                print(0)
            elif abs(y2-y1) < r2+r1:
                print(2)
        elif y1 == y2  and x1 != x2:
            if abs(x2-x1) == r2+r1:
                print(1)
            elif abs(x2-x1) > r2+r1:
                print(0)
            elif abs(x2-x1) < r2+r1:
                print(2)
    else:
        # 중심이 아예 다름
        # ((y2-y1)**2)+((x2-x1)**2) == r1+r2
        if ((y2-y1)**2)+((x2-x1)**2) == r1+r2:
            print(1)
        elif ((y2-y1)**2)+((x2-x1)**2) > r1+r2:
            print(2)
        elif ((y2-y1)**2)+((x2-x1)**2) < r1+r2:
            print(0)

           