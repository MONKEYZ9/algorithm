N = input()

max_N = 9*len(N)+1

ans = []
for i in range(1, max_N):
    temp = 0
    if int(N)-i > 0:
        if len(str(int(N)-i)) >= 2:
            for j in list(str(int(N)-i)):
                temp += int(j)
            if i == temp:
                ans.append(int(N)-i)
        else:
            if ((int(N)-i)*2) == int(N):
                ans.append(int(N)-i)
if len(ans) == 0:
    print(0)
else:
    print(min(ans))
