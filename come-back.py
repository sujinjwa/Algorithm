n = int(input()) # n: 방향과 거리 입력받는 총 횟수

directions = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3,
}

#    왼 아 위 오
dxs = [0, 1, -1, 0]
dys = [-1, 0, 0, 1]

x, y = 0, 0 # 시작 위치
cnt = 0
is_back = False

# 이동 방향과 거리 n번 입력 받기
for _ in range(n):
    direction, distance = input().split()
    
    distance = int(distance)
    
    # 입력 받은 distance(이동 횟수)만큼 이동
    for _ in range(distance):
        cur_dir = directions[direction] # 이동 방향

        # cur_dir 방향으로 한 칸 전진하며, 이동 시간 + 1
        x, y = x + dxs[cur_dir], y + dys[cur_dir]
        cnt += 1

        # 다시 (0, 0)에 돌아오는 경우 걸린 시간 출력
        if x == 0 and y == 0:
            is_back = True
            print(cnt)
            break
    
    if is_back:
        break

# 시작점으로 돌아오지 못한 경우 -1 출력
if not is_back:
    print(-1)