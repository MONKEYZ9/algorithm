
# for abc in abc_list:
#     print(abc)
#     if s in abc:
#         print(abc_list.index(s), end=' ')
#     else:
#         print(-1, end=' ')

# bin_list = []
# for s in S_list:
#     for abc in abc_list:
#         if abc == s:
#             bin_list.append(s.index(abc))
#             break

# print(bin_list)

# 있는지 없는지 확인해주자
def main_abc(s_list, abc_list):
    bin_list = []
    for abc in abc_list:
        if abc in s_list:
            bin_list.append(s_list.index(abc))
        else:
            bin_list.append(-1)
    print(*bin_list)


s_list = list(map(str, input()))
abc_list = [chr(i) for i in range(97, 123)]

main_abc(s_list, abc_list)