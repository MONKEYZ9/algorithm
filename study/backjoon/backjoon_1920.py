N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

# M 리스트의 숫자들이 있는지 확인하면 돼
# 재귀로 확인해주자는 거네
# 있으면 1 없으면 0을 내 뱉는


def check_num(N, N_list):
  mid_num = N_list[len(N_list)//2]
  last_num = N_list[-1]
  fisrt_num = N_list[0]
  if N == mid_num:
    return 1
  elif N > mid_num:
    if N > last_num:
      return 0
    N_list = 
    return check_num(N, N_list[(len(N_list)//2)+1:])
  elif N < mid_num:
    if N < fisrt_num:
      return 0
    return check_num(N, N_list[:(len(N_list)//2)])

for i in M_list:
  ans = check_num(i, N_list)
  print(ans)


