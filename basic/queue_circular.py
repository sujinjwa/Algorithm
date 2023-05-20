from collections import deque
# python에서 제공하는 deque 사용해 queue를 대신하여 이용함
# deque는 collections 라는 모듈에 있음

n, k = list(map(int, input().split())) # n : 사람의 수, k : 제거될 사람의 번째 수

class Queue:
    def __init__(self, n):
        self.dq = deque() # 빈 큐 하나 생성
        for i in range(1, n+1):
            self.dq.append(i) # 생성한 큐에 1부터 n까지 순서대로 추가
    
    def push(self, item): # 큐의 맨 뒤에 item 추가
        self.dq.append(item)
    
    def pop(self): # 큐의 맨 앞에 있는 데이터 반환하고 제거
        if len(self.dq) == 0:
            raise Exception("Error")
        return self.dq.popleft()

    def front(self): # 큐의 맨 앞에 있는 데이터 제거하지 않고 반환
        if len(self.dq) == 0:
            raise Exception("Error")
        return self.dq[0]
    
    def size(self): # 큐에 들어있는 데이터 수 반환
        return len(self.dq)

q = Queue(n) # n이라는 인자 보내, 1부터 n까지 순서대로 원소 가지는 큐 생성

while q.size() != 0: # 큐에 인자가 한 개도 남지 않을 때까지만 반복

    # 큐의 맨 앞에 위치한 q.front() 를 맨 뒤에 추가하고
    # 맨 앞의 데이터는 삭제하는 과정을 k-1번 만큼 반복
    for _ in range(k - 1):
       q.push(q.front())
       q.pop()
    
    # 앞에서 k - 1번 만큼 for문 돈 후
    # k번째에 위치한 데이터 반환 후 제거
    print(q.pop(), end=' ')
