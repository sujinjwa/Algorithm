# n : 격자의 크기, m : 턴의 개수
n, m = tuple(map(int, input().split()))

# n * n 크기의 격자 내 각 숫자들 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# (x, y)위치의 인접한 칸들 중 가장 큰 값이 위치한 칸 구하기
def find_max_neighbor(x, y):
    dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
    dys = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    max_neighbor_num = 0
    max_x, max_y = 0, 0
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy # (next_x, next_y) = (x, y)위치의 인접한 칸

        # (next_x, next_y)위치가 격자를 벗어나지 않으면서 최대값인지 확인
        if in_range(next_x, next_y) and grid[next_x][next_y] > max_neighbor_num:
            max_neighbor_num = grid[next_x][next_y]
            max_x, max_y = next_x, next_y
    
    return (max_x, max_y)

# grid 격자 내에 1 ~ n * n 숫자 하나씩 찾기
def simulate():
    for num in range(1, n * n + 1):
        for x in range(n):
            finished = False
            for y in range(n):
                if grid[x][y] == num:
                    # 각 칸의 인접한 칸들 중 가장 큰 값의 위치(max_x, max_y) 구하기
                    max_x, max_y = find_max_neighbor(x, y)

                    # (x, y)칸의 숫자와 (max_x, max_y) 칸의 숫자끼리 위치 교환
                    temp = grid[x][y]
                    grid[x][y] = grid[max_x][max_y]
                    grid[max_x][max_y] = temp
                    finished = True
                    break
            
            # 한 번 교환이 이루어졌으면 다음 숫자 찾기
            if finished:
                break


# m번의 턴 진행
for _ in range(m):
    simulate()

# m번의 턴 진행 후 격자판의 상태 출력
for row in grid:
    for num in row:
        print(num, end=' ')
    print()