MAX_D = 1000

n = int(input()) # n : 좌석의 개수
seats = list(map(int, input())) # '0'과 '1'로 이루어진 문자열 입력 받기
# 0 : 비어있음
# 1 : 이미 차 있음

max_of_min = 0 # 가장 가까운 두 사람 간 거리 중 최댓값
for i in range(n):
    if seats[i] == 1: # 이미 사람 있던 자리는 그대로 두기
        continue
    
    seats[i] = 1 # 빈 자리에 1 넣기

    min_dis = MAX_D
    for j in range(n - 1):
        # 새로운 사람 들어왔을 때
        # 1 간의 거리가 가장 가까운 경우의 거리 구하기 
        dis = 0
        if seats[j] == 1:
            # 모든 1 간 거리 구하기
            # seats[j] == 1인 곳부터 seats[k] == 1인 곳까지의 거리
            # dis에 1씩 더하며 구하기
            for k in range(j + 1, n):
                dis += 1
                
                if seats[k] == 1:
                    break
        else:
            continue
            
        min_dis = min(min_dis, dis) # 모든 1 간 거리 중 최솟값 구하기

    max_of_min = max(max_of_min, min_dis)
    seats[i] = 0 # 새로운 사람 들어왔던 자리 초기화

print(max_of_min)