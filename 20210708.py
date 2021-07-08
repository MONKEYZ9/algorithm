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

