# 프로그래머스 > 스택/큐 > 프로세스 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
# deque로 popleft, append 등 사용 가능

def solution(priorities, location):
    priorities = deque([x for x in priorities]) # priorities = 프로세스 별 우선순위
    arr = deque([i for i in range(len(priorities))]) # arr = 프로세스 별 인덱스

    count = 1 # count = 각 프로세스의 실행 번째수
    
    while True:
        if len(arr) <= 0: # 모든 프로세스가 실행된 경우 while문 종료
            break
        
        index = arr[0] # index = 실행 가능 여부 확인 위한 첫번째 프로세스의 인덱스
        prior = priorities[0] # prior = 실행 가능 여부 확인 위한 첫번째 프로세스의 우선순위
        CAN_BE_OUT = True # CAN_BE_OUT = 현재 실행 가능한가
        
        for num in priorities:
            # 첫번째 프로세스보다 우선순위 높은 게 뒤에 있는 경우
            # 첫번째 프로세스를 맨 뒤로 이동
            if num > prior:
                arr.popleft()
                arr.append(index)
                priorities.popleft()
                priorities.append(prior)
                CAN_BE_OUT = False
                break
        
        if CAN_BE_OUT: # 현재 실행 가능한 프로세스라면
            if location == arr[0]: # 실행 순서를 찾고자 하는 프로세스라면 실행 번째수 리턴
                return count
            
            # 첫번째 프로세스 실행 및 종료
            arr.popleft()
            priorities.popleft()
            count += 1 # 실행 번째수 + 1



# 두번째 풀이
# deque가 아닌 list를 가지고 pop(0), append() 사용해서 푼 방법
def solution(priorities, location):
    queue = [(index, prior) for index, prior in enumerate(priorities)]
    answer = 0

    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # 해당 프로세스 아직 실행하지 못하는 경우라면
            queue.append(cur)
        else: # 해당 프로세스 실행할 수 있으면
            answer += 1
            if cur[0] == location:
                return answer
            

print(solution([1, 1, 3, 2, 2], 2))