# 두 명의 새로운 사람이 오는 버전

n = int(input()) # 좌석의 개수 : n개
seats = input() # 0 : 공석, 1 : 자리 있음

seats = list(seats) # 문자열에서 list로 변환

max_min = 0
# 두 명을 비워진 자리에 집어 넣었을 때의 모든 경우 조회
for i in range(n):
    
    if seats[i] == '1': # 자리 있을 경우 그 다음 자리 조회
            continue

    seats[i] = '1' # 새로 온 한 명 자리에 앉기

    for j in range(i+1, n):

        if seats[j] == '1': # 자리 있을 경우 그 다음 자리 조회
            continue

        seats[j] = '1' # 새로 온 나머지 한 명 자리에 앉기

        dis_arr = []
        for k in range(n):
            # 새로 온 두 명 포함한 모든 좌석 조회
            # 사람 간 거리 중 최솟값 구하기

            if seats[k] == '1': # 사람 있는 자리의 index 모두 dis_arr 배열에 append
                dis_arr.append(k)
            
        # print(dis_arr)
        min_dis = n # 사람 간 거리 중 최솟값 구하기 위한 변수
        length = len(dis_arr)

        for l in range(length - 1): # 사람 간 거리 구한 후, 그 중 최솟값 구하기
            dis = dis_arr[l+1] - dis_arr[l]

            min_dis = min(min_dis, dis)

        # print(min_dis)
        max_min = max(max_min, min_dis)
    
        seats[j] = 0 # j가 앉았던 자리 다시 공석으로 초기화
    seats[i] = 0 # i가 앉았던 자리 다시 공석으로 초기화

print(max_min)