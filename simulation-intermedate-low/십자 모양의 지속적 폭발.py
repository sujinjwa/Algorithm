from collections import deque

# n : 격자의 크기, m : 폭탄 떠트릴 횟수
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# cols : m번에 걸쳐 폭탄 떠트릴 열의 위치
cols = [int(input()) for _ in range(m)]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# col번째 열에서 가장 위에 위치한 숫자의 위치 구하는 함수
def find_bomb_pos(col):
    for row in range(n):
        if grid[row][col]: # 해당 칸에 숫자가 있다면
            return [row, col]
    
    return [-1, -1]

# r, c 칸에서 시작하여 num만큼 인접한 상하좌우로 폭탄 폭발시키는 함수
def explode(r, c, num):
    global grid

    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 동서남북
    for i in range(num): # i : 0, 1, 2, ..., num - 1
        for dx, dy in zip(dxs, dys):
            nx, ny = r + dx * i, c + dy * i # 동서남북 위치로 i칸 만큼 이동

            if in_range(nx, ny): # 격자 벗어나지 않는 경우 0으로 초기화
                grid[nx][ny] = 0

# 폭탄 터진 후 중력 발생시키는 함수
def go_down():
    global grid

    temp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for col in range(n):
        arr = deque()
        for row in range(n - 1, -1, -1): # 해당 칸에 숫자 있을 때만 arr에 추가
            if grid[row][col]:
                arr.append(grid[row][col])
        
        for row in range(n - 1, -1, -1):
            if len(arr) == 0:
                temp[row][col] = 0
            else:
                temp[row][col] = arr.popleft()
    
    for row in range(n):
        for col in range(n):
            grid[row][col] = temp[row][col]

# m개의 입력 받은 열의 위치에 대해 시뮬레이션 진행
for col in cols:
    col -= 1
    # 1. col에 해당하는 열의 작은 row부터 큰 row까지 순회하면서 가장 먼저 조회되는 숫자의 위치 선택
    # 조회되는 숫자가 해당 열에 하나도 없으면 폭탄 터지지 X, continue 해줌
    [r, c] = find_bomb_pos(col)
    if r == -1 and c == -1:
        continue
    
    # 2. 해당 위치에 있는 숫자 크기만큼 폭탄 폭발
    explode(r, c, grid[r][c])

    # 3. 폭탄 터진 후 중력 작용. (숫자 없는 빈 공간 위에 있던 숫자들이 아래로 떨어짐)
    go_down()


# 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()