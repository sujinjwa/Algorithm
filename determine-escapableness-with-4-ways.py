from collections import deque

n, m = list(map(int, input().split())) # n * m : 이차원 grid의 넓이 & 높이

# grid : 각 칸에 뱀이 있는지 여부 입력 받은 이차원 배열
# 각 칸에 뱀이 없는 경우 1, 있는 경우 0 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# visited : 각 칸에 방문했는지 여부 확인하기 위한 이차원 배열
visited = [
    [0] * m
    for _ in range(n)
]

dq = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    # 해당 칸이 범위를 벗어난 경우
    if not in_range(x, y):
        return False
    
    # 해당 칸에 이미 방문했거나 뱀이 있는 경우
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

def push(x, y):
    dq.append((x, y))

def bfs():
    while dq: # dq에 값이 없을 때까지 이동 가능한 칸 찾는 과정 반복
        x, y = dq.popleft() # dq에서 맨 앞에 위치한 값 pop 하고, 현재 위치(x, y)로 설정

        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        
        # 현재 위치(x, y)와 인접한 칸 중 이동 가능한 칸 찾기
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy

            if can_go(next_x, next_y): # 이동 가능한지 확인
                push(next_x, next_y)
                visited[next_x][next_y] = True # 방문한 곳임을 표시

# 첫 시작 위치(0, 0)을 dq에 넣고 방문했음을 표시한 이후
# BFS 탐색 시작
push(0, 0)
visited[0][0] = True
bfs()

# 탈출 가능한 경로 있는지 여부 출력
if(visited[n-1][m-1] == 1):
    print(1)
else:
    print(0)