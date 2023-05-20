from collections import deque

n = int(input()) # 명령의 수 : n개
orders = [
    input().split()
    for _ in range(n)
]

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push_back(self, item):
        self.dq.append(item)
    
    def push_front(self, item):
        self.dq.appendleft(item)
    
    def pop_front(self):
        return self.dq.popleft()
    
    def pop_back(self):
        return self.dq.pop()
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        return not self.dq
    
    def front(self):
        return self.dq[0]
    
    def back(self):
        return self.dq[-1]

q = Queue()

for order in orders:
    if order[0] == 'push_back':
        q.push_back(int(order[1]))
    
    elif order[0] == 'push_front':
        q.push_front(int(order[1]))
    
    elif order[0] == 'pop_front':
        print(q.pop_front())

    elif order[0] == 'pop_back':
        print(q.pop_back())
    
    elif order[0] == 'size':
        print(q.size())
    
    elif order[0] == 'empty':
        print(1 if q.empty() else 0)
    
    elif order[0] == 'front':
        print(q.front())
    
    else:
        print(q.back())