
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
#  이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 36

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

# def recur(N, B):
#     try:
#         N_first = int(N[0])
#         answer = (N_first)*(B**(len(N)-1))
#         N.pop(0)
#         if len(N) == 0:
#             return answer
#         return answer + recur(N, B)

#     except ValueError:
#         n_len = len(N)
#         answer = (ord(N[0])-55)*(B**(n_len-1))
#         N.pop(0)
#         if len(N) == 0:
#             return answer
#         return answer + recur(N, B)


#     # 일단, 1ZZZZZ 와 같은걸 만났을때 
#     #1에 대해서 해결할 수 있어야 함
#     # 리스트의 인덱스로 통해서 꺼내와서 가져와서 하는게 나을거 같은데.

# N, B = input().split()
# # N = list(N)
# # B = int(B)
# # a = recur(N, B)
# # print(a)
# # print(1295//36)
# # # print(1295%36)

# # print(ord('Z'))
# # print(ord('A'))
# # # print(chr(36+54))
# # print(chr(90))

# # A : 10  65
# # Z : 35  90

# print(int(N, int(B)))



def recur(N, B, cnt):
    if N[-1].isnumeric():
        answer = int(N[-1])*(B**(cnt))
    else:
        answer = (ord(N[-1])-55)*(B**(cnt))
    N.pop()
    cnt += 1
    if len(N) == 0:
        return answer
    return answer + recur(N, B, cnt)

N, B = input().split()
N = list(N)
B = int(B)
cnt = 0
a = recur(N, B, cnt)
print(a)