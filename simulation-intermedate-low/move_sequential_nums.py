n, m = list(map(int, input().split())) # n : 격자의 크기, m : 턴의 수

# n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

#       ↑  ↗  →  ↘ ↓  ↙  ←  ↖
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 위치(x, y)가 격자 범위에 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 위치(x, y)와 인접한 8개의 위치(cur_x, cur_y)의 숫자 조회하여
# 최댓값과 그 위치 구하고
# 위치(x, y)에 있는 값과 교환
def find_max_neighbor(x, y):
    
    global grid

    max_pos = -1
    max_x, max_y = 0, 0

    for dx, dy in zip(dxs, dys):
        cur_x, cur_y = x + dx, y + dy
        
        if in_range(cur_x, cur_y) and grid[cur_x][cur_y] > max_pos:
            max_pos = grid[cur_x][cur_y]
            max_x, max_y = cur_x, cur_y
    
		# 값 교환
    temp = grid[x][y]
    grid[x][y] = grid[max_x][max_y]
    grid[max_x][max_y] = temp
    
# m번의 턴을 거쳐
# grid에서 1 ~ n*n 까지의 숫자 순서대로 조회하여
# find_max_neighbor 함수 실행
for _ in range(m):
    for num in range(1, n * n + 1):
        
        is_true = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == num:
                    find_max_neighbor(i, j)
                    is_true = True
                    break
            if is_true:
                break

# m번의 턴 거친 이후 격자판의 상태 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()