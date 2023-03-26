from collections import deque
import sys

INT_MAX = sys.maxsize

# n : 격자의 크기, m : 사람의 수
n, m = tuple(map(int, input().split()))

# 출발 시간이 되기 전까지 사람들은 격자 밖에 나와있다!
# poeple : m명의 모든 사람들의 위치 (-1, -1)로 초기화
people = [(-1, -1)] * m

# n * n 크기의 격자 입력 받기
# 0 : 빈 공간, 1 : 베이스 캠프
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# m개의 편의점 위치 입력 받기
stores = []
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    stores.append((r - 1, c - 1))

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# step : 최단 거리 구하기 위한 2차원 배열
step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

curr_t = 0 # curr_t : 현재 분
arr = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 2

# 우선순위가 ↑, ←, →, ↓
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# 편의점 위치인 stores에서 최단 거리에 위치한 베이스 캠프 위치 찾기
def bfs(stores):
    # visited와 step 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    r, c = stores
    visited[r][c] = True
    arr.append((r, c))
    
    while arr:
        x, y = arr.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                step[new_x][new_y] = step[x][y] + 1
                arr.append((new_x, new_y))

def simulation():
    # 1. 격자에 있는 사람들이 본인이 가고 싶은 편의점으로 1칸 움직인다
    for i in range(m):
        # 아직 격자 밖에 있거나 이미 편의점에 도착한 사람이면 continue
        if people[i] == (-1, -1) or people[i] == stores[i]:
            continue
        
        # 본인이 가고 싶은 편의점 찾고,
        bfs(stores[i])

        # 해당 편의점으로 갈 때 상좌우하 우선순위로
        # step값이 가장 작은 곳으로 한 칸 이동
        x, y = people[i]
        min_dis = INT_MAX
        min_pos = ()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y) and visited[new_x][new_y] and step[new_x][new_y] < min_dis:
                min_dis = step[new_x][new_y]
                min_pos = (new_x, new_y)
        
        # 한 칸 이동
        people[i] = min_pos
    
    # 2. 편의점 도착한 경우 
    # 다른 사람들은 해당 편의점이 있는 칸을 지날 수 없게 된다
    for i in range(m):
        if people[i] == stores[i]:
            r, c = people[i]
            grid[r][c] = 2
    
    # 3. curr_t <= m 이면,
    # 해당 사람(people[curr_t])이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프 찾고
    # 해당 베이스 캠프에 사람을 위치시킨다
    if curr_t <= m:
        bfs(stores[curr_t - 1])

        # 최단 거리에 위치한 베이스 캠프 구하기
        min_dis = INT_MAX
        min_pos = ()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] and step[i][j] < min_dis:
                    min_dis = step[i][j]
                    min_pos = (i, j)

        people[curr_t - 1] = min_pos

        # 사람들은 해당 베이스 캠프가 있는 칸을 지나갈 수 없다
        r, c = min_pos
        grid[r][c] = 2

# 모든 사람이 편의점에 도착했는지 확인
def end():
    for i in range(m):
        if people[i] != stores[i]:
            return False
    
    return True

# 1분에 한 번씩 simulation 진행
while True:
    curr_t += 1
    simulation()

    if end():
        break

print(curr_t)