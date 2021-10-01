# def insertion_sort(num_list, n):
#     bef_n_list = num_list.copy()

#     for i in range(bef_n_list):
#         bef_n_list[i]
#         bef_n_list[i-1 ]


#     # 밑의 과정을 반복할거니까 반복문을 써보자
#     # for i in range(n):
#     #     if i == n-1:
#     #         return dict.values()
#     #     f_n = dict[i]
#     #     b_n = dict[i+1]
#     #     if f_n > b_n:
#     #         dict[i]= b_n
#     #         dict[i+1] = f_n
#     #     while i > 0:
#     #         f_n = dict[i-1]
#     #         b_n = dict[i]
#     #         if f_n > b_n:
#     #             dict[i-1]= b_n
# #     #             dict[i] = f_n
# #             i -= 1

# # def selection_sort(num_list, n):
# #     # num이 인덱스가 되어 뒤에 있는 인덱스를 바꿔주자
# # #     dict = {i : num for i, num in enumerate(num_list)}

# # #     new_num_list = []
# # #     remove_key = []

# #     for _ in range(n):
# #         for key, value in dict.items():
# #             if value == min(dict.values()):
# #                 new_num_list.append(value)
# #                 remove_key.append(key)
# #         del dict[remove_key[-1]]
# #     return new_num_list

# # def bubble_sort(num_list, n):
# #     dict = {i : num for i, num in enumerate(num_list)}
# # #     # 밑의 과정을 반복할거니까 반복문을 써보자
# # #     for i in range(n-1, 0, -1):
# # #         start_num = 0
# # #         while start_num != i:
# # #             if dict[start_num] > dict[start_num + 1]:
# # #                 dict[start_num], dict[start_num + 1] = dict[start_num + 1], dict[start_num]
# # #             start_num += 1
# # #     return dict.values()
        

# # n = int(input())
# # num_list = []

# # for _ in range(n):
# #     num = int(input())
# #     num_list.append(num)

# # insertion_sorted_list = insertion_sort(num_list, n)
# # print(" ".join(map(str, insertion_sorted_list)))
# # selection_sorted_list = selection_sort(num_list, n)
# # print(" ".join(map(str, selection_sorted_list)))
# # bubble_sorted_list = bubble_sort(num_list, n)
# # print(" ".join(map(str, bubble_sorted_list)))