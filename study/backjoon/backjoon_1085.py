x, y, w, h = map(int, input().split())
cha_list=[]
cha_list.append(h-y)
cha_list.append(y)
cha_list.append(x)
cha_list.append(w-x)

print(min(cha_list))