from collections import deque # queue 아닌 deque를 사용해야 함!

# n : 행의 크기, m : 열의 크기
n, m = tuple(map(int, input().split()))

# n * m 크기의 이차원 영역의 각 칸에
# 뱀이 없는 경우 1, 있는 경우 0 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# visited : 각 칸이 이미 방문한 칸인지 확인하기 위한 n * m 크기의 이차원 배열
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

q = deque() # deque 선언

# 상하좌우로의 이동을 위한 연산
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    # 격자를 벗어나는지 확인
    if not in_range(x, y):
        return False
    
    # 이미 방문한 위치인지 혹은 해당 위치에 뱀이 배치되어 있는지 확인
    if visited[x][y] or not grid[x][y]:
        return False
    
    return True

def bfs():
    # q가 빈 deque가 될 때까지 반복
    while q:
        # (curr_x, curr_ y) : 가장 최근 이동하여 도착한 위치
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            # (new_x, new_y)칸으로 이동할 수 있다면
            # 해당 위치로 이동
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

# (0, 0)칸에 방문 여부 True로 설정
# q에 (0, 0)칸 추가한 뒤 bfs 탐색 시작
visited[0][0] = True
q.append((0, 0))
bfs()

# 우측 하단까지 탈출 가능한 경로 있으면 1, 없으면 0 출력
print(1 if visited[n-1][m-1] else 0)