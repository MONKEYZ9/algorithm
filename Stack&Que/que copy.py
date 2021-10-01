import de

class Que:
    def __init__(self, n):
        self.que_list = [None for _ in range(n)]
        self.que_size = 0
    
    def push(self, num):
        self.que_list[self.size()] = int(num)
        self.que_size += 1
    
    def pop(self):
        if self.size() > 0:
            last_val = self.top()
        
            self.que_list[self.size()-1] = None
            
            self.que_size -= 1
            return last_val
        
        return -1
    def size(self):
        return self.que_size

    def empty(self):
        if self.size() > 0:
            return 0
        
        return 1

    def top(self):
        if self.size() > 0:
            return self.que_list[self.size()-1]
        
        return -1

def run_cmd_with_stack(new_que, cmd):
    cmd_type = cmd[0]
    # cmd_type, num = cmd

    if cmd_type == "push":
        _, num = cmd
        new_que.push(num)
    elif cmd_type == "pop":
        print(new_que.pop())
    elif cmd_type == "size":
        print(new_que.size())
    elif cmd_type == "empty":
        print(new_que.empty())
    elif cmd_type == "top":
        print(new_que.top())
     
    return new_que

n = int(input())
new_que = Que(n)

for _ in range(n):

    command = input().split()
    new_que = run_cmd_with_stack(new_que, command)
    
    print(new_que.stack_list)
    print(new_que.stack_size)