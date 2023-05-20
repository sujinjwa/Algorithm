# L =: 왼쪽으로 90도 방향 전환
# R =: 오른쪽으로 90도 방향 전환
# F =: 바라보고 있는 방향으로 한칸 이동

orders = list(input()) # L, R, F 으로 이루어진 문자열 입력 받기
x, y = 0, 0 # 처음 위치하는 좌표

        # 동 남 서 북    동 남 서 북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

dir_num = 3 # 처음 바라보는 방향

for order in orders:
    if order == 'L':
        dir_num = (dir_num + 3) % 4 # 반시계 방향으로 회전 시 dir_num 재정의
    
    elif order == 'R':
        dir_num = (dir_num + 1) % 4 # 시계 방향으로 회전 시 dir_num 재정의
    
    else: # order == 'F' 일 때
        x, y = x + dx[dir_num], y + dy[dir_num] # 바라보고 있는 방향으로 한칸 이동
print(x, y)