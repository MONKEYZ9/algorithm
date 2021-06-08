n = int(input())
li = []
for i in range(n):
    li.append(input())
li2 = list(set(li))
li2.sort()
li2.sort(key=len)

for i in range(len(li2)):
    print(li2[i])