from collections import deque

# n : 격자의 크기, k : 반복할 횟수
n, k = tuple(map(int, input().split()))

# grid: 각 칸에 1 이상 100 이하의 숫자 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# (r, c) : 시작 위치
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

# 시작 위치 queue에 추가해주고, 방문했음을 표시
q = deque()
q.append((r, c))
visited[r][c] = True

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# 이동 가능 조건
# 1. 현재 위치한 곳의 숫자보다는 작은 숫자가 위치한 곳으로, 현재 위치에서 시작해 인접한 칸으로 계속해서 이동했을 때 갈 수 있는 모든 곳
# 2. 갈 수 있는 모든 곳에서 가장 최댓값이 위치한 곳
# 2. 최댓값이 위치한 곳이 여러 곳인 경우 행, 열 번호가 가장 작은 곳으로 최종적으로 이동

# min_num : 갈 수 있는 모든 곳 중 최댓값 구하기 위해 0으로 초기화한 변수
min_num = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def is_smaller(x, y):
    global r, c

    return grid[x][y] < grid[r][c]

def can_go(x, y):
    return in_range(x, y) and is_smaller(x, y) and not visited[x][y]

# 시작점(r, c)에서 시작해서 도달할 수 있는 모든 곳 visited 각 칸을 True로 색칠
def bfs():
    global min_num, visited, r, c

    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            next_x, next_y = curr_x + dx, curr_y + dy

            if can_go(next_x, next_y):
                q.append((next_x, next_y))
                visited[next_x][next_y] = True

                # 이동할 수 있는 칸들 중 최댓값(min_num) 구하기
                if grid[next_x][next_y] > min_num:
                    min_num = grid[next_x][next_y]

# 이동할 수 있는 모든 칸(visited값이 True)들 중 
# 최댓값이 위치하면서 행, 열 번호가 가장 작은 곳을 현재 위치(r, c)로 갱신
def find_max_pos():
    global visited, min_num, r, c

    for x in range(n):
        for y in range(n):
            # 해당 칸에 놓인 숫자가 최댓값인 경우
            if visited[x][y] and grid[x][y] == min_num:
                r, c = x, y
                return

def cant_go():
    global visited, r, c

    for x in range(n):
        for y in range(n):
            # 현재 위치(r, c)도 아니면서 이동 가능한 곳이 있으면 이동 가능하다고 판단
            if visited[x][y] and (x != r or y != c):
                return False
    
    return True

# no_pos : 이동 가능한 곳 있는지 여부 나타내는 불리언 변수
no_pos = False

def move():
    global min_num, visited, r, c
    # 1. bfs 탐색으로 (r, c)에서 갈 수 있는 모든 곳 visited True로 색칠하기
    bfs()

    # 더 이상 이동할 수 있는 곳 없으면 시뮬레이션 종료
    if cant_go():
        no_pos = True
        return

    # 2. 이동 가능한 곳들 중 최댓값이면서 행, 열 번호가 작은 곳으로 위치 이동
    find_max_pos()

    # 이동 후 현재 위치(r, c) queue에 추가, 방문했음을 표시
    q.append((r, c))
    visited[r][c] = True
    
    # visited, min_num 초기화
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    min_num = 0

for _ in range(k):
    # 이동 가능한 곳 없으면 시뮬레이션 종료
    if no_pos:
        break

    move()

# k초 후 최종 현재 위치 출력
print(r + 1, c + 1)