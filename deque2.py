from collections import deque

n = int(input()) # 1부터 n까지의 정수가 오름차순으로 정렬

class Deque:
    def __init__(self, n):
        self.dq = deque() # 빈 덱 생성
        
        for i in range(1, n+1): # 1부터 n까지의 정수 순서대로 self.dq에 추가
            self.dq.append(i)
    
    def push_back(self, item):
        self.dq.append(item)
    
    def pop_front(self):
        return self.dq.popleft()
    
    def front(self):
        return self.dq[0]
    
    def size(self):
        return len(self.dq)

q = Deque(n) # 1부터 n까지의 정수가 오름차순으로 정렬된 덱 q 생성

while q.size() != 1: # 해당 덱의 정수가 하나만 남을 때까지 while문 반복
    
    q.pop_front() # 맨 앞 정수 제거
    q.push_back(q.pop_front()) # 남은 수열의 맨 앞의 정수 맨 뒤로 이동

print(q.front()) # 마지막으로 남은 정수 출력