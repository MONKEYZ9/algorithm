# 간단한 문제
# N으로 나누었을때, 나머지와 몫이 같은 것을 구해라
# 그니까 2로 나눴을때, 몫이랑 나머지가 같아야 하는건데
# 그럼 나머지는 2보다 작아야 나머지니까 1이겠고 몫은 1이겠지
#
# 그럼 3이면 나머지가 2 몫도 2 => 8
# 또는 나머지가 1 몫도 1 => 4
#
4이면
나머지, 몫이 3 => 4 * 3 + 3 = 15
나머지, 몫이 2 => 4 * 2 + 2 = 10
나머지, 몫이 1 => 4 * 1+ 1 = 5
#
# 5이면
# 나머지, 몫이 4 => 5 * 4 + 4 = 24
# 나머지, 몫이 3 => 5 * 3 + 3 = 18
# 나머지, 몫이 2 => 5 * 2 + 2 = 12
# 나머지, 몫이 1 => 5 * 1 + 1 = 6
#
#
# 6이면
# 나머지, 몫이 5 => 6 * 5 + 5 = 35
# 나머지, 몫이 4 => 6 * 4 + 4 = 28
#
#
# N이라면 (N+1) * (N-1)
# def test2(N):
#     # 몫과 나머지가 같아야해
#     hab = []
#     for i in range(N):
#         hab.append((N * i) + i)
#     return sum(hab)
# 범위가 언급되어있다면 범위를 정해주면 되고
# 범위가 언급되어있지 않다?
# 범위가 이미 정해져있을 것이다.
# 수기로 함 풀어보라는 거야

# 가우스 합
# 1부터 50까지의 합
# 이런걸 바로 아느냐
# n(n+1) / 2 가 1부터 n까지의 합



# 이건 안된다.
# N = int(input())
# hab = 0
# for i in range(1, N):
#     hab += (N+i) * (N-i)
#     print(hab)
# print(hab)