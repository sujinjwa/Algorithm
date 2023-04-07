# n : 격자 크기, m : 도망자 수, h : 나무의 수, k : 턴 수
n, m, h, k = map(int, input().split())

# 상 하 오 왼
dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

# x, y : 도둑의 위치 / d : 1이면 좌우로만 움직임(방향 오른쪽), 2이면 상하로만 움직임(방향 아래쪾)
theives = []
for _ in range(m):
    x, y, d = map(int, input().split())

    if d == 1:
        theives.append((x - 1, y - 1, 2)) # 방향 좌우 오른쪽
    else:
        theives.append((x - 1, y - 1, 1)) # 방향 상하 아래쪽

grabber = (n // 2, n // 2) # 잡는 사람의 위치
grab_dir = 0 # 술래는 위를 보고 있다

# 나무들의 위치
trees = []
for _ in range(h):
    x, y = map(int, input().split())
    trees.append((x - 1, y - 1))

total_score = 0

grid = [
    [0] * n
    for _ in range(n)
]

# 술래가 가야 할 움직임들을 미리 추적해놓기
# 술래는 되돌아갈 때 무조건 0, 0 에서 아래로 이동하기 시작하면서 달팽이처럼 돈다
trace = [
    [0] * n
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

isRight = True # 술래가 정방향(True)으로 가는지 역방향(False)으로 가는지 확인하기 위함

# 나무 위치에다가 -1 설정해두기
for x, y in trees:
    grid[x][y] = -1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def init():
    x, y, curr_num = 0, 0, 0 # 시작점 (0, 0)에서 아래쪽 향함
    cnt = 1
    visited[x][y] = True
    trace[x][y] = cnt

    # 하 오 위 왼
    dxs1 = [1, 0, -1, 0]
    dys1 = [0, 1, 0, -1]

    for _ in range(n * n - 1):
        nx, ny = x + dxs1[curr_num], y + dys1[curr_num]
            
        if not in_range(nx, ny) or visited[nx][ny]:
            curr_num = (curr_num + 1) % 4 # 격자 벗어나면 방향 전환
            nx, ny = x + dxs1[curr_num], y + dys1[curr_num]
        
        visited[nx][ny] = True
        cnt += 1
        trace[nx][ny] = cnt
        x, y = nx, ny
    

def move_theives():
    # 현재 술래와의 거리가 3 이하인 도망자만 움직인다
    # |x1 - x2| + |y1 - y2| <= 3
    gx, gy = grabber
    for i in range(len(theives)):
        tx, ty, d = theives[i]
        distance = abs(tx - gx) + abs(ty - gy)
        if distance <= 3: # 움직일 수 있는 도망자! (tx, ty)

            nx, ny = tx + dxs[d], ty + dys[d] # nx, ny: 바라보는 방향으로 1칸 움직인 곳

            # 현재 바라보는 방향으로 1칸 움직일 때 격자를 벗어나지 않는 경우
            if in_range(nx, ny):
                # nx, ny에 술래가 있으면 이동 x
                if nx == gx and ny == gy:
                    continue

                # 술래 없으면 이동!
                theives[i] = (nx, ny, d)

            # 현재 바라보는 방향으로 1칸 움직일 때 격자를 벗어나는 경우
            else:
                # 방향 반대로 전환
                d = d - 1 if d == 3 or d == 1 else d + 1
                # 전환 후 1칸 이동 시 술래 없으면 1칸 이동!
                nx, ny = tx + dxs[d], ty + dys[d]

                if nx == gx and ny == gy:
                    theives[i] = (tx, ty, d)
                    continue
                
                theives[i] = (nx, ny, d)


def move_grabber():
    global grabber, grab_dir, isRight

    x, y = grabber # 술래의 현재 칸
    grabber = x + dxs[grab_dir], y + dys[grab_dir] # 한 칸 이동!

    
    # 다음 이동 시 방향 틀어지는 지점인지 미리 확인!
    # isRight == True이면 trace의 현재 위치에서 인접한 칸들 중
    # 현재 칸의 값 - 1 이 있는 값의 위치로 이동하도록 방향 업데이트!
    x1, y1 = grabber # 한칸 이동한 이후 위치한 곳
    nx, ny = x1 + dxs[grab_dir], y1 + dys[grab_dir] # 거기서 더 이동했을 때?
    if isRight:
        # 만약 술래가 현재 (0, 0)에 도착하면 그때도!! 방향 전환
        if x1 == 0 and y1 == 0:
            grab_dir = 1
            isRight = False
            return

        # 만약 trace[nx][ny] = trace[x][y] - 1 가 아니면 잘못된 방향으로 간 것!
        # 방향 전환 후 한 칸 이동
        if not in_range(nx, ny):
            grab_dir = grab_dir - 1 if grab_dir == 2 else (grab_dir + 2) % 5
            return
        
        if trace[nx][ny] != trace[x1][y1] - 1:
            grab_dir = grab_dir - 1 if grab_dir == 2 else (grab_dir + 2) % 5
            return

    else:
        # 만약 술래가 현재 (n//2, n//2)에 도착하면 그때도!! 방향 전환
        if x1 == n//2 and y1 == n//2:
            grab_dir = 0
            isRight = True
            return

        # isRight == False이면 현재 칸의 값 + 1인 곳으로 이동하도록 방향 업데이트!
        if not in_range(nx, ny):
            grab_dir = grab_dir + 3 if grab_dir == 0 else (grab_dir + 1) % 3
            return
        
        if trace[nx][ny] != trace[x1][y1] + 1:
            grab_dir = grab_dir + 3 if grab_dir == 0 else (grab_dir + 1) % 3
            return


def grab_theives(turn):
    global grabber, grab_dir, total_score
    x, y = grabber # 술래의 위치

    # 술래의 현재 위치 포함 시야 3칸 확인
    cnt = 0 # 도망자의 수
    removed_theives = []
    for _ in range(3):
        for tx, ty, td in theives:

            if x == tx and y == ty and grid[tx][ty] != -1:
                cnt += 1
                removed_theives.append((tx, ty, td))

        x, y = x + dxs[grab_dir], y + dys[grab_dir] # 한 칸 이동
    
    total_score += turn * cnt

    # 잡힌 도망자들 제거
    for tx, ty, td in removed_theives:
        theives.remove((tx, ty, td))


init()
def simulate(turn):
    # 1. m명의 도망자가 먼저 동시에 움직인다
    move_theives()

    # 2. 술래가 움직인다(바라보는 방향 갱신 꼭!)
    move_grabber()

    # 3. 술래의 시야에 위치한 도망자들 있는지 확인, 있으면 제거, 점수 업데이트
    grab_theives(turn + 1)

for turn in range(k):
    simulate(turn)

print(total_score)