MAX_NUM = 100

n = int(input()) # 사람들의 수
arr = [0] * (MAX_NUM + 1) # 일직선 상 101칸의 빈 공간

# n개의 줄에 걸쳐 각 사람의 위치와 알파벳 입력 받기
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    arr[x] = 1 if c == 'G' else 2 # 'G'이면 1, 아니면 2

max_len = 0 # 사람 간의 최대 거리
for i in range(MAX_NUM + 1):
    for j in range(i + 1, MAX_NUM + 1):
        # i 와 j 위치에 사람 있는지 확인
        if arr[i] == 0 or arr[j] == 0:
            continue
            
        # 해당 구간 내 g와 h의 개수 구하기
        cnt_g = 0
        cnt_h = 0

        # [i, j] 구간 내 g와 h 개수 구하기
        for k in range(i, j + 1):
            if arr[k] == 1:
                cnt_g += 1 # 구간 내 'G'가 있을 때 cnt_g + 1
            if arr[k] == 2:
                cnt_h += 1 # 구간 내 'H'가 있을 때 cnt_H + 1
        
        # 조건 만족할 경우  구간의 길이 구해 최댓값과 비교
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            leng = j - i
            max_len = max(max_len, leng)

print(max_len)