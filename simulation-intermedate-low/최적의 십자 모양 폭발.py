from collections import deque

# n : 격자의 크기
n = int(input())

# real_grid : 1~ 100 이하의 숫자들로 구성된 격자판 입력 받기
real_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        grid[i][j] = real_grid[i][j]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# 1. 선택 위치의 숫자만큼 폭탄 터트린다
# 2. 숫자 중간에 빈공간 없도록 중력 발생하여 아래로 숫자들이 떨어진다
# 3. 중력이 작용하고 나서 조건을 만족하는 최대 쌍의 수 출력 (인접한 칸에 같은 숫자 위치)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def bomb(x, y):
    size = grid[x][y] # size 크기만큼의 폭탄 터뜨리기

    grid[x][y] = 0

    if size == 1:
        return

    for s in range(1, size):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx * s, y + dy * s

            if in_range(nx, ny):
                grid[nx][ny] = 0

def fall_down():
    for col in range(n): # 각 열을 조회하며 마지막 행부터 temp에 넣어줌
        temp = deque()
        for row in range(n - 1, -1, -1):
            if grid[row][col]: # 칸에 위치한 숫자가 0이 아닌 경우
                temp.append(grid[row][col])
        
        # 마지막 행부터 temp에 넣어둔 숫자 먼저 넣은 순서대로 하나씩 빼서 설정해주기
        for row in range(n - 1, -1, -1):
            if len(temp) > 0:
                grid[row][col] = temp.popleft()
            else:
                grid[row][col] = 0

def count_pairs():
    chosen_pairs = []

    for i in range(n):
        for j in range(n):
            if not grid[i][j]: # 빈칸인 경우는 제외
                continue

            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if in_range(nx, ny) and grid[i][j] == grid[nx][ny]: # 쌍이라면
                    if (nx, ny, i, j) not in chosen_pairs and (i, j, nx, ny) not in chosen_pairs:
                        chosen_pairs.append((i, j, nx, ny))

    return len(chosen_pairs)

def refresh():
    for i in range(n):
        for j in range(n):
            grid[i][j] = real_grid[i][j]

ans = 0

for i in range(n):
    for j in range(n):

        # 1. 선택 위치의 숫자만큼 폭탄 터트린다
        bomb(i, j)

        # 2. 숫자 중간에 빈공간 없도록 중력 발생하여 아래로 숫자들이 떨어진다
        fall_down()

        # 3. 중력이 작용하고 나서 조건을 만족하는 최대 쌍의 수 출력 (인접한 칸에 같은 숫자 위치)
        ans = max(ans, count_pairs())

        # 4. 다음 시뮬레이션을 위해 grid 초기화
        refresh()

print(ans)