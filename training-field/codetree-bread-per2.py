from collections import deque

# n : 격자 크기, m : buyer 수
n, m = map(int, input().split())

buyers = [
    (-1, -1) for _ in range(m)
]

# 0은 빈 공간, 1은 베이스캠프
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

stores = []
for _ in range(m):
    x, y = map(int, input().split())
    stores.append((x - 1, y - 1))

camps = [
    (-1, -1) for _ in range(m)
]

visited = [
    [False] * n
    for _ in range(n)
]

q = deque()

trace = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y): # 다른 사람이 위치한 편의점이거나 방문했던 베캠이 아닌 경우
    return grid[x][y] != -1

#     상 왼 오 하
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# 각 편의점으로부터 이동할 때 걸리는 최단 시간을 각 칸에 표시(trace 배열)
def bfs():
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue
            
            if not can_go(nx, ny):
                continue
            
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            trace[nx][ny] = trace[x][y] + 1
            q.append((nx, ny))


def simulate(time):
    # 1. 격자에 있는 사람들 편의점 방향을 향해 1칸씩 움직임
    # 격자에 있는지 확인
    for i1 in range(m):
        x, y = buyers[i1]
        if x == -1 and y == -1: # 격자에 없는 경우 continue
            continue

        s1, s2 = stores[i1]
        if x == s1 and y == s2: # 이미 편의점에 도착했으면 이동 X
            continue

        # trace와 visited 초기화
        for i2 in range(n):
            for j2 in range(n):
                trace[i2][j2] = 0
                visited[i2][j2] = False

        # 여기 시점에서 가고 싶은 편의점에서 시작하는 bfs 탐색을 다시 해줘서
        # trace를 그려줘야 최단 거리로 편의점을 갈 수 있다
        s1, s2 = stores[i1]
        visited[s1][s2] = True
        q.append((s1, s2))
        bfs()
        
        # 인접한 4칸 중 trace값이 가장 작은 곳으로 가야 최단 거리이다
        min_trace = n * n
        min_x, min_y = -1, -1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue
        
            if not can_go(nx, ny):
                continue

            # 최단 거리로 해당 편의점 향해 움직임
            if trace[nx][ny] < min_trace:
                min_trace = trace[nx][ny]
                min_x, min_y = nx, ny
        
        # 편의점 방향 향해 1칸 움직임
        buyers[i1] = (min_x, min_y)

    # 2. 편의점 도착한 사람들이 있는 경우 해당 칸을 지나지 못하도록 설정
    for i2 in range(m):
        s1, s2 = stores[i2]
        b1, b2 = buyers[i2]
        if s1 == b1 and s2 == b2: # 편의점에 도착한 사람
            grid[s1][s2] = -1 # 지나갈 수 없음

    # 3. time <= m일 때 time번 사람이 베이스 캠프에 위치하도록
    # 이때 배정된 베이스캠프는 가고 싶은 편의점과 가장 가까이에 있는 캠프!
    if time <= m - 1: # 아직 배정된 베캠이 없는 time번째 사람 있는 경우
        # trace와 visited 초기화
        for i in range(n):
            for j in range(n):
                trace[i][j] = 0
                visited[i][j] = False
        
        # 3-1. sotres[time]과 가장 가까운 베캠 찾기
        x, y = stores[time]
        visited[x][y] = True
        q.append((x, y))
        bfs()

        print(trace)
    
        # trace 하나씩 보면서 가장 최소 값을 가지는 베캠(grid[x][y] == 1) 위치 찾기
        min_trace = n * n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and trace[i][j] != 0: # trace[i][j] == 0인 곳은 갈 수 없는 곳! 편의점과 베캠이 겹쳐져 주어지진 않으니까
                    if trace[i][j] < min_trace:
                        min_trace = trace[i][j]
                        camps[time] = (i, j)
        
        # 해당 캠프 위치(camps[time])에 buyers[time] 위치시키기
        buyers[time] = camps[time]
        print(buyers)
        
        # 다른 사람이 해당 베캠에 못 지나가도록 설정
        x, y = camps[time]
        grid[x][y] = -1


def end():
    # 모든 사람들이 원하는 편의점에 도착한 경우
    for i in range(m):
        s1, s2 = stores[i]
        b1, b2 = buyers[i]

        if s1 != b1 or s2 != b2:
            print(s1, s2, b1, b2)
            return False
    
    return True


time = -1 # 모든 사람이 편의점에 도착하는 시간
while True:
    print(grid)
    print(buyers)

    if end(): # 모든 사람이 편의점에 도착한다면
        break

    time += 1
    print(time)
    simulate(time)

print(time + 1)