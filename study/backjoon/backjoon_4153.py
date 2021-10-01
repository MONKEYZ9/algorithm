while True:
    a,b,c = map(int, input().split())
    abc_list = [a,b,c]
    abc_list.sort()
    if a == b == c == 0:
        break
    if (abc_list[2]**2) == ((abc_list[0]**2)+(abc_list[1]**2)):
        print('right')
    else:
        print('wrong')
