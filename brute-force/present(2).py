n, B = tuple(map(int, input().split())) # 학생 수 : n명, 예산 : B원

# 각 학생의 선물 가격 입력 받기
prices = [
    int(input())
    for _ in range(n)
]

max_student = 0 # 학생 최대 명수 구하기 위한 변수

for i in range(n): # i번째 선물에 쿠폰 쓸 때 선물 가능한 학생의 명수 구하기

    prices[i] //= 2 # i번째 선물에 쿠폰 적용
    sorted_p = sorted(prices) # 쿠폰 적용한 상태로 오름차순 정렬

    sum_price = 0 # 가격의 합
    student = 0 # 선물 받을 수 있는 학생 명수

    for j in range(n): # 예산보다 커지기 전까지 선물 받는 최대 학생 명수 구하기

        sum_price += sorted_p[j] # 작은 금액부터 가격 더하기

        if sum_price > B: # 선물 가격 합이 예산보다 커진 경우
            break

        student += 1 # 예산보다 커지지 않은 경우 학생 수 + 1

    max_student = max(max_student, student)
    prices[i] *= 2 # 적용된 쿠폰 초기화

print(max_student)