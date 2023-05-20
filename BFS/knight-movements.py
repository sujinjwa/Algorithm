from collections import deque

n = int(input()) # n : 격자의 크기

# (r1, c1) : 시작 위치, (r2, c2) : 끝 위치
r1, c1, r2, c2 = list(map(int, input().split()))

q = deque()

# distance : 시작점으로부터 각 칸으로 가는 데 걸리는 
# 최소 이동 횟수 기록하기 위한 2차원 배열
distance = [
    [0] * n
    for _ in range(n)
]

# visitied : 각 칸에 방문했는지 여부 확인하기 위한 2차원 배열
visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_move(x, y):
    return in_range(x, y) and not visited[x][y]

dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs():
    while q: # q가 빈 값이 될 때까지 반복
        x, y = q.popleft() # q에서 가장 앞의 위치를 현재 위치로 설정
        
        # 현재 위치(x, y)에서 이동할 수 있는 칸 조회
        for dx, dy in zip(dxs, dys):
            next_x = x + dx
            next_y = y + dy

            # 이동할 수 있는 경우
            # 이동 횟수 갱신 및 방문 여부 표시
            if can_move(next_x, next_y):
                distance[next_x][next_y] = distance[x][y] + 1
                visited[next_x][next_y] = True
                q.append((next_x, next_y))

# 시작점(r1, c1)에서 한 번만 이동하여 도착할 수 있는 8개의 칸들을 q에 넣기
for dx, dy in zip(dxs, dys):
    next_x = r1 + dx - 1
    next_y = c1 + dy - 1

    # 조회한 칸들 중 격자 내에 위치한 경우에만 이동
    if in_range(next_x, next_y):
        distance[next_x][next_y] = 1
        visited[next_x][next_y] = True
        q.append((next_x, next_y))

# BFS 탐색 시작
bfs()

# 최소 이동 횟수 출력
# 만약 이동이 불가능한 경우 -1 출력
answer = distance[r2 - 1][c2 - 1] if distance[r2 - 1][c2 - 1] or (r2 == 1 and c2 == 1) else -1
print(answer)
