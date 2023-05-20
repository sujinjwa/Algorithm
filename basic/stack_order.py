n = int(input()) # 명령어의 가짓수 입력 받기
# n개의 명령어 한 줄마다 입력 받기
orders = [
    input().split()
    for _ in range(n)
]

class Stack:
    def __init__(self):
        self.arr = [] # 빈 배열(스택) 선언
    
    def push(self, num): # 스택에 데이터 추가
        self.arr.append(num)
    
    def pop(self): # 스택의 가장 위에 있는 데이터 반환 후 제거
        print(self.arr[-1])
        self.arr.pop()
    
    def size(self): # 스택에 잉ㅆ는 데이터 수 반환
        print(len(self.arr))
    
    def empty(self): # 스택 비어있으면 1 반환, 아니면 0 반환
        if len(self.arr):
            print(0)
        else:
            print(1)
    
    def top(self): # 스택의 가장 위에 있는 데이터 제거하지 않고 반환
        print(self.arr[-1])

arr = Stack() # 스택 선언

for order in orders: # 명령어 순서대로 처리
    if order[0] == 'push':
        arr.push(int(order[1]))

    elif order[0] == 'pop':
        arr.pop()

    elif order[0] == 'size':
        arr.size()

    elif order[0] == 'empty':
        arr.empty()

    else:
        arr.top()