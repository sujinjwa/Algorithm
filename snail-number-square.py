n, m = tuple(map(int, input().split())) # n : 행의 크기, m : 열의 크기

# visited : n * m 크기 격자의 각 칸에 방문 여부 표시하는 2차원 배열
visited = [
    [False] * m
    for _ in range(n)
]

# grid : 달팽이 모양으로 숫자 증가시키며 채우기 위한 n * m 2차원 배열
grid = [
    [0] * m
    for _ in range(n)
]

r, c = 0, 0 # 시작 위치
cur_dir = 1 # 시작 방향

#     위  오 아  왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

grid[r][c] = 1
visited[r][c] = True

for i in range(2, n * m + 1):
        # 벽 또는 이미 방문한 칸 만난 경우 오른쪽으로 방향 전환
        if not in_range(r + dxs[cur_dir], c + dys[cur_dir]) or visited[r + dxs[cur_dir]][c + dys[cur_dir]]:
            cur_dir = (cur_dir + 1) % 4

        # cur_dir 방향으로 한 칸 전진
        r, c = r + dxs[cur_dir], c + dys[cur_dir]
        visited[r][c] = True
        grid[r][c] = i

# 숫자 1부터 증가하여 달팽이 모양으로 채워진 n*m 2차원 배열 출력
for row in grid:
    for number in row:
        print(number, end=' ')
    print()