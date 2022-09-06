n = int(input()) # 격자 크기: n

grid = [
    list(map(int, input().split()))
    for _ in range(n) # n개의 줄에 걸쳐 각 행에 n개의 숫자 입력
]

r, c = list(map(int, input().split())) # 폭탄의 중심 위치

r = r - 1 # 폭탄 위치의 행 index
c = c - 1 # 폭탄 위치의 열 index

distance = grid[r][c] # 폭탄이 주변에 영향 미치는 범위
grid[r][c] = 0 # 가장 중심위치 우선 0으로 초기화

# x, y 가 격자를 벗어나는지 확인
def is_inrange(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 폭탄 위치인 r,c 기준 동서남북 방향으로 distance까지 위치한 모든 곳에 폭탄 터뜨리기
for i in range(1, distance):
    
    # r,c에서 동서남북으로 i만큼 떨어진 곳 모두 0으로 초기화
    if is_inrange(r-i, c):
        grid[r-i][c] = 0 # 북

    if is_inrange(r, c+i):
        grid[r][c+i] = 0 # 동

    if is_inrange(r+i, c):
        grid[r+i][c] = 0 # 남

    if is_inrange(r, c-i):
        grid[r][c-i] = 0 # 서

# 폭탄 터진 후 중력 작용한 버전 입력받을
# n * n 크기의 새 배열 new_grid, 모든 칸 0으로 초기화
new_grid = [ [0 for _ in range(n)] for _ in range(n) ]

# 폭탄 터진 후 중력 작용한 결과 new_grid에 업데이트
for i in range(n):
    idx = 0
    for j in range(n - 1, -1, -1): # grid의 각 열마다 마지막 행부터 시작하여 모두 조회
        if grid[j][i] == 0:
            continue
        else:
            new_grid[i][idx] = grid[j][i]
            idx += 1

# 출력
for i in range(n - 1, -1, -1):
    for j in range(n):
        print(new_grid[j][i], end=' ')
    print()