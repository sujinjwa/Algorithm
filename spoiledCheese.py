# 클래스 선언
class Info1:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class Info2:
    def __init__(self, p, t):
        self.p, self.t = p, t

# 변수 선언 및 입력
# 사람의 수 : n명, 치즈의 수 : m개, 치즈 먹은 기록의 수 : d개, 아픈 기록의 수 : s개
n, m, d, s = tuple(map(int, input().split()))

given_inputs = [
    tuple(map(int, input().split())) # 몇 번째 사람(p), 몇 번째 치즈(m), 언제 먹었는지(t)
    for _ in range(d)
]

info1 = [
    Info1(p, m, t)
    for (p, m, t) in given_inputs
]

given_inputs2 = [
    tuple(map(int, input().split())) # 몇 번째 사람(p), 언제 아팠는지(t)
    for _ in range(s)
]

info2 = [
    Info2(p, t)
    for (p, t) in given_inputs2
]

ans = 0 # 약 필요한 최대 개수 구하기 위한 변수

# 하나의 치즈 상했을 때 필요한 약의 수 최댓값 구하기
for i in range(1, m+1):
    
    # i번째 치즈 상했을 때 필요한 약의 수 구하기
    
    # 우선 i번째 치즈 상했다고 가정할 때 모순 발생하지 않는지 확인
    # time 배열 만들어 각 사람이 언제 치즈 먹었는지 저장
    time = [0] * (n + 1)

    for info in info1:
        # i번째 치즈에 대한 정보 아닌 경우 넘어가기
        if info.m != i:
            continue
            
        # person이 i번째 치즈 처음 먹었거나
        # 이전보다 더 빨리 먹게 된 경우 time 배열 갱신
        person = info.p
        if time[person] == 0:
            time[person] = info.t
        elif time[person] > info.t:
            time[person] = info.t
        
        # possible : i번째 치즈 상했을 수 있으면 true, 아니면 false
        possible = True

        for info in info2:
            # person이 i번째 치즈 먹지 않았거나
            # i번째 치즈 먹은 시간보다 먼저 아픈 경우 모순 발생
            person = info.p
            if time[person] == 0:
                possible = False
            if time[person] >= info.t:
                possible = False
        
        # 만약 i번째 치즈 상했을 가능성 있다면, 몇 개의 약 필요한지 확인
        pill = 0
        if possible:
            # 한 번이라도 i번째 치즈 먹은 적 있다면, 약 필요
            for j in range(1, n+1):
                if time[j] != 0:
                    pill += 1
        
        ans = max(ans, pill)

print(ans)