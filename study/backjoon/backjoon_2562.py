# N_list  = []
# for i in range(9):
#     N_list.append(int(input()))

# print(max(N_list))
# N_list.remove(max(N_list))
# print(max(N_list))
N_list2 = [
    int(input())
    for _ in range(9)
]
max_n = max(N_list2)
max_n_idx = N_list2.index(max(N_list2))
print(max_n)
print(max_n_idx+1)
