from collections import deque

# n : 격자의 크기, h : 사람의 수, m : 비를 피할 수 있는 공간의 수
n, h, m = list(map(int, input().split()))

# n * n 크기 격자의 각 칸에 대한 입력 받기
# 0인 경우 이동할 수 있는 곳, 1인 경우 이동할 수 없는 곳,
# 2인 경우 사람이 서 있는 곳, 3인 경우 비를 피할 수 있는 곳임을 의미
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# visitied : 각 칸에 방문한 적 있는지 여부 확인하기 위한 n*n 크기의 2차원 배열
visited = [
    [False] * n
    for _ in range(n)
]

# distance : 각 칸에서 비를 피할 수 있는 곳까지의 최소 거리 기록하기 위한 n*n 크기의 2차원 배열
distance = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < n

def can_move(x, y):
  return in_range(x, y) and grid[x][y] != 1 and not visited[x][y]

# 이동 가능한 곳인 (x, y) 를 q에 추가 및 방문 여부 기록하고
# 그동안의 최소 이동 시간 기록
def push(x, y, new_step):
  q.append((x, y))
  visited[x][y] = True
  distance[x][y] = new_step

q = deque()

# q가 빈 큐가 될 때까지 (x, y) 위치에서 인접한 칸들 중 이동 가능한 곳 조회
def bfs():
  while q:
    x, y = q.popleft()

    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
      next_x = x + dx
      next_y = y + dy

      if can_move(next_x, next_y):
        push(next_x, next_y, distance[x][y] + 1)

# 비를 피할 수 있는 모든 곳을 q에 추가
for x in range(n):
  for y in range(n):
    if grid[x][y] == 3:
      push(x, y, 0)

# 비를 피할 수 있는 공간들을 시작점으로 하는 BFS 진행
bfs()

# 각 사람들이 비를 피할 수 있는 공간까지 가는 데 걸리는 최소 시간 출력
for i in range(n):
  for j in range(n):
    if grid[i][j] != 2: # 사람이 서 있는 곳이 아닌 경우
      print(0, end=' ')
    else:
      if not visited[i][j]: # 비를 피할 수 있는 공간에서 시작하여 방문하지 못한 곳인 경우
        print(-1, end=' ')
      else: # 비를 피할 수 있는 공간으로 이동 가능한 사람인 경우 최소 이동 시간 출력
        print(distance[i][j], end=' ')
  print()