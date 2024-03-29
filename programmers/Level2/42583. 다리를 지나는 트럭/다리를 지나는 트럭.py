from collections import deque

def solution(bridge_length, weight, truck_weights):
    # bridge_length: 다리에 올라갈 수 있는 최대 트럭 수 (다리 길이)
    # weight: 다리가 견딜 수 있는 최대 무게
    # truck_weights: 순서대로 건너야 하는 트럭들 (1차원 배열)

    answer = 0
    truck_weights = deque(truck_weights) # 남아있는 트럭들 (type: deque)
    bridge = deque([0 for _ in range(bridge_length)]) # 다리의 상태 (type: deque)
    sum = 0 # 현재 다리 위에 있는 모든 트럭의 무게 총합

    while True:
        # 1초 지날 때마다 다리 맨 앞 칸 제거
        first_bridge = bridge.popleft()
        sum -= first_bridge
        answer += 1 # 1초 지남

        # 모든 다리에 트럭 없고, 모든 트럭 건넜으면 break
        if answer > 0 and sum == 0 and len(truck_weights) == 0:
            break

        # 아직 남아있는 트럭이 있고, 남아있는 맨 앞의 트럭이 다리에 건널 수 있으면 bridge에 추가
        if len(truck_weights) != 0 and sum + truck_weights[0] <= weight:
            first_truck = truck_weights.popleft()
            bridge.append(first_truck)
            sum += first_truck
        
        # 건널 수 없으면 bridge에 0 추가
        else:
            bridge.append(0)

    return answer