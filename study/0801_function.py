n_list = [ x for x in range(1, 100)]

for a in range(1, 100):
    k = a
    for i in range(len(str(a))):
        k += a//10**i %10
    # if k in n_list:
    n_list.remove(k)

for j in n_list:
    print(j)

# # def get_hab(a):
# #     return sum(a)
# # 생성자를 가지고 있는 친구들을 쫙 뽑아볼 수 있어
# # def get_notd(n):
# #     new_list = []
# #     for i in range(n):
# #         string_n = str(i)
# #         if len(string_n) < 2:
# #             string_n = '0' + string_n
# #             new_n = i + int(string_n[0]) + int(string_n[1])
# #             new_list.append(new_n)

# #         else:
# #             new_n = i + int(string_n[0]) + int(string_n[1])
# #             new_list.append(new_n)

# #     return new_list
# # ==> 2자리만 생각함

# # 해당 파일을 동적계획법으로 해야 할 것 같은데
# # 있는지 없는지 확인하고
# # 그걸 다시 확인안하게끔 해야지 있다면 안하게 해야할거같은데
# # def get_notd(n):
# sangsungja = 0
# nanugi = 10
# # for i in range(10000+1):
# i = 112
#     # while True:
# sangsungja += i // nanugi * len(str(i))
# namugi = i % 10
# print(sangsungja)
            
# # 112 % 10 2
# # 112 // 100 1





# # # 확인하는 함수
# # def check_d(n):
# #     new_list = get_notd(n)
# #     if n not in new_list:
# #         return n

# # def d(n):
# #     n_list = [i for i in range(10001)]
# #     selfNum = check_d(n)
# #     n_list
# #     print(answer)
# # n = int(input())



# # 1 1+1 2
# # 2 2+2 4
# # 3 3+3 6
# # 4 4+4 8
# # 5 5+5 10
# # 6 6+6 12
# # 7 7+7 14
# # 8 8+8 16
# # 9 9+9 18
# # 10 10 + 1 + 0 = 11
# # 11 11+1+1 13
# # 12 12+1+2 15
# # 13 13+1+3 17
# # 14 14+1+4 19
# # 15 15+1+5 21
# # 16 16+1+6 23
# # 17 17+1+7 25
# # 18 18+1+8 27
# # 19 19+1+9 29
# # 20 20+2+0 22
# # 21 21+2+1 23
# # 23 23+2+3 28

# # 31 31+3+1 35
# # 100 100+0+0+1 101
# # 113 113+1+1+3 118