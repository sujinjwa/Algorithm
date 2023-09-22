from collections import deque
import sys

MAX_INT = sys.maxsize

# n : 격자 크기, k : 없애야 할 벽의 개수
n, k = tuple(map(int, input().split()))

# grid: n * n 크기의 격자 입력받기
# 0: 이동할 수 있는 칸, 1: 벽이 있어 이동할 수 없는 칸

real_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        grid[i][j] = real_grid[i][j]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

steps = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# r1, c1 : 시작점 위치, r2, c2 : 도착점 위치
r1, c1 = tuple(map(int, input().split()))
r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

# 1. 백트래킹으로 k개의 벽 없애는 경우의 수 구하기
# 2. bfs 최단거리 탐색으로 시작점 -> 도착점 이동 시간 구하기

walls = []
chosen_walls = []
q = deque()
ans = MAX_INT

for i in range(n):
    for j in range(n):
        if grid[i][j]: # 벽이라면
            walls.append((i, j))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and not grid[x][y]

def push(x, y, new_steps):
    visited[x][y] = True
    steps[x][y] = new_steps
    q.append((x, y))

def bfs():
    global ans

    # 1. chosen_walls 들의 위치를 1 -> 0 으로 변경 (이동할 수 있는 칸으로 변경)
    for i, j in chosen_walls:
        grid[i][j] = 0
    
    visited[r1][c1] = True
    q.append((r1, c1))
    
    # 2. BFS 탐색으로 각 칸까지 이동하는 데 걸리는 시간 steps에 남기기
    while q:
        curr_x, curr_y = q.popleft()

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        
        for dx, dy in zip(dxs, dys):
            next_x, next_y = curr_x + dx, curr_y + dy

            if can_go(next_x, next_y):
                push(next_x, next_y, steps[curr_x][curr_y] + 1)

    # 3. 도착점 (r2, c2)에 방문했는지 확인 후 도착하는 데 걸린 최소 시간 갱신
    if visited[r2][c2]:
        ans = min(ans, steps[r2][c2])

# refresh: visited와 grid 초기화시키기
def refresh():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = real_grid[i][j]

# k개의 벽 없애는 모든 경우 구하기
def choose(n):
    # n번째 벽 고르기
    if n > k:
        bfs() # 고른 벽 개수가 k개인 경우 chosen_walls 가지고 bfs 탐색 시작
        refresh() # 초기화
        return
        
    for i in range(len(walls)):
        if walls[i] in chosen_walls: # 이미 고른 벽은 제외
            continue

        chosen_walls.append(walls[i])
        choose(n + 1)
        chosen_walls.pop()

choose(1)

# 도착점까지 도달하는 데 걸리는 최소 시간 출력
if ans == MAX_INT:
    ans = -1

print(ans)