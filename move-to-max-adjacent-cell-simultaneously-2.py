# n : 격자의 크기, m : 구슬의 개수, t : 주어진 시간
n, m, t = tuple(map(int, input().split()))

# a : n * n 크기의 격자
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# count : 이동하기 이전에 각 구슬의 위치 표시하기 위한 2차원 배열
count = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# next_count : 각 구슬이 이동한 이후 위치 표시하기 위한 2차원 배열
next_count = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def get_max_neighbor_pos(x, y):
    max_num, max_pos = 0, (0, 0)
    
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
            max_pos = (next_x, next_y)
    
    return max_pos

# (x, y) 위치에 있는 구슬 움직인다
def move(x, y):
    # 인접한 곳 중 가장 값이 큰 위치 찾기
    max_x, max_y = get_max_neighbor_pos(x, y)

    # 해당 위치로 이동
    next_count[max_x][max_y] += 1


def move_all():
    # next_count 내 구슬 개수 전부 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            next_count[i][j] = 0
    
    # (i, j) 위치에 구슬 있는 경우
    # 움직임 시도하고 그 결과 전부 next_count에 기록
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] == 1:
                move(i, j)
    
    # next_count 를 count에 복사
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[i][j] = next_count[i][j]

def remove_duplicate_marbles():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] > 1:
                count[i][j] = 0

def simulate():
    # step1 : 구슬을 전부 한번씩 움직인다
    move_all()

    # step2 : 움직임 이후에 충돌한 구슬들을 제거한다
    remove_duplicate_marbles()

# 초기 count 배열 설정
# 구슬이 있는 곳 입력받고 해당 위치에 1 표시한다
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    count[x][y] = 1

# t초 동안 시뮬레이션 진행한다
for _ in range(t):
    simulate()

# 출력
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans += count[i][j]

print(ans)