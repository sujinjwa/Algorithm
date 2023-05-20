from collections import deque

n, k = list(map(int, input().split())) # n : 격자의 크기, k : 시작점의 수

# n * n 크기의 격자의 각 칸에 0 또는 1 입력 받기
# 이때, 0이면 이동할 수 있는 곳, 1이면 이동할 수 없는 곳임을 의미
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# k개의 시작점 위치(r, c) 입력 받기
points = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

# 방문 여부 확인하는 함수
visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_move(x, y):
    return in_range(x, y) and grid[x][y] == 0 and visited[x][y] == False # visited가 True인 조건은 제외

def bfs():
    while que: # que 안에 값이 없을 때까지 반복
        x, y = que.popleft()

        dxs = [-1, 1, 0, 0]
        dys = [0, 0, -1, 1]

        # 각 위치(x, y)의 상하좌우 인접한 곳으로 이동 가능 여부 확인
        for dx, dy in zip(dxs, dys):
            next_x = x + dx
            next_y = y + dy

            # 이동 가능한 경우 방문 가능 표시 및 queue에 넣어주기
            if can_move(next_x, next_y):
                visited[next_x][next_y] = True
                que.append((next_x, next_y))

# bfs 탐색 전에 시작점을 que에 모두 넣어두기
que = deque()
for x, y in points:
    que.append((x - 1, y - 1))
    visited[x - 1][y - 1] = True

# bfs 탐색 시작
bfs()

# k개의 시작점으로부터 도달 가능한 모든 칸의 수 출력
cnt = 0
for row in visited:
    for elem in row:
        if elem:
            cnt += 1

print(cnt)