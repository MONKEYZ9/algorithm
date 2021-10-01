N, M = map(int, (input().split()))
N_list = list(map(int, (input().split())))

print(N_list)

len_list = len(N_list)

new_list = []



for i in range(len_list):
    # print('i : ', i)
    for j in range(i+1, len_list):
        # print('j : ', j)

        for k in range(j+1, len_list):
            # print('k : ', k)
            ans = N_list[i]+N_list[j]+N_list[k]
            if ans <= M:
                new_list.append(ans)
print(max(new_list))






