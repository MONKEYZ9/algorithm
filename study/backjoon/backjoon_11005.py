
# def recur(N, B):
#     N = N // B
#     if N%B < 10:
#         print('다르게 해야함')
#         answer = str(N%B)
#         print(answer)
#         return answer+recur(N, B)
#     else:
#         answer = chr(N%B+55)
#         if N%B > N // B:
#             return answer + chr(N%B+55)
#         return answer + recur(N, B) 

# # 2191931 36
# # 3359231 36


def recur(N, B):
    if B > 10:
        if N%B >= 10:
            answer = chr(N%B+55)
        else:
            answer = str(N%B)
        N = N//B
        if N ==0:
            return answer
        return recur(N,B) + str(answer)
    else:
        answer = str(N%B)
        N = N//B
        if N == 0:
            return answer
        return recur(N,B) + str(answer)


N, B = map(int, input().split())
a = recur(N, B)
print(a)
