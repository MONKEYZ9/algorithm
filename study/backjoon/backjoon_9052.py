p = [False,False] + [True]*10001
for i in range(2, 10001):
    if p[i]:
        for j in range(2*i, 10001, i):
            p[j] = False


T = int(input())
for _ in range(T):
    n = int(input())
    n_list = []
    for i in range(n+1):
        if p[i]:
            n_list.append(i)
    n_dict = {}
    for i in range(len(n_list)):
        # 벨류 값이 가장 작은 키를 뽑아내자
        if (n-n_list[i]) in  n_list:
            if n_list[i] - (n-n_list[i]) >= 0:
                n_dict [n_list[i] - (n-n_list[i])] = (n-n_list[i], n_list[i])

    min_key = min(n_dict.keys())
    print(n_dict[min_key][0],n_dict[min_key][1])
        