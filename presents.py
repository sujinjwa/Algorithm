n, B = tuple(map(int, input().split())) # 학생 수 : n명, 예산 : B원
# 각 학생의 선물 가격
p = [
    int(input())
    for _ in range(n)
]

ans = 0 # 학생 최대 명수 구하기 위한 변수

# 한 명의 학생에 선물 쿠폰 쓸 때 선물 가능한 학생의 최대 명수 구하기
for i in range(n):
    # i번째 학생의 선물에 쿠폰 쓸 때 선물 가능한 학생 수 구하기

    # tmp 배열 만들어 i번째 학생의 선물에 쿠폰 쓸 때
    # 각 학생의 원하는 선물 가격 저장
    tmp = [
        p[j]
        for j in range(n)
    ]
    tmp[i] /= 2

    # 학생을 선물 가격 오름차순으로 정렬
    # 선물 가격이 가장 작은 학생부터 선물 사 줄 때,
    # 반드시 갖아 많은 학생에게 선물 줄 수 있기 때문
    tmp.sort()

    student = 0 # 선물 받은 학생 수
    cnt = 0 # 현재까지 쓴 돈

    # 가장 많은 학생에게 선물 줄 때, 그 학생 수 구하기
    for j in range(n):
        if cnt + tmp[j] > B: # 예산을 넘을 경우
            break
        cnt += tmp[j] # 선물 가격을 쓴 돈(cnt)에 더하기
        student += 1
    
    ans = max(ans, student)

print(ans)