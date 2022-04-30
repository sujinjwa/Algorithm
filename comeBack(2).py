n = int(input())

# 시작 위치 기록
x, y = 0, 0

# 동, 서, 남, 북 순으로 dxs, dys 정의
dxs, dys = [1, -1 ,0, 0], [0, 0, -1, 1]

# 답 저장
ans = -1

# 지금까지 걸린 시간 기록
elapsed_time = 0

# dir 방향으로 dist만큼 이동하는 함수
# 만약 시작지(0, 0)에 도달하면 true 반환
def move(move_dir, dist):
    global x, y
    global ans, elapsed_time

    for _ in range(dist):
        x, y = x + dxs[move_dir], y + dys[move_dir]

        # 이동한 시간 기록
        elapsed_time += 1

        # 시작지로 다시 돌아오면,
        # 답 갱신
        if x == 0 and y == 0:
            ans = elapsed_time
            return True
    
    return False

# 움직이는 것을 진행
for _ in range(n):
    c_dir, dist = tuple(input().split()) # 움직일 방향과 거리 입력 받기
    dist = int(dist)

    # 각 방향에 맞는 번호 붙이기
    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    # 주어진 방향대로 dist만큼 위치 이동
    done = move(move_dir, dist)

    # 시작 위치에 도달했다면, 종료
    if done:
        break

print(ans)