n, k = tuple(map(int, input().split())) # 사람들의 수 n명, 촬영 가능한 사진의 크기 k

# 각 사람들의 위치, 들고 있는 알파벳 입력 받기
people = [
    input().split()
    for _ in range(n)
]

places = [''] * 10001  # 빈 문자열로 배열 초기화

# places 배열의 index가 locat인 위치에 alpha로 선언
for locat, alpha in people:
    locat = int(locat) # 입력 받은 각 사람들의 위치를 정수로 변환
    places[locat] = alpha # 배열 palces의 각 위치(locat)에 alpha 값 선언

max_score = 0
# places 배열 내 모든 k 크기의 구간 조회하는 반복문
for i in range(1, len(places)-k): 
    score = 0 # 각 구간 별 점수
    for j in range(i, i+k+1): # i ~ i + k 구간 조회하는 반복문
        if places[j] == 'G':
            score += 1
        elif places[j] == 'H':
            score += 2
    max_score = max(max_score, score)

print(max_score)