# 고득점 KIT > 스택/큐 > '다리를 지나는 트럭' 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    # 다리에 bridge_length대 올라갈 수 있음
    # weight 이하까지의 무게 견딜 수 있음
    
    ans = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while True:
        # while문 종료 조건            
        if len(truck_weights) == 0:
            ans += bridge_length
            break
            
        # bridge의 첫번째를 pop
        # 그리고 bridge 맨 뒤에 truck_weights 의 첫번째 pop 하면서 추가
        # 이때 bridge의 sum이 weight보다 작은지 확인
        # 작을 때만 append 가능
        # 크면 0을 append
        
        bridge.pop(0)
        if sum(bridge) + truck_weights[0] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights.pop(0))
        
        ans += 1
    
    return ans

# list의 pop(0)은 O(N), deque의 popleft()는 O(1)
from collections import deque

def solution(bridge_length, weight, truck_weights):   
    ans = 0
    bridge = deque([0] * bridge_length)
    truck_weights.reverse() # pop(0) 이 아닌 pop()을 써서 시간 복잡도 줄이기 위함
    cur_weight = 0
    
    while truck_weights:
            
        # bridge의 첫번째를 pop
        # 그리고 bridge 맨 뒤에 truck_weights를 pop 한 트럭을 추가
        # 이때 bridge의 sum이 weight보다 작은지 확인
        # 작을 때만 append 가능
        # 크면 0을 append
        
        front = bridge.popleft()
        cur_weight -= front
        if cur_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            num = truck_weights.pop()
            bridge.append(num)
            cur_weight += num
        
        ans += 1
    
    ans += bridge_length
    
    return ans