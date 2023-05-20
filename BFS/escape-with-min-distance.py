from collections import deque

n, m = list(map(int, input().split())) # n : 격자의 행 크기, m : 격자의 열 크기

# n * m 크기만큼 숫자 입력 받기
# 이때 입력 받는 숫자가 1이면 뱀이 없는 칸, 0이면 뱀이 있는 칸
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# visited : 각 칸에 방문했는지 확인하기 위한 grid 크기의 2차원 배열
visited = [
    [False] * m
    for _ in range(n)
]

# distance : 시작점으로부터 각 칸의 최단 거리 구하기 위한 grid 크기의 2차원 배열
distance = [
    [0] * m
    for _ in range(n)
]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_move(x, y):
    return in_range(x, y) and grid[x][y] and not visited[x][y]

# BFS 탐색하며 근접한 칸 중 이동 가능한 칸으로 이동하는 함수
def bfs():
    while q:
        x, y = q.popleft() # x, y : 가장 최근까지 이동한 위치

        dxs = [-1, 0, 1, 0]
        dys = [0, 1, 0, -1]

        # 현재 칸(x, y)과 인접한 칸들 중 이동 가능한 칸 찾기
        for dx, dy in zip(dxs, dys):
            next_x = x + dx
            next_y = y + dy

            # 이동 가능한 경우
            # 최단 거리와 방문 여부 각각 distance와 visited에 표시
            if can_move(next_x, next_y):
                distance[next_x][next_y] = distance[x][y] + 1
                visited[next_x][next_y] = True
                q.append((next_x, next_y))

# (0, 0) 칸에서 시작하여 vfs 탐색 시작
q.append((0, 0))
bfs()

# 좌측 상단엥서 우측 하단까지의 최단 거리 출력
# 우측 하단까지 이동 불가능한 경우 -1 출력
answer = distance[n - 1][m - 1] if distance[n - 1][m - 1] else -1
print(answer)