# n : 격자의 크기, m : 구슬의 개수, t : 주어진 시간
n, m, t = tuple(map(int, input().split()))

# grid : n * n 크기의 격자에 각 칸에 해당하는 숫자 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# starts : m개의 구슬들의 각 시작 위치 나타내는 r, c 값 입력 받기
starts = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# count : 이동하기 이전에 각 구슬의 위치 표시하기 위한 2차원 배열
count = [
    [0] * n
    for _ in range(n)
]

# count 배열에 각 구슬이 위치한 곳을 1로 표시
for r, c in starts:
    count[r - 1][c - 1] = 1

# next_count : 각 구슬이 이동한 이후 위치 표시하기 위한 2차원 배열
next_count = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def is_max_pos(max_pos, next_x, next_y):
    if max_pos < grid[next_x][next_y]:
        return True
    
    return False

# 상하좌우 순으로 이동하기 위한 값, x : 행, y : 열
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(t):
    # t초 중 1초에 한번씩 모든 구슬 이동
    for x in range(n):
        for y in range(n):
            if count[x][y] == 1: # 해당 x, y칸에 구슬이 있는 경우
                max_pos = 0
                max_x, max_y = 0, 0
                # 각 구슬의 상하좌우 한칸씩 이동했을 때의 위치 확인
                for dx, dy in zip(dxs, dys):
                    next_x, next_y = x + dx, y + dy

                    # 이동한 위치가 격자를 벗어나지 않고
                    # 지금까지 조회한 칸 중 가장 큰 값이 적혀있는 경우
                    if in_range(next_x, next_y) and is_max_pos(max_pos, next_x, next_y):
                        max_pos = grid[next_x][next_y]
                        max_x, max_y = next_x, next_y
 
                # 가장 큰 값이 적혀있는 숫자의 위치로 이동
                next_count[max_x][max_y] += 1
    
    # 1초 동안 모든 구슬이 인접한 곳 중 큰 값의 위치로 이동한 이후
    # next_count 확인
    for x in range(n):
        for y in range(n):
            if next_count[x][y] > 1: # 두 구슬 이상이 충돌한 경우
                next_count[x][y] = 0 # 충돌한 모든 구슬 제거
    
    # count를 next_count로 덮어 씌우기
    count = next_count

    # next_count의 모든 칸을 0으로 초기화
    next_count = [
        [0] * n
        for _ in range(n)
    ]

# t초 후 남아있는 구슬의 수 출력
cnt = 0
for x in range(n):
    for y in range(n):
        if count[x][y] == 1:
            cnt += 1

print(cnt)