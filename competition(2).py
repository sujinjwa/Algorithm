n = int(input()) # 점수 변동 목록의 수
info = [
    list(input().split()) # 점수 변동 관련 정보 입력 받기
    for _ in range(n)
]

# ABC : 0, A : 1, B : 2, C : 3, AB : 4, BC : 5, AC : 6
honors = 0 # 명예의 전당에 올라간 조합 정수로 나타내는 변수
scoreA, scoreB, scoreC = 0, 0, 0
cnt = 0 # 조합 변경된 횟수
for c, s in info:
    # c : 학생에 대한 정보, 'A', 'B', 'C' 중 하나
    # s : 점수 변동값

    s = int(s)
    post_honors = honors # 지난 번에 명예의 전당에 올라간 조합의 정수 honors로 초기화

    # step 1. 해당 학생에게 s만큼 점수 부여하기
    if c == 'A':
        scoreA += s
    
    elif c == 'B':
        scoreB += s
    
    else:
        scoreC += s
    
    # step 2. 세 명의 학생 점수 비교하여 honors 갱신
    if scoreA == scoreB == scoreC:
        honors = 0
    
    if scoreA > scoreB and scoreA > scoreC:
        honors = 1
    
    if scoreB > scoreA and scoreB > scoreC:
        honors = 2
    
    if scoreC > scoreB and scoreC > scoreA:
        honors = 3

    if scoreA == scoreB and scoreB > scoreC:
        honors = 4
    
    if scoreB == scoreC and scoreC > scoreA:
        honors = 5
    
    if scoreA == scoreC and scoreC > scoreB:
        honors = 6

    # step 3. post_honors와 honors 비교하여 조합 변경되었는지 확인
    if post_honors != honors:
        cnt += 1

print(cnt)