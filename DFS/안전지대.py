import sys
sys.setrecursionlimit(2500)

# n : 마을의 행 크기, m : 마을의 열 크기
n, m = tuple(map(int, input().split()))

# n * m 크기의 마을 각 칸(집)에 해당되는 숫자(집의 높이) 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# max_k : 안전 영역이 최대일 때의 k 값, max_cnt : 안전 영역의 수
max_k = 1
max_cnt = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y, k):
    return in_range(x, y) and not visited[x][y] and grid[x][y] > k

def dfs(x, y, k):

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)


# 주어진 k의 범위 : 1 <= k <= 100
# 모든 k의 경우 시뮬레이션 진행
for k in range(1, 100 + 1):

    cnt_of_areas = 0
    for x in range(n):
        for y in range(m):
            if can_go(x, y, k):

                # (x, y)을 시작점으로 (x, y)가 포함된 안전 영역 찾기
                cnt_of_areas += 1
                dfs(x, y, k)
    
    # 안전 영역의 수 최대값으로 갱신
    if max_cnt < cnt_of_areas:
        max_k = k
        max_cnt = cnt_of_areas

    # 다음 시뮬레이션 위해 visited 초기화
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


print(max_k, max_cnt)