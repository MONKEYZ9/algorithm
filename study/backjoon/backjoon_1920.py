N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

# M 리스트의 숫자들이 있는지 확인하면 돼
# 재귀로 확인해주자는 거네
# 있으면 1 없으면 0을 내 뱉는


# 1 2 3 4 5
# 1 3 5 7 9

def check_num(start_num, end_num, M, N_list):
  if start_num > end_num:
    return 0

  mid_num = (start_num+end_num)//2

  if M == N_list[mid_num]:
    return 1

  elif M < N_list[mid_num]:
    return check_num(start_num, mid_num-1, M, N_list)

  elif M > N_list[mid_num]:
    return check_num(mid_num+1, end_num, M, N_list)
  
for i in M_list:
  print(check_num(0, len(N_list)-1, i, N_list))

# def check_num(start_num, end_num, M, N_list):
  
#   while True:
#     mid_num = (start_num+end_num)//2
#     mid_N = N_list[(start_num+end_num)//2]
#     if M == mid_N:
#       return 1
#     elif M < mid_N:
#       end_num = mid_num

#     elif M > mid_N:
#       start_num = mid_num
  
# for M in M_list:
#   start_num = 0
#   end_num = N-1
#   if M > N_list[end_num] or M < N_list[start_num]:
#     print(0)

#   elif M == N_list[end_num] or M == N_list[start_num]:
#     print(1)

#   else:
#     ans = check_num(start_num, end_num+1, M, N_list)
#     print(ans)
