X = int(input())
count = 0
# 한자리일때
if X < 10:
    count += X
# 두자리일때
elif X < 100:
    dujari_hab = [
        i 
        for i in range(10,X+1)
        if str(i)[0] <= str(i)[1]
    ]
    dujari_cha = [
        i 
        for i in range(10,X+1)
        if str(i)[0] > str(i)[1]
    ]
    count+=9
    count += len(dujari_hab) + len(dujari_cha)
elif X <= 1000:
    dujari_hab = [
        i 
        for i in range(10,100)
        if str(i)[0] <= str(i)[1]
    ]
    dujari_cha = [
        i 
        for i in range(10,100)
        if str(i)[0] > str(i)[1]
    ]
    count += 9
    count += len(dujari_hab) + len(dujari_cha)

    sajari_hab = [
        i
        for i in range(100,X+1)
        if str(i)[0] <= str(i)[1] <= str(i)[2]
        if int(str(i)[1])-int(str(i)[0]) == int(str(i)[2])-int(str(i)[1])
    ]
    sajari_cha = [
        i 
        for i in range(100,X+1)
        if str(i)[0] > str(i)[1] > str(i)[2]
        if int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0])
    ]

    count += len(sajari_hab) + len(sajari_cha)
print(count)

# 세자리일때
# elif len(X) < 4:
#     count += 99
    # 양의 등차수열일때

    # 음의 등차수열일때


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 9

# 12 13 14 15 16 17 18 19 - 9
# 23 24 25 26 27 28 29 - 7
# 34 - 6
# 45 - 5
# 56 - 4
# 67 - 3
# 78 79 - 2
# 88 89  - 2
# 99 - 1
# 45

# 99 98 97 96 95 94 93 92 91 90

# 22 21
# 11
# 45

# 11 12 13 14

