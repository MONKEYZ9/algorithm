import sys


# 그럼 재귀함수로 가보자
def recursive_funtion(store_model, customer_Num, customer_model):
    store_model.sort()
    customer_model.sort()
    start = store_model[0]
    end = store_model[-1]
    mid  = (start + end) // 2
    for i in range(int(customer_Num)):
        while start <= end:
            if customer_model[i] > end:
                return 'no'
            elif mid > customer_model[i]:
                # 지금 5보다 낮다는 거야
                



            elif mid <= customer_model[i]:
                return 'no'

    # 그러니까 3번은 결과를 봐야하잖아 그럼 해보자
    # for i in range(int(customer_Num)):
    #     if 


store = sys.stdin.readline().rstrip()
store_model = sys.stdin.readline().rsplit()

customer_Num = sys.stdin.readline().rstrip()
customer_model = sys.stdin.readline().rsplit()

print(recursive_funtion(store_model, customer_Num, customer_model))