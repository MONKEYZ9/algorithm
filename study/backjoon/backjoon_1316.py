#문자를 받는데
# 해당 문자가 1개만 있어도 연속문자
# 다만 그게 앞에서 연속되었는데 다른 곳에 또 있으면 연속 문자가 아님


# 일단 문자가 몇개인지 확인
# 그리고 인덱스를 뽑아보자


# N = int(input())

# word = list(input())

# while True:
#     for i in range(len(word)):
#         char_cnt = word.count(i)
#         if char_cnt > 1:
#             f_w_idx = word.index(word[i])
#             print(word[i])
#             print(f_w_idx)
#             for i in range(char_cnt-1):
                
# 딕셔너리로 하자
# w_dict = {}
# for key, w_char in enumerate(word):
#     w_dict [key] = w_char
# print(w_dict)

# for key, value in w_dict.items():
#     f_w_idx = word[key]
#     for i in range(key+1, len(word)):
#         if value == word[i]:
#             print(key, value)
#             print(i, word[i]
#             print('i - key : ', i - key)
#             print('=---------------------------=')
#     print('========================')

n = int(input())
for _ in range(n):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            n -= 1
            break
print(n)