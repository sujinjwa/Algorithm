# n : 격자의 크기, m : 박멸이 진행되는 년 수, k : 제초제 확산 범위, c : 제초제 남아있는 년 수
n, m, k, c = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 제초제 뿌린 곳 확인하기 위한 2차원 배열
herb = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# m년 동안 총 박멸된 나무의 그루 수
total_removed_trees = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 나무의 인접한 위치에 또 다른 나무가 있다면 있는 만큼 나무 성장
def adjacent_grow():
    for x in range(n):
        for y in range(n):
            cnt = 0 # cnt : 인접한 위치에 있는 나무의 개수
            
            if grid[x][y] >= 1: # 나무가 있다면
                
                for i in range(4): # 상하좌우 조회
                    nx, ny = x + dxs[i], y + dys[i]

                    # 1. in_range 이면서 2. 벽이 아닌 나무인 경우
                    if in_range(nx, ny) and grid[nx][ny] >= 1:
                        cnt += 1
            
            # cnt만큼 성장
            grid[x][y] += cnt


# 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식 진행
def breeding():

    temp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for x in range(n):
        for y in range(n):
            cnt = 0 # cnt : 번식 가능한 칸의 개수
            pos = [] # 번식 가능한 칸의 위치 저장하는 곳

            if grid[x][y] >= 1:

                for i in range(4):
                    nx, ny = x + dxs[i], y + dys[i]

                    # 1. in_range 2. 제초제도 없음 3. 벽이 아님 4. 다른 나무 없음
                    if not in_range(nx, ny):
                        continue
                    
                    if herb[nx][ny]: # 제초제 뿌린 곳이면 continue
                        continue
                    
                    if grid[nx][ny] == 0: # 벽이 아닌 다른 나무 없는 곳이면
                        cnt += 1
                        pos.append((nx, ny))
                        print(nx, ny)
            
            # 번식 진행
            for i, j in pos:
                temp[i][j] += (grid[x][y] // cnt)
    
    for x in range(n):
        for y in range(n):
            
            if temp[x][y]:
                grid[x][y] = temp[x][y]
            # grid[x][y] += temp[x][y] 도 가능


def find_most_killed_pos():
    max_cnt = 0 # 가장 많이 박멸되는 나무의 총 그루 수
    max_pos = (-1, -1) # 가장 많이 박멸되는 칸

    for x in range(n):
        for y in range(n):
            cnt = 0 # cnt : 박멸되는 나무의 개수

            if grid[x][y] >= 1:
                
                # 시작점의 나무의 개수 더해주기
                cnt += grid[x][y]

                # 1) k칸 만큼 왼쪽 윗 대각선 방향으로 박멸되는 나무의 개수
                for i in range(1, k + 1):
                    nx, ny = x - i, y - i

                    if not in_range(nx, ny) or grid[nx][ny] <= 0:
                        # 전파되는 도중 벽이 있거나 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
                        break
                    
                    cnt += grid[nx][ny]

                # 2) k칸 만큼 왼쪽 아랫 대각선 방향으로 박멸되는 나무의 개수
                for i in range(1, k + 1):
                    nx, ny = x + i, y - i

                    if not in_range(nx, ny) or grid[nx][ny] <= 0:
                        # 전파되는 도중 벽이 있거나 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
                        break
                    
                    cnt += grid[nx][ny]

                # 3) k칸 만큼 오른쪽 윗 대각선 방향으로 박멸되는 나무의 개수
                for i in range(1, k + 1):
                    nx, ny = x - i, y + i

                    if not in_range(nx, ny) or grid[nx][ny] <= 0:
                        # 전파되는 도중 벽이 있거나 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
                        break
                    
                    cnt += grid[nx][ny]

                # 4) k칸 만큼 오른쪽 아랫 대각선 방향으로 박멸되는 나무의 개수
                for i in range(1, k + 1):
                    nx, ny = x + i, y + i

                    if not in_range(nx, ny) or grid[nx][ny] <= 0:
                        # 전파되는 도중 벽이 있거나 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
                        break
                    
                    cnt += grid[nx][ny]

            if max_cnt < cnt:
                max_cnt = cnt
                max_pos = (x, y)

    # if max_pos == (-1, -1): # 모든 나무가 사라진 경우
    #     return 'EMPTY', 0
    # else:
    return max_pos, max_cnt


# 제초제 뿌리는 곳이라는 표시는 grid2의 해당 칸에 -2 를 해놓는 것!
# => herb의 해당 칸에 c를 넣어주고, grid의 해당 칸에는 0으로! 나무 없애기로 변경
def kill(pos):
    x, y = pos

    # 시작점에 제초제 뿌리기
    grid[x][y] = 0
    herb[x][y] = c + 1

    # 1) k칸 만큼 왼쪽 윗 대각선 방향으로 박멸되는 나무의 개수
    for i in range(1, k + 1):
        nx, ny = x - i, y - i

        if not in_range(nx, ny):
            break
        
        if grid[nx][ny] == -1: # 벽이면
            break
        
        if grid[nx][ny] == 0:
            # 전파되는 도중 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
            herb[nx][ny] = c + 1
            break
        
        grid[nx][ny] = 0
        herb[nx][ny] = c + 1
                    
    # 2) k칸 만큼 왼쪽 아랫 대각선 방향으로 박멸되는 나무의 개수
    for i in range(1, k + 1):
        nx, ny = x + i, y - i

        if not in_range(nx, ny):
            break
        
        if grid[nx][ny] == -1: # 벽이면
            break
        
        if grid[nx][ny] == 0:
            # 전파되는 도중 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
            herb[nx][ny] = c + 1
            break
        
        grid[nx][ny] = 0
        herb[nx][ny] = c + 1
                    
    # 3) k칸 만큼 오른쪽 윗 대각선 방향으로 박멸되는 나무의 개수
    for i in range(1, k + 1):
        nx, ny = x - i, y + i

        if not in_range(nx, ny):
            break
        
        if grid[nx][ny] == -1: # 벽이면
            break
        
        if grid[nx][ny] == 0:
            # 전파되는 도중 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
            herb[nx][ny] = c + 1
            break
        
        grid[nx][ny] = 0
        herb[nx][ny] = c + 1

    # 4) k칸 만큼 오른쪽 아랫 대각선 방향으로 박멸되는 나무의 개수
    for i in range(1, k + 1):
        nx, ny = x + i, y + i

        if not in_range(nx, ny):
            break
        
        if grid[nx][ny] == -1: # 벽이면
            break
        
        if grid[nx][ny] == 0:
            # 전파되는 도중 나무가 없는 칸이면 제초제는 거기까지만 뿌려짐
            herb[nx][ny] = c + 1
            break
        
        grid[nx][ny] = 0
        herb[nx][ny] = c + 1


def remove_kill():
    for x in range(n):
        for y in range(n):

            if herb[x][y] > 0: # 제초제가 남아있는 칸인 경우
                herb[x][y] -= 1 # 1년 지났음을 표시


def simulate():
    global total_removed_trees

    # 1. 모든 나무들이 그들의 인접한 나무의 개수만큼 성장
    adjacent_grow()
    print(grid)

    # 2. 번식 진행
    breeding()
    print(grid)

    # 3. 가장 많이 박멸되는 칸 구하기
    pos, max_cnt = find_most_killed_pos()
    print(pos)
    print(max_cnt)
    
    # 총 박멸된 나무의 그루 수 갱신
    total_removed_trees += max_cnt

    # if pos == 'EMPTY':
    #     exit = True
    #     return

    # 3-1. 가장 많이 박멸되는 칸에 제초제 뿌리기
    kill(pos)
    print(grid)

    # 3-2. c년 지난 경우 제초제 없애기
    remove_kill()
    print(grid)
    print(herb)

# m년 동안 박멸 시뮬레이션 진행
for _ in range(m):
    simulate()

print(total_removed_trees)