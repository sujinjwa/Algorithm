n = int(input()) # 곱셈 반복 횟수 : n번
# 2를 곱할 때마다의 숫자 범위(ai, bi) 단서 입력
info = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_answer = info[0][1]//2

# 1부터 첫 번재 info의 2번째 값으로 주어진 값의 //2 한 것까지 for문 돌리면 됨
for i in range(1, info[0][1]//2):
    
    answer = True # 2씩 곱해지는 i가 모든 a, b 사이에 존재하는지 확인하는 변수
    for a, b in info:
        # i를 2 곱하며, a, b 사이에 존재하는지 확인
        # 존재하지 않으면 answer = False 후 break 실행
        
        i *= 2

        if i < a or i > b:
            answer = False
            break
    
    for _ in range(n): # i 원래 값으로 초기화
        i //= 2

    if answer:
        min_answer = min(min_answer, i) # 해당 조건 만족하는 i 중 최솟값 구하기
    

print(min_answer)