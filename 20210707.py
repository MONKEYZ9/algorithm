
# 강사님이 추천해주신 구조
def process_stack(command):
    # command에는 pop top push empty size
    li = []
    if command[0] == 'push':
        li.append(command[1])
        print(li[-1])
    elif command[0] == 'top' or 'pop':
        if not li:
            print(-1)
        else:
            if command[0] == 'pop':
                lastNum = li[-1]
                li.pop()
                print( lastNum)
            else:
                print( li[-1])
    elif command[0] == 'empty':
        if not li:
            print(1)
        else:
            print( 0)
    elif command[0] == 'size':
        print( len(li))

N = int(input('N : '))

for i in range(N):
    command = input().split(" ")
    process_stack(command)

