# N개의 수가 주어졌을 때,
#  이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# # 둘째 줄부터 N개의 줄에는 수가 주어진다.
# #  이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
# # 수는 중복되지 않는다.

# N = int(input())
# N_list = [int(input()) for _ in range(N)]

# # a=[1,2,3,4,5]
# # print(N_list+a)

# # 5 4 3 2 1
# # 2개 이상이면 쪼개고
# # 5 4 3  2 1 
# # 2개 이상이면 쪼개고
# # 5 4   3   2 1
# # 2개면 비교하고 
# # 4 5   3   1 2
# # 2개중 앞거랑 뒤 배열의 앞거랑 비교하고
# # 4 5   1 2
# # 3
# # 5   1 2
# # 3 4 
# #    1 2
# # 3 4 5
   
# # 3 4 5 1 2


# # 3 4 5   2 
# # => 1 
# # 3 4 5  
# # => 1 2
# # 3 4 5  
# # => 1 2 3 4 5 

# # def merge_sort()

# def merge_sort(list):
#     if len(list) <= 1:
#         return list
#     mid = len(list) // 2
#     leftList = list[:mid]
#     rightList = list[mid:]
#     leftList = merge_sort(leftList)
#     rightList = merge_sort(rightList)
#     return merge(leftList, rightList)

# def merge(leftList, rightList):
#     merged_list = []
#     l, h = 0, 0

#     while l < len(leftList) and h < len(rightList):
#         if (leftList[l] < rightList[h]):
#             merged_list.append(leftList[l])
#             l+=1
#         else:
#             merged_list.append(rightList[h])
#             h+=1
#     merged_list += leftList[l:]
#     merged_list += rightList[h:]
#     return merged_list


# print(merge_sort(N_list))



import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in sorted(l):
    print(str(i)+'\n')

