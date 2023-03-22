from collections import deque

# n : 격자의 크기, k : 시작점의 개수, m : 치워야 할 돌의 개수
n, k, m = list(map(int, input().split()))

# n * n 크기의 격자 내 숫자 입력 받기
# 0이면 이동할 수 있는 칸, 1이면 돌이 있어 이동할 수 없는 칸임을 의미
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid2 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# starts_pos : 시작점 모아놓은 1차원 배열
starts_pos = []
for _ in range(k):
    r, c = tuple(map(int, input().split()))
    starts_pos.append((r - 1, c - 1))

# 돌이 있는 칸 모아 놓은 배열 만들기
rocks_pos = []
for x in range(n):
    for y in range(n):
        if grid[x][y]:
            rocks_pos.append((x, y))

# removed_rocks : 치우기로 결정된 m개의 돌 모아 놓기 위한 1차원 배열
removed_rocks = []
q = deque()

# visited : n * n 격자 내 방문 여부 확인하기 위한 2차원 배열
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# max_visit_count : 상하좌우 인접한 곳으로 이동하여 도달 가능한 칸의 최대 개수 구하기 위한 변수
max_visit_count = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not grid2[x][y] and not visited[x][y]

# 도달 가능한 칸의 개수 구하는 함수
def find_visit_count():
    cnt = 0
    for row in visited:
        for elem in row:
            if elem:
                cnt += 1
    
    return cnt

def bfs():
    global max_visit_count, grid2, visited

    # 격자 초기화
    for x in range(n):
        for y in range(n):
            grid2[x][y] = grid[x][y]

    # visited 초기화
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    # 치우기로 선택한 돌들만 치우기
    for x, y in removed_rocks:
        grid2[x][y] = 0
    
    # 모든 시작점을 q에 추가
    for x, y in starts_pos:
        visited[x][y] = True
        q.append((x, y))
    
    while q:
        x, y = q.popleft()

        dxs = [-1, 1, 0, 0]
        dys = [0, 0, -1, 1]
        
        # 상하좌우 인접한 곳들 중 도달 가능한 칸 찾기
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

    # max_visit_count값 업데이트
    max_visit_count = max(max_visit_count, find_visit_count())

# (BackTracking - n개 중 m개 고르기)
# rocks_pos에서 m개의 제거해야 할 돌을 선택하여
# removed_rocks에 추가하는 모든 조합의 경우의 수 구하기
def choose(cnt, pre_index):
    if cnt == m:
        bfs()
        return
    
    for i in range(pre_index + 1, len(rocks_pos)):
        removed_rocks.append(rocks_pos[i])
        choose(cnt + 1, i)
        removed_rocks.pop()

choose(0, -1)

# 도달 가능한 칸의 최대 개수 출력
print(max_visit_count)