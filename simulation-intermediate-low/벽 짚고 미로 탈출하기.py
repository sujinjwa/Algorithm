import sys

# n : 격자의 크기
n = int(input())

curr_x, curr_y = tuple(map(int, input().split()))
curr_x, curr_y = curr_x - 1, curr_y - 1

grid = [
    list(input())
    for _ in range(n)
]

visited = [
    [
        [False for _ in range(4)] # 바라보는 방향(curr_dir)의 index
        for _ in range(n)
    ]
    for _ in range(n)
]

# 첫 위치는 무조건 우측 방향
curr_dir = 0

# 오, 아래, 왼, 위
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# (x, y) 칸에 벽이 있는지 없는지 확인
def can_go(x, y):
    return grid[x][y] == '.'

def simulate():
    global t, curr_x, curr_y, curr_dir

    nx, ny = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    if not in_range(nx, ny):
        curr_x, curr_y = nx, ny
        t += 1
        return

    if visited[nx][ny][curr_dir]:
        print(-1)
        sys.exit(0)

    # CASE 1. 바라보는 방향으로 이동 가능하지 않은 경우
    # 반시계 방향으로 90도 만큼 방향 바꾼다
    elif not can_go(nx, ny):
        # 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2
        if visited[nx][ny][curr_dir]:
            print(-1)
            sys.exit(0)

        visited[nx][ny][curr_dir] = True
        curr_dir = (curr_dir + 3) % 4

    # CASE 2. 바라보는 방향으로 이동 가능한 경우
    else:
        # CASE 2-1. (nx, ny)가 격자 밖이면 이동하여 탈출
        if not in_range(nx, ny):
            curr_x, curr_y = nx, ny
            t += 1
            return

        else:
            # (wx, wy) : (nx, ny)에서 현재 방향(curr_dir) 기준 오른쪽 위치
            # curr_dir : 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
            wx, wy = nx + dxs[(curr_dir + 1) % 4], ny + dys[(curr_dir + 1) % 4]

            # CASE 2-2. (wx, wy)에 짚을 벽 있으면 한 칸 앞으로 이동
            if grid[wx][wy] == '#':
                curr_x, curr_y = nx, ny
                visited[curr_x][curr_y][curr_dir] = True
                t += 1

            # CASE 2-3. (wx, wy)에 벽 없으면 한 칸 앞으로 이동 후 
            # 시계 방향으로 90도 방향 틀어 한칸 더 전진
            else: 
                curr_x, curr_y = wx, wy
                visited[nx][ny][curr_dir] = True
                curr_dir = (curr_dir + 1) % 4
                visited[curr_x][curr_y][curr_dir] = True
                t += 2

t = 0
visited[curr_x][curr_y][curr_dir] = True

while in_range(curr_x, curr_y):
    simulate()

print(t)