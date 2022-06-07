# 사람의 수 : n명, 치즈의 수 : m개, 치즈 먹은 기록의 수 : d개, 아픈 기록의 수 : s개
n, m, d, s = tuple(map(int, input().split()))

ds = [
    list(map(int, input().split())) # 몇 번째 사람(p), 몇 번째 치즈(m), 언제 먹었는지(t)
    for _ in range(d)
]

ss = [
    list(map(int, input().split())) # 몇 번째 사람(p), 언제 아팠는지(t)
    for _ in range(s)
]

ans = 0 # 최대 약 필요한 개수 구하기 위한 변수

for i in range(1, m+1): # i번째 치즈가 상한 경우 약 먹어야 하는 최대 사람 수 구하기
    
    sickPeople = 0 # 아픈 사람 수
    # 아픈 사람 모두가 아파지기 전에 i번째 치즈 먹었는가?
    for person, sick in ss: # 아픈 사람 모두 조회
        
        # person : 아픈 사람의 위치(번째)
        # sick : 아픈 시기

        for eatingPerson, cheese, eat in ds: # 치즈 먹은 기록 모두 조회

            # eatingPerson : 치즈 먹은 사람 위치(번째)
            # cheese : 치즈 종류
            # eat : 치즈 먹은 시기

            # 아픈 사람이 먹은 치즈 종류가 i번째 치즈이고,
            # 치즈 먹은 시기가 아프게 된 시기보다 앞서게 된 경우가 하나라도 있을 경우
            if cheese == i and person == eatingPerson and eat < sick:
                sickPeople += 1
                break
        
    cnt = 0 # i번째 치즈 먹은 사람의 수
    if sickPeople == s: # 모든 아픈 사람이 i번째 치즈 먹은 경우 = i번째 치즈 상했을 가능성 있음
                
        for j in range(1, n+1): # 각 j번째 사람마다 i번째 치즈 먹었는지 확인
                    
            for k in range(d):

                if i == ds[k][1] and j == ds[k][0]: # i번째 치즈 먹었을 때
                    cnt += 1
                    break

    ans = max(ans, cnt) # 아픈 사람이 최대인 경우의 명수
    
print(ans)