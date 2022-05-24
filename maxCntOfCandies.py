MAX_NUM = 100

n, k = tuple(map(int, input().split())) # 총 바구니 개수 := n, 중심점으로부터 떨어진 거리 := k

# n 개의 바구니의 각 사탕의 개수와 바구니의 좌표 arr에 입력 받기
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

blanket = [0] * (MAX_NUM + 1)  # 101 개의 비어있는 바구니 선언

# locat 번째의 바구니에 존재하는 사탕 개수(cnt) blanket[locat]에 추가
for cnt, locat in arr:
    blanket[locat] = cnt

max_cnt = 0
for i in range(0, 100): # 모든 구간의 시작점 i로 정하고 완전 탐색 진행
    cnt = 0 # 구간 내 사탕의 수
    for j in range(i - k, i + k + 1): # 중심점 c 기준으로 [c-k, c+k] 구간에 조재하는 바구니 위치 조회
        if 0 <= j and j <= 100: # 바구니가 주어진 위치 (MAX_NUM) 벗어나지 않을 경우
            cnt += blanket[j] # 해당 구간 내 존재하는 사탕의 개수 더하기
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)