n, r, c = list(map(int, input().split())) # n : 격자의 크기 / r, c : 시작 위치

r, c = r - 1, c - 1 # 입력받은 행,열을 배열 index 기준으로 -1

# n * n 크기의 격자 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

#      상  하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 위치 (x, y) 가 격자를 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 상하좌우 순서를 우선순위로, 인접한 위치에 적힌 최대값 찾아 r, c 값으로 갱신
def find_max():
    global r, c

    print(grid[r][c], end=' ') # 방문한 격자의 숫자 출력

    for dx, dy in zip(dxs, dys):
        cur_x, cur_y = r + dx, c + dy # r, c와 인접한 위치

        # 인접한 위치가 격자를 벗어나지 않는지, 해당 위치의 숫자보다 더 큰 값이라면
        if in_range(cur_x, cur_y) and grid[cur_x][cur_y] > grid[r][c]:
            r, c = cur_x, cur_y
            # print(grid[cur_x][cur_y], end=' ')
            find_max()

find_max()