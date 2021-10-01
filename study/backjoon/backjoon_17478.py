# str_list = ['"재귀함수가 뭔가요?"', '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
# '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
# '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
# str = '라고 답변하였지.'


# def recursion2(cnt):
#     if cnt == 0:
#         print(str)
#     else:
#         print('____' * cnt +str)
#         recursion2(cnt-1)

# def recursion(cnt, n):
#     if n < 0:
#         print('____' * cnt + str_list[0])
#         print('____' * cnt + '"재귀함수는 자기 자신을 호출하는 함수라네"')
#         recursion2(cnt)


#     else:
#         print('____' * cnt + str_list[0] +'\n'+ '____' * cnt +str_list[1]+'\n'+ '____' * cnt +str_list[2]+'\n'+ '____' * cnt +str_list[3])
#         cnt += 1
#         recursion(cnt, n-1)



# n = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recursion(0, n)


def recursion(cnt, n):
    if n == 0:
        print('____' * cnt + '"재귀함수가 뭔가요?"')
        print('____' * cnt + '"재귀함수는 자기 자신을 호출하는 함수라네"')


    else:
        print('____' * cnt + '"재귀함수가 뭔가요?"')
        print('____' * cnt +'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * cnt +"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")      
        print('____' * cnt +'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recursion(cnt + 1, n-1)
    print('____' * cnt +'라고 답변하였지.')
        
n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursion(0, -1)



# def Recursion(N):
#     print('-'*4*(M-N) + '"재귀함수가 뭔가요?"')

#     if N==0 :
#         print('-'*4*(M-N) + '"재귀함수는 자기 자신을 호출하는 함수라네"')

#     else:
#         print('-'*4*(M-N) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print('-'*4*(M-N) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print('-'*4*(M-N) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         Recursion(N-1)
    
#     return print('-'*4*(M-N) + "라고 답변하였지.")
        
# N = int(input())
# M = N
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# Recursion(N)