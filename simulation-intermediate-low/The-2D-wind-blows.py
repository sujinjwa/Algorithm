# 문제 링크
# https://www.codetree.ai/missions/2/problems/The-2D-wind-blows/description

# n : 행 크기, m : 열 크기, q : 총 바람이 분 횟수
n, m, q = map(int, input().split())

# grid : n * m 크기의 건물 상태 입력 받기
grid = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]

# grid의 0번째 행, 0번째 열은 0으로 두고 
# 그 이후의 칸부터 입력 받은 값들 저장
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        grid[i + 1][j + 1] = arr[j]

# winds : q개의 바람 정보(r1, c1, r2, c2) 입력 받기
# (r1, c1) : 바람에 영향 받는 직사각형 좌측 상단 위치
# (r2, c2) : 바람에 영향 받는 직사각형 우측 하단 위치
winds = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

# 주의! grid[1][1]부터 숫자 입력 받았으므로
# 격자 벗어나는지 판단하는 범위도 1 <= x <= n, 1 <= y <= m 이어야 함
def in_range(x, y):
    return 1 <= x and x < n + 1 and 1 <= y and y < m + 1


# 직사각형의 오른쪽 상단 위치 값을 tmp로 저장해둔 후
# 직사각형의 경계 값들을 시계 방향으로 한 칸씩 shift 하는 함수
def shift_all(r1, c1, r2, c2):
    global grid

    tmp = grid[r1][c2]

    for i in range(c2, c1, -1): # 직사각형 윗 변 한칸씩 오른쪽으로 shift
        grid[r1][i] = grid[r1][i - 1]
    
    for i in range(r1, r2): # 직사각형 왼쪽 변 한칸씩 위로 shift 
        grid[i][c1] = grid[i + 1][c1]
    
    for i in range(c1, c2): # 직사각형 밑 변 한칸씩 왼쪽으로 shift
        grid[r2][i] = grid[r2][i + 1]
    
    for i in range(r2, r1, -1): # 직사각형 오른쪽 변 한칸씩 밑으로 shift
        grid[i][c2] = grid[i - 1][c2]
    
    # tmp으로 저장한 grid[r1][c2] 위치의 값을 한 행 아래 칸으로 shift
    grid[r1 + 1][c2] = tmp


# 직사각형 영역 내 각 숫자들의 값을
# 현재 칸에 적힌 숫자 + 인접한 칸의 숫자들의 평균 값으로 업데이트하는 함수
def update_all(r1, c1, r2, c2):
    global grid
    
    grid2 = [
        [0 for _ in range(m + 1)]
        for _ in range(n + 1)
    ]

    # grid의 각 칸에 위치한 숫자들을 grid2에 복사
    for i in range(n + 1):
        for j in range(m + 1):
            grid2[i][j] = grid[i][j]
    
    # 상하좌우 인접한 칸 조회하기 위한 dx dy
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 직사각형의 각 칸의 인접한 칸에 위치한 숫자들과의 평균값을 구하고
    # 이를 해당 칸의 숫자로 설정
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            sum_of_nums = grid2[i][j]
            cnt = 1
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if in_range(nx, ny):
                    sum_of_nums += grid2[nx][ny]
                    cnt += 1
            
            grid[i][j] = sum_of_nums // cnt


def simulate(r1, c1, r2, c2):
    # 1. 직사각형 영역 경계의 숫자들을 시계 방향으로 한 칸씩 shift
    shift_all(r1, c1, r2, c2)

    # 2. 직사각형 영역에 있는 값들을 인접한 원소들과의 평균 값으로 동시에 업데이트
    update_all(r1, c1, r2, c2)

# q번의 바람의 정보를 가지고 건물의 상태 시뮬레이션 진행
for r1, c1, r2, c2 in winds:
    simulate(r1, c1, r2, c2)


# 출력
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(grid[i][j], end=' ')
    print()