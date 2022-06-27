#      북 동  남 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
cur_dir = 0 # 처음 바라보는 방향(북)

orders = list(input()) # n개의 명령 입력받을 문자열

x, y = 0, 0 # 초기 좌표 위치
for order in orders:
    if order == 'L': # 왼쪾으로 90도 방향 전환
        cur_dir = (cur_dir + 3) % 4
    elif order == 'R': # 오른쪽으로 90도 방향 전환
        cur_dir = (cur_dir + 1) % 4
    else: # 명령 F인 경우 바라보고 있는 방향으로 한칸 이동
        x, y = x + dxs[cur_dir], y + dys[cur_dir]

print(x, y) # 최종 위치 출력