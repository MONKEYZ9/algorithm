# A, B = map(int, (input().split()))
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# elif A == B:
#     print('==')

# score = int(input())
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score <= 89:
#     print('B')
# elif 70 <= score <= 79:
#     print('C')
# elif 60 <= score <= 69:
#     print('D')
# else:
#     print('F')

# year = int(input())
# if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
#     print(1)
# else:
#     print(0)

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y < 0:
#     print(3)
# elif x < 0 and y > 0:
#     print(2)

H, M = map(int, input().split())

if M - 45 < 0:
    M = 60 - 45 + M
    H -= 1
    if H < 0:
        H = 23
else:
    M = M - 45
print(H, M)