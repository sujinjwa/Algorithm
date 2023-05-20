from collections import deque
# python에서 제공하는 deque 사용해 queue를 대신하여 이용함
# deque는 collections 라는 모듈에 있음

n = int(input()) # n : 주어지는 명령의 수
orders = [
    input().split() # n줄에 걸쳐 명령 입력 받기
    for _ in range(n)
]

class Queue():
    def __init__(self): # 빈 큐 하나 생성
        self.dq = deque()
    
    def push(self, item): # 큐의 맨 뒤에 데이터 추가
        self.dq.append(item)
    
    def front(self): # 큐의 맨 앞에 있는 데이터 제거하지 않고 반환
        if self.empty():
            # return 'Deque is empty'
            raise Exception('Deque is empty')
        
        return self.dq[0]
    
    def pop(self): # 큐의 맨 앞에 있는 데이터 반환하고 제거
        if self.empty():
            # return 'Deque is empty'
            raise Exception('Deque is empty')
        
        return self.dq.popleft()
    
    def size(self): # 큐에 들어있는 데이터 수 반환
        return len(self.dq)
    
    def empty(self): # 큐가 비어있으면 True 반환
        return not self.dq
    

q = Queue() # 빈 큐 하나를 q라는 변수로 선언

for order in orders:
    if order[0] == 'push':
        q.push(int(order[1]))
    
    elif order[0] == 'front':
        print(q.front())
    
    elif order[0] == 'pop':
        print(q.pop())

    elif order[0] == 'size':
        print(q.size())
    
    else: # 명령어가 "empty"일때 q가 비어 있으면 1, 아니면 0 출력
        print(1 if q.empty() else 0)
