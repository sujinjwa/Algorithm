from collections import deque

# n : 행의 개수, m : 열의 개수
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

visited2 = [
    [False for _ in range(m)]
    for _ in range(n)
]

q = deque()

# 1. 시뮬레이션 돌리기
# - 각 칸마다 상하좌우 확인하여 각 칸의 숫자 업데이트
# - 모든 칸 확인 후 새로운 grid에 전체 복붙
# - 모든 칸이 0이면 종료

# 2. 각 시뮬레이션마다 분리된 빙산 개수 2개 이상인지 확인
# - 그래프 탐색 진행, 각 덩어리별로 1, 2, 3 색칠하기
# - 2 이상의 숫자로 색칠된 칸 있으면 True

def all_melted():
    for row in grid:
        for elem in row:
            if elem:
                return False
    
    return True

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def reset_temp():
    global temp

    for x in range(n):
        for y in range(m):
            temp[x][y] = grid[x][y]


def melt():
    reset_temp()

    for x in range(n):
        for y in range(m):
            if grid[x][y]:
                
                melted_count = 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy

                    if in_range(nx, ny) and grid[nx][ny] == 0: # 인접한 칸이 바닷물이라면
                        melted_count += 1
                
                temp[x][y] = temp[x][y] - melted_count

                if temp[x][y] < 0:
                    temp[x][y] = 0

    for x in range(n):
        for y in range(m):
            grid[x][y] = temp[x][y]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    return in_range(x, y) and not visited2[x][y] and grid[x][y]

def bfs():
    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny):
                visited2[nx][ny] = True
                q.append((nx, ny))

def reset_vistied2():
    global visited2

    visited2 = [
        [False for _ in range(m)]
        for _ in range(n)
    ]


def over_two():
    reset_vistied2()
    
    cnt = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] and not visited2[x][y]:
                cnt += 1
                # print('x, y: ', x , y)
                visited2[x][y] = True
                q.append((x, y))
                bfs()

    if cnt >= 2:
        return True

    return False

def print_visited():
    for row in visited:
        for elem in row:
            print(elem, end= ' ')
        print()

def print_grid():
    for row in grid:
        for elem in row:
            print(elem, end= ' ')
        print()

def simulate():
    global T

    while not all_melted():
        # 1. 빙산 녹이기
        melt()

        # 2. 1년 지남
        T += 1

        # 3. 덩어리 개수 확인, 2개 이상이면 T 출력 및 break
        if(over_two()):
            print(T)
            break

    if all_melted():
        print(0)

T = 0
simulate()
