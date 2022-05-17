n = int(input()) # 격자의 크기

# n * n 크기의 격자 정보 입력 받기
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0 # 동전의 최대 개수
# (i, j) 칸과 (k, l) 칸 순회하는 반복문
for i in range(n):
    for j in range(n-2): # (i, j)부터 (i, j+2)까지 조회해야 하므로 인덱스 범위 초과하지 않도록 열은 n-2까지 순회
        for k in range(n):
            for l in range(n-2):
                if i == k and (l - j) <= 2: # (i, j)칸과 (k, l)칸의 행이 같고(i==k), 열이 2칸 이하의 거리에 위치((l-j) <= 2)할 때
                    continue # 즉, 두 격자가 겹치는 경우엔 pass
                else:
                    cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] # (i, j)부터 (i, j+2)까지의 동전 개수
                    cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2] # (k, l)부터 (k, l+2)까지의 동전 개수
                    max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)