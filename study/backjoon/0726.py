# # 소수 구하는 걸 만들자
# def get_decimal(num):
#     # 자기 이외에 나눠지면 소수가 아님
#     start_num = 2
#     while True:
#         if num % start_num == 0:
#             break
#         else:
#             start_num += 1


            
# def make_dec_list(m,n):
#     # 소수 리스트
#     decimal_list = []

#     # m, n  사이에서 반복문
#     for num in range(m, n+1):
#         decimal = get_decimal(num)
#         decimal_list.append(decimal)
    
#     return decimal_list

# def get_result(decimal_list):
#     if sum(decimal_list) == 0:
#         print(-1)
#     else:    
#         print(decimal_list)
#         print(sum(decimal_list))
#         print(decimal_list[1])


# decimal_list = make_dec_list(m,n)
# get_result(decimal_list)

def test(m, n):
    new_num_list = []
    for i in range(m,n+1):
        error = 0
        for i2 in range(2, i):
            if i % i2 == 0:
                error += 1
        if error == 0:
            new_num_list.append(i)

    return new_num_list



# 백준 소수값 구하기
m = int(input())
n = int(input())

new_num_list = test(m,n)
if len(new_num_list) == 0:
    print(-1)
else:
    print(sum(new_num_list))
    print(min(new_num_list))





    


