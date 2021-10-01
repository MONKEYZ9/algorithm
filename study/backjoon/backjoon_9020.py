p = [False,False] + [True]*10001
for i in range(2, 10001):
    if p[i]:
        for j in range(2*i, 10001, i):
            p[j] = False

# 1948ms까지 줄임
T = int(input())
for _ in range(T):
    n = int(input())
    i_list =[]
    for i in range((n+1)//2+1):
        # 먼저 소수인지 확인하고
        if p[i] and p[n-i] and i <= n-i:
            print(i)
            i_list.append(i)
    print(i_list[-1], n-i_list[-1])


# 3128ms에서 
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     i_list =[]
#     for i in range(n+1):
#         # 먼저 소수인지 확인하고
#         if p[i]:
#             # n에서 뺀거도 소수인지 확인하고
#             if p[n-i]:
#                 # 
#                 if i <= n-i:
#                     i_list.append(i)
#     print(i_list[-1], n-i_list[-1])
    
# 시간초과
    # n_dict = {}
    # for i in range(int(len(n_list)**0.5)+1):
    #     print(i)
        # 벨류 값이 가장 작은 키를 뽑아내자
    #     if (n-n_list[i]) in  n_list:
    #         if n_list[i] - (n-n_list[i]) >= 0:
    #             n_dict [n_list[i] - (n-n_list[i])] = (n-n_list[i], n_list[i])

    # min_key = min(n_dict.keys())
    # print(n_dict[min_key][0],n_dict[min_key][1])
        