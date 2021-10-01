# import numpy as np
N, M = map(int, input().split())

# N_list = [list(input()) for _ in range(N)]

N_list = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B']]
cnt_list = []
for n in range(N-7):
    New_n_list = N_list[n:n+8]
    # 새로운 8개 행으로 된 리스트 완성 그러나 열은 M개임
    for m in range(M-7):
        new_N_list = []

        for n_list in New_n_list:
            new_N_list.append(n_list[m:m+8])
        cnt = 0
        for j in range(len(new_N_list)):
            new_n_list = new_N_list[j]

            for i in range(1, len(new_n_list)):
                if j-1 > 0:
                    if new_N_list[j-1][0] == new_N_list[j][0]:
                        cnt += 1
                        if new_N_list[j][0] == 'B':
                            new_N_list[j][0] = 'W'
                        else:
                            new_N_list[j][0] = 'B'
                
                    if new_n_list[i-1] == new_n_list[i]:
                        cnt += 1
                        if new_n_list[i] == 'B':
                            new_n_list[i] = 'W'
                        else:
                            new_n_list[i] = 'B'
        cnt_list.append(cnt)
print(min(cnt_list))
    

        




























# N_list = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B']]
# N_list_np = np.array(N_list)
# print(N_list_np[0:3, 0:8])

























# print(N_list[3][3])
# N_list_str = " ".join(N_list)
# print(N_list_str)
# print(len(N_list_str))

# cnt=0
# for i in range(1, len(N_list_str)):
#     if N_list_str[i-1] == N_list_str[i]:
#         print(N_list_str[i])
#         print(N_list_str[i-1])
#         cnt += 1
#         if N_list_str[i] == 'B':
#             N_list_str = N_list_str.replace()
#         else:
#             N_list_str[i] = 'B'
#         print(cnt)
#         print(i)



# cnt = 0
# for i in N_list:
#     i_list = list(i)
#     for j in range(1,len(i_list)):

# for i in range(N):
#     print(N_list[i])

# cnt_li = []
# for i in range(N-8):
#     nw_N_li = N_list_np[i:i+8]
    # cnt = 0
    # for j in range(M-8):
    #     for nw in nw_N_li:
    #         for n in nw[j:j+8]:
    #             print(n, end=' ')
    #         print()
    #     print('========================')
    # print('-----------------------')
                

            


#                 for n in range(1, len(n_li)):
#                     if n_li[n-1] == n_li[n]:
#                         if n != len(n_li):
#                             if n_li[n+1] == n_li[n]:
#                                 cnt += 1
#                         # if n_li[n] == 'B':
#                         #     n_li[n] = 'W'
#                         # else:
#                         #     n_li[n] = 'W'
#         cnt_li.append(cnt)
# print(cnt_li)


