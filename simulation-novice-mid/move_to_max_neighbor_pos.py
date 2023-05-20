n, m, t = list(map(int, input().split()))
# n : 격자의 크기, m : 구슬의 개수, t: 흐른 시간(초)

# n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 각 구슬 위치 여부에 따라 1, 0 으로 기록할 격자 생성
cnt = [
    [0] * n
    for _ in range(n)
]

# 이동 후 각 구슬의 위치 여부에 따라 1, 0 으로 기록할 격자 생성
next_cnt = [
    [0] * n
    for _ in range(n)
]

# m개의 줄에 걸쳐 각 구슬의 시작 위치 입력 받고,
# cnt에서 해당 위치에 1로 기록
for _ in range(m):
    r, c = list(map(int, input().split()))
    r, c = r - 1, c - 1
    
    cnt[r][c] = 1

#      상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 위치(x, y)가 해당 격자를 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 인접한 위치의 숫자들 중 최댓값 찾고, 최댓값과 r,c에 위치한 값끼리 위치 이동
def swap(r, c):

    global grid, cnt, next_cnt

    max_num = -1
    x, y = 0, 0
    for dx, dy in zip(dxs, dys):

        # 격자 벗어나지 않는 최댓 값과 그 위치 x, y에 저장
        if in_range(r+dx, c+dy) and grid[r+dx][c+dy] > max_num:
            max_num = grid[r+dx][c+dy]
            x = r + dx
            y = c + dy
    
    # next_cnt배열에서 최댓 값의 위치에 1 저장
    next_cnt[x][y] += 1

    # 두 값 교환 -> 교환을 왜 한 겨?!?? 문제 제대로 읽자...
    #temp = grid[r][c]
    #grid[r][c] = grid[x][y]
    #grid[x][y] = temp

    # 이동한 각 구슬의 위치 cnt 배열에 업데이트
    #cnt[r][c] -= 1
    #cnt[x][y] += 1
    

# t초마다 구슬 움직이기
for _ in range(t):
    
    next_cnt = [
    [0] * n
    for _ in range(n)
    ]
    
    # 해당 구슬 위치에서 상하좌우 조회해서 가장 큰 값 있는 위치로 이동
    for r in range(n):
        for c in range(n):
            if cnt[r][c] == 1: # 만약 구슬이 있다면
                swap(r, c)

    # cnt에 next_cnt 복사하여 
    # 이동한 각 구슬의 위치 cnt배열에 업데이트
    # cnt = next_cnt 도 python에서는 가능하지 않나? (가능하다!)
    for i in range(n):
        for j in range(n):
            cnt[i][j] = next_cnt[i][j]

    # cnt 조회하고, 2 이상인 경우 cnt 없애기
    for i in range(n):
        for j in range(n):
            if cnt[i][j] >= 2:
                cnt[i][j] = 0

# cnt 조회해서 t초 후 최종 구슬 개수 출력
answer = 0
for row in cnt:
    for elem in row:
        if elem == 1:
            answer += 1

print(answer)