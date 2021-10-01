# 4. 중심거리와 두 원의 위치 관계 <출처: 네이버 지식백과>

# 반지름의 길이가 r1인 원과 r2인 원의 중심거리를 d라고 할 때,  |r1 - r2| 또는 r1 + r2와의 크기를 비교하면, 두 원의 위치 관계를 알 수 있다.

# r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.

# r1 + r2 = d 이면 두 원은 외접한다.

# |r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.

# |r1 - r2| = d 이면 한 원이 다른 원에 내접한다.

# |r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.

# https://terms.naver.com/entry.naver?docId=3405330&cid=47324&categoryId=47324

import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 중심간 거리
    d = math.sqrt(((y2-y1)**2)+((x2-x1)**2))
    # 두원이 중심도 같고 반지름도 같은 경우
    if d == 0 and r2 == r1:
        print(-1)
    # |r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있는 경우
    elif abs(r1 - r2) > d and r1 != r2:
        print(0)
    # r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
    elif r1 + r2 < d:
        print(0)
    # r1 + r2 = d 이면 두 원은 외접한다.
    # |r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
    elif r1 + r2 == int(d) or abs(r1 - r2) == int(d):
        print(1)
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)