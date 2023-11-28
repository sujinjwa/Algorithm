from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    []
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

traces = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 1: 이동할 수 있는 칸, 0: 이동할 수 없는 칸
for i in range(n):
    arr = list(input())
    for j in range(m):
        grid[i].append(int(arr[j]))

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y]

def bfs():
    while q:
        curr_x, curr_y = q.popleft()

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                traces[nx][ny] = traces[curr_x][curr_y] + 1
                q.append((nx, ny))

x, y = 0, 0
visited[x][y] = True
traces[x][y] = 1
q.append((x, y))
bfs()

print(traces[n-1][m-1])