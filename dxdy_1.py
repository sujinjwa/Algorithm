n = int(input()) # 움직이려는 방향과 거리 입력받는 횟수 n번
x, y = 0, 0 # 좌표 시작점 (0, 0)
#        동, 서, 남, 북  동, 서, 남, 북
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

# 움직이려는 방향과 거리 n번 입력받고, 이동 좌표 업데이트하는 반복문
for _ in range(n):
    direction, length = input().split() # 움직이려는 방향과 거리 입력받기
    length = int(length)
    idx = 0

    if direction == 'E':
        idx = 0
    elif direction == 'W':
        idx = 1
    elif direction == 'S':
        idx = 2
    else:
        idx = 3

    # 이동방향에 따른 이동한 거리 추적 
    x, y = x + dx[idx] * length, y + dy[idx] * length

# x,y의 최종 위치 출력
print(x, y)