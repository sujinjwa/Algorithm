n = int(input())

# 움직이려는 방향과 움직일 거리를 n번에 걸쳐 배열 dd에 입력 받기
dd = [
    input().split()
    for _ in range(n)
]

# n*n 크기의 2차원 grid 만들기
answer = [
    [0] * n
    for _ in range(n)
]

#           W  S   N  E    W   S  N  E
dxs, dys = [0, 1, -1, 0], [-1, 0, 0, 1]
x, y = 0, 0 # 현재 위치

total_time = 0 # 이동 후 다시 (0, 0)로 돌아오기까지의 시간
answer[0][0] = 1 # 현재 위치에 초기 값 선언
breaker = False # 이중 for문 빠져나오기 위한 boolean 변수

# 입력받았던 움직이려는 방향(direction)과 움직일 거리(distance) 한 쌍씩 확인하는 반복문
for (direction, distance) in dd:
    # 이동할 방향의 인덱스(dir_num) 선언
    if direction == 'W':
        dir_num = 0
    elif direction == 'S':
        dir_num = 1
    elif direction == 'N':
        dir_num = 2
    else:
        dir_num = 3
    
    # 움직일 거리만큼 한 칸씩 이동하며 1초씩 증가시키는 반복문
    for _ in range(int(distance)):
        x, y = x + dxs[dir_num], y + dys[dir_num] # 한 칸씩 이동하기
        total_time += 1 # 1초 증가

        if x == 0 and y == 0: # 이동한 위치가 (0, 0) 이라면
            breaker = True
            break
    if breaker:
        break

sum_time = 0 # 모든 입력으로 이동했을 때의 시간((0,0)으로 돌아오지 않았을 때의 시간)
for (direction, distance) in dd:
    sum_time += int(distance)

if total_time == sum_time: # (0,0)으로 돌아오지 못했을 경우
    print(-1)
else:
    print(total_time)