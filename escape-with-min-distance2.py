from collections import deque

# n : 행의 크기, m : 열의 크기
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# step : n*m 크기의 이차원 배열에서 각 칸의 가중치 업데이트 하기 위한 배열
step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque()

dxs = [-1, 1, 0, 0] # 상하좌우
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or not grid[x][y]:
        return False
    
    return True

def bfs():
    while q:
        x, y = q.popleft() # (x, y)칸 : 가장 최근에 위치한 칸
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                q.append((new_x, new_y)) # deque인 q에 이동 가능한 위치(new_x, new_y) 추가
                visited[new_x][new_y] = True # 방문했음을 표기
                step[new_x][new_y] = step[x][y] + 1 # 이전 위치의 가중치에 + 1 해서 가중치 업데이트
    
visited[0][0] = True
q.append((0, 0))
# (0, 0)칸에서 가중치 0을 갖고 bfs 탐색 시작
bfs()

# 좌측 상단에서 우측 하단까지 이동 가능한 경로 중 최단 거리 출력
# 단, 이동 불가능한 경우 -1 출력
print(step[n - 1][m - 1] if step[n - 1][m - 1] else -1)