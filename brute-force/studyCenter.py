n = int(input()) # 좌석의 개수 : n개

seats = list(map(int, input())) # n개의 좌석 사용여부 입력 (1: 이미 차 있음. 0: 비어있음)

max_of_min = 0 # 경우마다 가장 가까이 있는 사람 간 거리 중 최댓값

for i in range(n): # i := 새로 배정받은 좌석 idx

    if seats[i] == 1: # 이미 배정받은 좌석이라면
        continue
    
    seats[i] = 1 # 좌석 배정 받기

    min_dis = n # 거리 가장 최소인 경우 구하는 변수
    for j in range(n): # 새로 배정 받은 후, 모든 좌석 간 거리 차이 확인
        
        for k in range(j+1, n):

            if seats[j] == 1 and seats[k] == 1:
                min_dis = min(min_dis, k - j)

    max_of_min = max(max_of_min, min_dis)
    seats[i] = 0 # 좌석 배정 초기화

print(max_of_min)