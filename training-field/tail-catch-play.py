# n : 격자의 크기, m : 팀의 개수, k: 라운드 수
n, m, k = map(int, input().split())

# 0 : 빈칸, 1 : 머리사람, 2 : 나머지, 3 : 꼬리사람, 4 : 이동선
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 각 팀의 이동선
lines = [
    [] for _ in range(m)
]

# 각 팀의 꼬리사람 번째 수 (nth)
tails = [0 for _ in range(m)]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

turn = 0
total_score = 0

temp = []

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def dfs(x, y, idx, nth):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue

        if grid[nx][ny] == 0: # 빈칸인 경우 continue
            continue

        if visited[nx][ny]: # 이미 방문한 곳이면
            continue

        # x, y 가 머리사람일 때는 2가 있는 곳으로 이동
        if grid[x][y] == 1 and grid[nx][ny] != 2:
            continue
    
        nth += 1
        if grid[nx][ny] == 3: # 꼬리 사람이면
            tails[idx] = nth # nth: 몇 번째인지

        visited[nx][ny] = True
        lines[idx].append((nx, ny))
        dfs(nx, ny, idx, nth)

def dfs2(x, y, idx, nth):
    global temp

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue

        if grid[nx][ny] == 0: # 빈칸인 경우 continue
            continue

        if visited[nx][ny]: # 이미 방문한 곳이면
            continue

        # x, y 가 머리사람일 때는 2가 있는 곳으로 이동
        if grid[x][y] == 3 and grid[nx][ny] != 2:
            continue
    
        nth += 1
        if grid[nx][ny] == 1: # 꼬리 사람이면
            tails[idx] = nth # nth: 몇 번째인지

        visited[nx][ny] = True
        temp.append((nx, ny))
        dfs2(nx, ny, idx, nth)


def init():
    # 각 팀의 이동선 구하기
    # grid 내에 1을 우선 구하고
    # 1이 있는 위치로부터 2,3,4가 있는 곳으로만 탐색해서 이동선 구하기
    # 처음 조회할 때는 4나 0이 아닌 2가 있는 곳으로 가기
    idx = 0 # 팀 번호
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1: # 머리사람 찾기
                visited[x][y] = True
                lines[idx].append((x, y))
                dfs(x, y, idx, 1)
                idx += 1 # 다음 팀

def move_all():
    for i in range(m):
        temp = lines[i][-1]
        # 머리 사람을 따라 한 칸 이동
        for j in range(len(lines[i]) - 1, 0, -1):
            lines[i][j] = lines[i][j - 1]
            
        lines[i][0] = temp
    
    # lines 부분을 grid에 복붙해줘야 함
    for i in range(m):
        idx = 1
        for x, y in lines[i]:
            if idx == 1: # 머리사람인 경우
                grid[x][y] = 1
            
            elif idx == tails[i]: # 꼬리사람인 경우
                grid[x][y] = 3
            
            elif idx > 1 and idx < tails[i]:
                grid[x][y] = 2
            
            else:
                grid[x][y] = 4
            
            idx += 1


def throw_ball():
    # divided = turn // n
    remain = (turn - 1) % n
    # result1 = divided % 4
    t = (turn - 1) % (4 * n) + 1

    # result1이 0, 1, 2, 3 중 하나
    # 0이면 왼쪽에서 오른쪽으로, 1이면 아래에서 위로,
    # 2이면 오른쪽에서 왼쪽으로, 3이면 위에서 아래로 던져짐
    fx, fy = -1, -1 # 공을 맞은 사람

    if t <= n:
        # remain이 공이 던져지는 인덱스 + 1 한 값
        # 그니까 공은 grid[remain - 1][0] 에서 던져짐
        for i in range(n):
            # 사람이 있다면
            if grid[remain][i] != 0 and grid[remain][i] != 4:
                fx, fy = remain, i
                # print(fx, fy)
                return fx, fy

    elif t <= 2 * n:
        for i in range(n -1, -1, -1):
            if grid[i][remain] != 0 and grid[i][remain] != 4:
                fx, fy = i, remain
                return fx, fy
    
    elif t <= 3 * n:
        for i in range(n - 1, -1, -1):
            if grid[n -1 - remain][i] != 0 and grid[n - 1 - remain][i] != 4:
                fx, fy = n -1 -remain, i
                return fx, fy
    
    else:
        for i in range(n):
            if grid[i][n -1 - remain] != 0 and grid[i][n - 1 - remain] != 4:
                fx, fy = i, n -1 -remain
                return fx, fy

    return fx, fy

def add_score(fx, fy):
    global total_score, temp

    if fx == -1 and fy == -1:
        return
    # 이 밑 부분은 다른 단계 함수 생성하여 구현

    # 공을 맞은 사람이 팀 내에서 몇 번째 사람인지 구하고
    # 번째의 제곱 만큼 점수 추가하기
    for i in range(m):
        idx = 1
        for x, y in lines[i]:
            if x == fx and y == fy:
                total_score += idx * idx

                # i번째 line에 속한 팀의 머리사람과 꼬리사람 바꾼다
                for i1 in range(n):
                    for j1 in range(n):
                        visited[i1][j1] = False
                
                xl, yl = lines[i][tails[i] - 1] # lines[i]의 꼬리의 번째 수
                temp = []
                temp.append((xl, yl))
                visited[xl][yl] = True
                dfs2(xl, yl, i, 1)

                lines[i] = temp

                # lines[i] 변경된 사항을 grid에 복붙
                idx2 = 1
                for cx, cy in lines[i]:
                    if idx2 == 1: # 머리사람인 경우
                        grid[cx][cy] = 1
                    
                    elif idx2 == tails[i]: # 꼬리사람인 경우
                        grid[cx][cy] = 3
                    
                    elif idx2 > 1 and idx2 < tails[i]:
                        grid[cx][cy] = 2
                    
                    else:
                        grid[cx][cy] = 4
                    
                    idx2 += 1
                return

            idx += 1


def simulate():
    # 1. 각 팀은 머리사람을 따라서 한 칸 이동한다.
    move_all()

    # 2. 각 라운드마다 정해진 선을 따라 공을 던진다.
    fx, fy = throw_ball()
    # fx, fy는 맞은 사람의 위치

    # 3. 공을 맞은 사람의 번째 수의 제곱 만큼 점수 더한다.
    add_score(fx, fy)

init()
for _ in range(k):
    turn += 1
    simulate()

print(total_score)