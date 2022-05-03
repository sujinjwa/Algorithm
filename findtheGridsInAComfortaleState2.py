n, m = tuple(map(int, input().split())) # 격자 크기 n과 색칠하는 횟수 m번 입력 받기

#           북  서 동 남
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

# n * n 격자 생성
grid = [
    [0] * n
    for _ in range(n)
]

# 해당 칸(x, y)이 격자 벗어나는지 확인하는 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 해당 칸(x, y)의 인접한 칸 4개가 격자를 벗어나는지, 색칠되었는지 확인하는 함수
def adjacent_cnt(x, y):
    cnt = 0
    # 위,아래,오른쪽,왼쪽에 위치한 칸 순회하는 반복문
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy # 인접한 칸의 위치 (nx, ny)
        # 인접한 칸(nx, ny)가 격자 벗어나지 않고 색칠되었다면
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    
    return cnt

for _ in range(m):
    x, y = tuple(map(int, input().split())) # m개의 줄에 걸쳐 색칠할 칸의 위치 (x, y) 입력 받기
    # grid 배열의 index는 0부터 시작하므로 입력 받은 행 x와 열 y에서 -1씩 해줘야 함
    x -= 1
    y -= 1
    grid[x][y] = 1 # 색칠하기

    # 해당 칸 탐색
    if adjacent_cnt(x, y) == 3: # return값인 cnt가 3인 경우
        print(1)
    else:
        print(0)