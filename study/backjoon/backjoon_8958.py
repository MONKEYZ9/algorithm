N = int(input())
N_list = [input() for _ in range(N)]


# for n in N_list:
#     for i in range(len(n)):
#         count = 0
#         if n[i] == 'O':
#             count += 1
#             count_list.append(count)
#             print(count_list)
#         else:
#             count = 0
#             count_list.append(count)
#             print(count_list)
# print(count_list)
        
# strr= 'OOXXOXXOOO'
# print(strr[4])


for n in N_list:
    count = 0
    for i in n.split('X'):
        if i.count('O') > 1:
            for j in range(1, i.count('O')+1):
                count += j
        else:
            count += ( i.count('O') ) 
    print(count)