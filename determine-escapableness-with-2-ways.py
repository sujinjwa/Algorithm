n, m = list(map(int, input().split())) # n : 행의 크기, m : 열의 크기

# grid : 전체 경로 입력 받는 2차원 배열
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# visited : 각 칸에 방문했는지 확인하기 위한 2차원 배열
visited = [
    [False] * m
    for _ in range(n)
]

# (x, y) 위치가 경로의 유효한 범위 이내에 있는지 확인
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

# (x, y) 위치로 이동할 수 있는지 확인
def canMove(x, y):
    return in_range(x, y) and visited[x][y] == False and grid[x][y]


def dfs(x, y):
    dxs, dys = [1, 0], [0, 1] # 아래 행, 오른쪽 열의 방향으로 이동할 수 있는 크기
    
    # 아래와 오른쪽 2방향의 인접한 칸으로 순서대로 이동
    for dx, dy in zip(dxs, dys):
        next_x = x + dx
        next_y = y + dy

        # (next_x, next_y) 위치로 이동할 수 있다면
        # 해당 칸에 방문했음을 표시하고 다음 칸으로 이동하여 탐색 계속 진행
        if canMove(next_x, next_y):
            visited[next_x][next_y] = True
            dfs(next_x, next_y)

x, y = 0, 0 # 시작 위치 : (0, 0)
visited[x][y] = True # (0, 0) 위치에 방문했음을 표시
dfs(x, y) # (0, 0) 위치에서 이동할 수 있는 칸 탐색 시작

# 탈출 가능한 경로 찾았는지 여부 확인
def succeeded():
    return visited[n - 1][m - 1]

# 탈출 가능한 경로 여부 판별하여 출력
if succeeded():
    print(1)
else:
    print(0)