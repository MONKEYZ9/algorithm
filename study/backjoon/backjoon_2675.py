T = int(input())
for i in range(T):
    sen =''
    number, test  = input().split()
    for i in range(len(test)):
        sen += test[i]*int(number)
    print(sen)