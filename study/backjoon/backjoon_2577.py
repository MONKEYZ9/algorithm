N_list = [int(input()) for _ in range(3)]
c = 1
for num in N_list:
    c *= num


# 갯수를 세자
for i in range(0,10):
    print(str(c).count(str(i)))