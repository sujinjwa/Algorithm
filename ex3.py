def solution(n, plans, clients):
    # 1 ~ m번 : 휴대폰 요금제
    # 1 ~ n번 : 부가 서비스
    # plans (2차원 배열, 문자열) : 제공하는 요금제 및 부가 서비스
    # clients (2차원 배열, 문자열) : 원하는 요금제 및 부가 서비스
    
    # 추가된 부가 서비스 포함시키기
    plus = []
    plus_service = []
    for plan in plans:
        plan = list(map(int, plan.split()))

        for i in range(1, len(plan)):
            plus.append(plan[i])
        
        plus_service.append(list(plus))
    # print(plus_service)


    answer = []
    for client in clients: # 모든 고객 조회
        arr = list(map(int, client.split())) # 각 고객 하나씩 조회
        client_data = arr[0] # 각 고객 원하는 데이터

        find = False  
        plus = []
        for j in range(len(plans)): # 각 요금제 조회
            plan = list(map(int, plans[j].split())) # 각 요금제 정보 하나씩 조회
            plan_data = plan[0] # 각 요금제 제공 데이터
            # print(plan)

            if client_data > plan_data: # 만족하는 요금제 데이터 아닌 경우
                continue

            cnt = 0

            # 원하는 부가 서비스 들어있는지 확인
            for i in range(len(plus_service[j])):
                for k in range(1, len(arr)): # 특정 고객이 원하는 부가 서비스
                    if plus_service[j][i] == arr[k]:
                        # print(plus_service[j], arr[k])
                        cnt += 1

            if cnt == (len(arr) - 1):
                find = True
                break

        if find == False:
            answer.append(0)
        else:
            answer.append(j + 1)
    
    return answer