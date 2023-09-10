n = int(input())

grid = [
    list(input())
    for _ in range(n)
]

k = int(input()) # 레이저 쏘는 위치

# 시작점과 레이저 방향 초기화
r, c = -1, -1
curr_dir = 0

# 시작 위치(r, c) 구하기
# 1. k = 1 ~ n => grid[0][k - 1], curr_dir = 0
# 2. k = n + 1 ~ 2n => grid[k - n - 1][n - 1]. curr_dir = 3
# 3. k = 2n + 1 ~ 3n => grid[n - 1][n - (k - 2n)]. curr_dir = 1
# 4. k = 3n + 1 ~ 4n => grid[n - (k - 2n)][0]. curr_dir = 2

if k >= 1 and k <= n:
    r, c = 0, k - 1
    curr_dir = 0

elif k >= n + 1 and k <= 2 * n:
    r, c = k - n - 1, n - 1
    curr_dir = 3

elif k >= 2 * n + 1 and k <= 3 * n:
    r, c = n - 1, n - (k - 2 * n)
    curr_dir = 1

else:
    r, c = n - (k - 3 * n), 0
    curr_dir = 2


# curr_dir = 0, 1, 2, 3 => 하 상 오 왼
# / 이면 : curr_dir = 0 <-> 3, 1 <-> 2
# \\ 이면 : curr_dir = (curr_dir + 2) % 4
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
cnt = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate(curr_x, curr_y):
    global curr_dir, cnt
        
    # 1. 방향 바꾸기
    if grid[curr_x][curr_y] == '/':
        if curr_dir == 0:
            curr_dir = 3
        elif curr_dir == 1:
            curr_dir = 2
        else:
            curr_dir = 3 % curr_dir
    else:
        curr_dir = (curr_dir + 2) % 4
    
    # 2. 레이저 쏴서 이동할 다른 칸 구하기
    nx, ny = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    cnt += 1 # 이동 횟수 + 1
    
    # 3. 격자 밖으로 나간 경우 이동 종료, 아닌 경우 nx, ny를 curr_x, curr_y으로 갱신
    if not in_range(nx, ny):
        return
    else:
        simulate(nx, ny)


simulate(r, c)
print(cnt)