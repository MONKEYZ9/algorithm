#분할정복 알고리즘

N = int(input())
# N이 3보다 클 경우, 
# 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을
#  크기 N/3의 패턴으로 둘러싼 형태이다. 
# 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.


print('***\n* *\n***'*3)

# sttt = '***\n* *\n***'
# def recur(N, sttt):
#     if N == 3:
#         return sttt
#     else:
#         N = N // 3
#         sttt = sttt*3+'\n'+sttt+"   \n  \n   \n"+sttt+'\n'+sttt*3+'\n'+sttt
#         return recur(N, sttt)
# print(recur(N, sttt))






#         return recur(N)

# recur(N)
# # def recur2(N):
# #     if N == 3:



# 어차피 
# 그럼 행렬로 생각을 해보자
# (0,0) (1,0) (2,0) => *
# (0,1) (2,1) => *
# (1,1) => 공백
# (0,2) (1,2) (2,2) => *







# * * *
# *   *
# * * *

# * * * * * * * * *
# *   * *   * *   *
# * * * * * * * * *
# * * *       * * *
# *   *       *   *
# * * *       * * *
# * * * * * * * * *
# *   * *   * *   *
# * * * * * * * * *

# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *   * *   * *   * *   * *   * *   * *   * *   * *   *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * *       * * * * * *       * * * * * *       * * *
# *   *       *   * *   *       *   * *   *       *   *
# * * *       * * * * * *       * * * * * *       * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *   * *   * *   * *   * *   * *   * *   * *   * *   *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * *                   * * * * * * * * *
# *   * *   * *   *                   *   * *   * *   *
# * * * * * * * * *                   * * * * * * * * *
# * * *       * * *                   * * *       * * *
# *   *       *   *                   *   *       *   *
# * * *       * * *                   * * *       * * *
# * * * * * * * * *                   * * * * * * * * *
# *   * *   * *   *                   *   * *   * *   *
# * * * * * * * * *                   * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *   * *   * *   * *   * *   * *   * *   * *   * *   *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * *       * * * * * *       * * * * * *       * * *
# *   *       *   * *   *       *   * *   *       *   *
# * * *       * * * * * *       * * * * * *       * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *   * *   * *   * *   * *   * *   * *   * *   * *   *
# * * * * * * * * * * * * * * * * * * * * * * * * * * *