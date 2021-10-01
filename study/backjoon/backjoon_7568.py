N = int(input())
N_list = []
for i in range(N):
    N_list.append(tuple(map(int,(input().split()))))

for i in N_list:
    rank = 1
    for j in N_list:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]:
                rank +=1
    print(rank, end=' ')