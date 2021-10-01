# 일단, 번호에 해당하는 알파벳을 뽑아주고
# 할당시키되, 중간중간, 다른거 보고
# 그리고 해당 알파벳을 찾을때 숫자를 꺼내 쓰자

import string

# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
upper = string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits# 숫자 0123456789
upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
a = list(input().upper())
n = 0
abc= {}
for i in range(3, 11):
    if n == 15:
        abc [i] = upper[n:n+4]
        n += 4
    elif n == 22:
        abc [i] = upper[n:]
    else:
        abc [i] = upper[n:n+3]
        n+=3
count = 0
for spell in a:
    for key, value in abc.items():
        if spell in list(value):
            count += key
print(count)