# n : 행의 크기, m : 열의 크기
n, m = tuple(map(int, input().split()))

# n * m 크기의 격자 내에
# 뱀이 없는 경우 1, 뱀이 있는 경우 0 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# visited: n * m 크기의 격자 grid의 각 칸에
# 방문 여부 확인하기 위한 배열
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 칸 (x, y)로 이동할 수 있는지 확인
def can_go(x, y):
    # 격자 벗어나는지 확인
    if not in_range(x, y):
        return False
    
    # 이미 방문했는지 또는 뱀이 배치되어 있는지 확인
    if visited[x][y] or not grid[x][y]:
        return False
    
    return True

# 칸 (x, y)에서 이동 가능한 다른 칸 (new_x, new_y) 탐색
def dfs(x, y):
    # 반드시 아래와 오른쪽 2방향 중에서만 이동 가능하며
    # 아래 방향이 더 우선순위
    dxs = [1, 0]
    dys = [0, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

# 칸(0, 0)에서 dfs 탐색 시작
dfs(0, 0)

# 뱀에게 물리지 않고 탈출할 수 있으면 1 없으면 0 출력
print(1 if visited[n - 1][m - 1] else 0)