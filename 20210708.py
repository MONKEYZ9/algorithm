# len(list)
# 어떻게 하면 len을 안스고 할 수 있는가
# 리스트의 시간복잡도를 구하는 시간은 뭘까
# 푸쉬와 팝만 할 수 있다고    하면 괜찮다는 거야



def run_cmd_with_stack(cmd, st):
    cmd_type = cmd[0]

    if cmd_type == "push":
        _, num = cmd #이렇게 하면 cmd[1]안해도 되고 이렇게 하면 된다는 거야
        st.append(num)
    elif cmd_type == 'pop':

        print(stack.pop()) # 이렇게 짯을거다
    elif command[0] == 'size':
        print( len(st))
    elif command[0] == 'empty':
        if len(st) > 0 :
            print(1)
        else:
            print( 0)
    
    return stack

n = int(input())
stack = []

for i in range(n):
    command = input().split()
    stack = run_cmd_with_stack(command, stack)


# if result is not None:
#     stack = result

