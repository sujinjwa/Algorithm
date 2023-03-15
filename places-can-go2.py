from collections import deque

# n : 격자의 크기, k : 시작점의 수
n, k = tuple(map(int, input().split()))

# n * n 크기의 격자 입력 받기
# 0 : 이동할 수 있는 칸, 1 : 이동할 수 없는 칸
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# k개의 시작점의 위치 starts 배열에 입력 받기
starts = []
for _ in range(k):
    r, c = tuple(map(int, input().split()))
    starts.append((r - 1, c - 1))

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

#     상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y]:
        return False

    return True

arr = deque()

def bfs():
    while arr:
        x, y = arr.popleft()
        for dx, dy in zip(dxs, dys):
            curr_x, curr_y = x + dx, y + dy

            if can_go(curr_x, curr_y):
                visited[curr_x][curr_y] = True
                arr.append((curr_x, curr_y))

# k개의 시작점 (x, y)로부터 상하좌우 인접한 곳으로만 이동하여
# 도달 가능한 칸의 수 구하기
for x, y in starts:
    arr.append((x, y))
    visited[x][y] = True
    bfs()

# 총 도달 가능한 칸의 수 구하여 출력
cnt = 0
for row in visited:
    for elem in row:
        if elem:
            cnt += 1

print(cnt)