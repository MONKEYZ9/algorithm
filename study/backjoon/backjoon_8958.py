N = int(input())
N_list = [input() for _ in range(N)]

for i in N_list:
    # 그냥 O이면 읽고 카운트해주는거로 가자
    # X가 나오면 count 0으로 바꾸고
    print(len(N_list[i]))
    # for j in range(len(N_list[i])):




    # count = 0
    # 문자를 X기준으로 자르자
    # n_list = i.split('X')
    # print(n_list)
    # for j in n_list:
    #     print(j)
    #     count +=  j.count('O')
    #     print()
    #     # print(count)
    #     # print('=========================')