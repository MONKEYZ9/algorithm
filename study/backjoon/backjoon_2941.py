#  위 문자들은 문자로만 읽는 거고 나머지는 다른 알파벳이랑 같다는거잖아

# str_n = input()
# croatia_str = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# abc = [chr(i) for i in range(97,123)]
# cnt = 0
# for c in croatia_str:
#     if c in str_n:
#         if str_n.count('c=') > 1:
#             cnt += str_n.count('c=')
#             str_n = str_n.replace(c,' ')
#         else:
#             str_n = str_n.replace(c,' ')
#             cnt += 1
# str_n = list(str_n)
# for str in str_n:
#     if str in abc:
#         cnt += 1

# print(cnt)
# # c=c= => 오류남 2로 뜸

# str_n = input()
# croatia_str = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for i in croatia_str:
#     str_n = str_n.replace(i,'!')

# print(len(str_n))

c = input().count
print(c('') - 1 - sum(map(c, ['-','=','nj','lj','dz='])))