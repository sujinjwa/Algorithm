# n : 격자 크기, m : 주사위 굴릴 횟수, r, c : 초기 주사위 위치
n, m, r, c = tuple(map(int, input().split()))

# dirs: m개의 방향 정보
direcs = tuple(input().split())

r, c = r - 1, c - 1

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 위, 오, 아래, 왼 : (index가) 0, 1, 2, 3
curr_dir = 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# 현재 윗면, 앞면, 오른쪽면에 위치한 각 숫자가 1, 2, 3
up, front, right = 1, 2, 3

# 1. 왼쪽으로 돌면 up, front, right = right, front, 7 - up
# curr_num = 7 - right

# 2. 오른쪽으로 돌면 up, front, right = 7 - right, front, up
# curr_num = right

# 3. 위로 돌면 up, front, right = front, 7 - up, right
# curr_num = 7 - front

# 4. 아래로 돌면 up, front, right = 7 - front, up, right
# curr_num = front

# 현재 격자 위치에 찍힐 숫자 : = 7 - up = 6
curr_num = 7 - up
grid[r][c] = curr_num

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for direc in direcs:
    # 1. 이동할 방향 구하기
    # direc: 현재 이동할 방향
    if direc == 'U':
        curr_dir = 0
    elif direc == 'R':
        curr_dir = 1
    elif direc =='D':
        curr_dir = 2
    else:
        curr_dir = 3
    
    # 2. 이동할 방향으로 한칸 이동한 위치(nx, ny)로 이동 가능하면 이동 후
    # 이동된 위치에 바닥면에 위치한 숫자 찍어주기
    nx, ny = r + dxs[curr_dir], c + dys[curr_dir]

    if not in_range(nx, ny):
        continue

    if curr_dir == 0:
        curr_num = 7 - front
        up, front, right = front, 7 - up, right
    
    elif curr_dir == 1:
        curr_num = right
        up, front, right = 7 - right, front, up
    
    elif curr_dir == 2:
        curr_num = front
        up, front, right = 7 - front, up, right
    
    else:
        curr_num = 7 - right
        up, front, right = right, front, 7 - up
    
    r, c = nx, ny
    grid[r][c] = curr_num


# 격자판에 써잇는 숫자들의 합 구하기
ans = 0
for row in grid:
    for elem in row:
        ans += elem

print(ans)