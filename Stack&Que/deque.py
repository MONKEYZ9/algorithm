from collections import deque

class StackNQueue:
    # 초기화에 대한 부분
    # 값을 넣어놔야 할 것이 필요하다.
    def __init__(self, data_type="stack"):
        self.array = deque()
        self.data_type = data_type

    def push(self, num):
        self.array.append(num)
    
    def pop(self):
        # 비워져있는지 아닌지를 판단하는게 먼저가 될 수 있어
        if self.is_stack():
            # 스택일 경우에는 오른쪽 끝을 지우면 되고
            return self.array.pop()
        return self.array.popleft()

    def is_stack(self):
        return self.data_type == 'stack'

    def size(self):
        return len(self.array)

    def empty(self):
        # return int(self.size() == 0)
        # 이렇게 쓰기보다는 별도로 분리를 해서 보는게 낫다
        return int(self.is_empty)

    def is_empty(self):
        return self.array.size()
        
    def front(self):
        if self.is_stack() or self.is_empty():
            return -1
            # 스택에서는 못쓰는 거니까
        return self.array[0]

    def back(self):
        if self.is_stack() or self.is_empty():
            return -1
            # 스택에서는 못쓰는 거니까
        return self.array[-1]
        # return self.get_last_val() 이걸 이렇게 할 필요가 있는가에 대해 고민해봐라
        #  2개 이상 반복된다고 함수로 만들 필요는 없다는 것을 알아야 한다.

    def top(self):
        if not self.is_stack or self.is_empty():
            return -1
        # top은 
        return self.array[-1]
        
    # def get_last_val(self):
    #     return self.array[-1]

def run_cmd(command, data_obj):
    cmd_type = command[0]
    # cmd_type, num = cmd

    if cmd_type == "push":
        _, num = command
        data_obj.push(num)

    elif cmd_type == "pop":
        print(data_obj.pop())
    elif cmd_type == "size":
        print(data_obj.size())
    elif cmd_type == "empty":
        print(data_obj.empty())
    elif cmd_type == "top":
        print(data_obj.top())
    elif cmd_type == "size":
        print(data_obj.size())
    elif cmd_type == "front":
        print(data_obj.front())
    elif cmd_type == "back":
        print(data_obj.back())



data_type = input() # 스택이냐 큐냐
n = int(input())

# 이걸 기본값으로 넣어줘도 된다.
data_obj = StackNQueue(data_type)

for _ in range(n):
    run_cmd( input().split(), data_obj )