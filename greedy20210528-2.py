# 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 
# 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 
# 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.

# 그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 


# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

# 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 
# 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

# import sys
# T = int(sys.stdin.readline())

# first_test_scores = []
# second_test_scores = []

# for i in range(T):
#   N = int(sys.stdin.readline())
#   for _ in range(N):
#     if i == 0:
#       first_test_scores.append(list(map(int, sys.stdin.readline().split())))      
    # else:
    #   second_test_scores.append(list(map(int, sys.stdin.readline().split())))
  # if i == 0:
  #   first_test_scores.sort()
  #   gijun1 = first_test_scores[0][1]
  #   firstTestCount = 1
  #   for i2 in range(1, N):
  #     if gijun1 > first_test_scores[i2][1]:
  #       gijun1 =  first_test_scores[i2][1]
  #       firstTestCount += 1
  # else:
  #   second_test_scores.sort()
  #   gijun2 = second_test_scores[0][1]
  #   secondTestCount = 1
  #   for i2 in range(1, N):
  #     if gijun2 > second_test_scores[i2][1]:
  #       gijun2 =  second_test_scores[i2][1]
  #       secondTestCount += 1

# print(firstTestCount)
# print(secondTestCount)


import sys
T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  test_scores = []
  testCount = 1
  for i in range(N):
    test_scores.append(list(map(int, sys.stdin.readline().split())))
  test_scores.sort()
  gijun = test_scores[0][1]
  for i2 in range(1, N):
    if gijun > test_scores[i2][1]:
      gijun =  test_scores[i2][1]
      testCount += 1
  print(testCount)