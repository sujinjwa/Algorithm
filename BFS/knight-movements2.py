from collections import deque

# n : 격자의 크기
n = int(input())

# (r1, c1) : 나이트의 시작 위치 / (r2, c2) : 나이트의 끝 위치
r1, c1, r2, c2 = list(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

arr = deque()

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# steps[i][j] : 시작점(r1, c1)로부터 (i, j) 지점에 도달하기 위한 최단거리 기록하는 1차원 배열
steps = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1, 1, 2, 2, 1, -1, -2]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

# r1, c1에서 r2, c2까지 최단 거리로 갈 때의 이동 횟수 구하기
def bfs():
    while arr:
        x, y = arr.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = dx + x, dy + y

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                steps[new_x][new_y] = steps[x][y] + 1 # 최단 거리는 이전 최단거리에서 +1
                arr.append((new_x, new_y))

visited[r1][c1] = True
arr.append((r1, c1))
bfs()

# 출력 (단, (r2, c2) 지점에 도착하지 못하는 경우라면 -1 출력)
print(steps[r2][c2] if visited[r2][c2] else -1)