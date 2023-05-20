# python에는 이중연결리스트 구현체에 해당하는 list라는 class 없음
# 따라서 list 자료구조를 사용하기 위해서 class 만들어줘야 함

# Node 클래스 생성
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# 이중 연결 리스트 클래스 생성
class DoublyLinkedList:
    def __init__(self):
        self.head = None # 해당 리스트의 head가 어떤 노드인지
        self.tail = None # 해당 리스트의 tail이 어떤 노드인지
        self.node_num = 0 # 해당 리스트 내 노드 수

    def push_front(self, new_data): # 원소(new_data)를 첫 번째 위치에 추가
        new_node = Node(new_data) # 새로운 노드 만들기
        new_node.next = self.head # 새로운 노드의 next 값을 head로 변경

        if self.head != None: # 기존 리스트 비어있지 않았다면 (*주의! Null이 아니라 None)
            self.head.prev = new_node # 이전 head의 prev값을 새로운 노드 값으로 바꾼 뒤
            self.head = new_node # head값 new_node로 변경
            new_node.prev = None
        
        else: # 기존 리스트 비어있었다면
            self.head = new_node # head, tail 새로 설정
            self.tail = new_node
            new_node.prev = None
        
        self.node_num += 1 # 리스트 내 노드 수 1 증가
    
    def push_back(self, new_data): # 원소(new_data)를 맨 끝 위치에 추가
        new_node = Node(new_data) # 새로운 노드 만들기
        new_node.prev = self.tail # 새로운 노드의 prev값을 tail로 변경

        if self.tail != None: # 기존 리스트 비어있지 않았다면
            self.tail.next = new_node # 이전 tail의 next값을 new_node로 바꾼 뒤
            self.tail = new_node # tail값 new_node로 변경
            new_node.next = None
        
        else: # 기존 리스트 비어있었다면
            self.head = new_node # head, tail 새로 설정
            self.tail = new_node
            new_node.next = None

        self.node_num += 1 # 리스트 내 노드 수 1 증가
    
    def pop_front(self): # 첫 번째 수 빼고, 그 수 반환

        if self.head == None: # 기존 리스트 비어있다면
            print("List is empty")
        
        elif self.head.next == None: # 노드가 하나 남아있다면
            temp = self.head # 삭제할 노드

            self.head = None # head값을 None으로 변경해주고
            self.tail = None # tail값도 None으로 변경해주고
            self.node_num = 0 # 원소의 수도 0개로 변경
            return temp.data
        
        else: # 노드가 두 개 이상 남아있다면
            temp = self.head # 삭제할 노드

            """ 이렇게는 작성할 수 없는건가?
            self.head.next = None
            self.head = self.head.next
            self.node_num -= 1
            """
            temp.next.prev = None # 새로 node가 될 노드의 prev 값 지워줌
            self.head = temp.next # head값을 temp.next로 변경
            temp.next = None # 이전 head의 next 값 지워줌

            self.node_num -= 1 # 리스트 내 노드 수 1 감소
            return temp.data
    
    def pop_back(self): # 맨 끝에 있는 수 빼고, 그 수 반환
        if self.tail == None: # 리스트에 노드가 없다면
            print("List is empty")
        
        elif self.tail.prev == None: # 리스트에 노드가 1개 있다면
            temp = self.tail # 삭제할 노드
        
            self.head = None # head값을 None으로 변경
            self.tail = None # tail값도 None으로 변경

            self.node_num = 0 # 원소의 수 0개로 변경
            return temp.data
        
        else: # 리스트에 노드가 2개 이상 있다면
            temp = self.tail # 삭제할 노드
            temp.prev.next = None # 새로 tail이 될 노드의 next값 지워줌
            self.tail = temp.prev # tail값을 temp.prev로 변경
            temp.prev = None # 이전 tail의 prev 값 지워줌
            
            self.node_num -= 1 # 원소의 수 1개 감소
            return temp.data
        
    def size(self):
        return self.node_num
    
    def empty(self):
        return self.node_num == 0
    
    def front(self): # 첫 번째 수 반환
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data
    
    def back(self): # 맨 끝에 잇는 수 반환
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


l = DoublyLinkedList() # list 선언 (빈 연결리스트)
l.push_front(3) # 맨 앞에 3 추가
l.push_back(4) # 맨 뒤에 4 추가
print(l.front()) # 맨 앞에 있는 숫자인 3 출력
print(l.pop_front()) # 맨 앞에 있는 숫자 3 출력되고 제거
l.push_front(6) # 맨 앞에 6 추가
print(l.front()) # 맨 앞에 있는 숫자인 6 출력
print(l.size()) # 원소의 개수 출력 => 2