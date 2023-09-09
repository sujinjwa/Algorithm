from collections import deque
MIN_NUM = 0

# n : 격자의 크기, k : 시작점의 수, m : 치워야 할 돌의 개수
n, k, m = tuple(map(int, input().split()))

# grid : n * n 크기의 격자, 0: 이동할 수 있는 곳, 1 : 돌이 있어서 이동하지 못하는 곳
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

s_points = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

chosen_rocks = []
q = deque()
max_cnt = MIN_NUM

# 주어진 모든 돌의 위치 구하기
rocks = []
for x in range(n):
    for y in range(n):
        if grid[x][y]: rocks.append((x, y))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def has_rock(x, y):
    # 치워진 돌 array에 포함되어 있지 않은 위치만 돌이 있다고 취급
    return grid[x][y] and not (x, y) in chosen_rocks

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and not has_rock(x, y)

def bfs():
    while q:
        curr_x, curr_y = q.popleft()

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            next_x, next_y = curr_x + dx, curr_y + dy

            if can_go(next_x, next_y):
                q.append((next_x, next_y))
                visited[next_x][next_y] = True

def find_max_pos():
    global s_points, max_cnt, visited
    
    # 모든 시작점 deque에 넣어두기
    for x, y in s_points:
        q.append((x - 1, y - 1))
        visited[x - 1][y - 1] = True
    
    # BFS 탐색 시작
    bfs()

    # 방문 가능한 칸의 수 구하기
    cnt = 0
    for row in visited:
        for elem in row:
            if elem:
                cnt += 1

    max_cnt = max(max_cnt, cnt)

    # visited 초기화
    for x in range(n):
        for y in range(n):
            visited[x][y] = False
    
# 돌들 중 m개의 돌만 선택되는 모든 경우의 수 조합으로 구하기
def choose(curr_num, cnt):
    if curr_num == m:
        find_max_pos()
        return
    
    for i, (x, y) in enumerate(rocks):
        if i + 1 > cnt:
            chosen_rocks.append((x, y))
            choose(curr_num + 1, i + 1)
            chosen_rocks.pop()

choose(0, 0)

print(max_cnt)