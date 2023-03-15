from collections import deque

# n : 행의 크기, m : 열의 크기
n, m = tuple(map(int, input().split()))

# 뱀이 없는 경우 1, 있는 경우 0
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

arr = deque()

#     상 하 좌 우
dxs = [-1, 1, 0, 0]
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
    if not arr:
        return
    
    x, y = arr.popleft()
    for dx, dy in zip(dxs, dys):
        curr_x, curr_y = x + dx, y + dy

        if can_go(curr_x, curr_y):
            visited[curr_x][curr_y] = True
            arr.append((curr_x, curr_y))
            bfs()

visited[0][0] = True
arr.append((0, 0))
bfs()

print(1 if visited[n - 1][m - 1] else 0)