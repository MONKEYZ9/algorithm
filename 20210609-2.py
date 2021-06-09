import sys


# 그럼 재귀함수로 가보자
def recursive_funtion(store_model, customer_Num, customer_model):
    store_model.sort()
    customer_model.sort()

    print(store_model[-1])
    print(store_model)
    # 그러니까 3번은 결과를 봐야하잖아 그럼 해보자
    # for i in range(int(customer_Num)):
    #     if 


store = sys.stdin.readline().rstrip()
store_model = sys.stdin.readline().rsplit()

customer_Num = sys.stdin.readline().rstrip()
customer_model = sys.stdin.readline().rsplit()

print(recursive_funtion(store_model, customer_Num, customer_model))