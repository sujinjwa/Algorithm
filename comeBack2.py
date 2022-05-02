inputs = list(input()) # n개의 L, R, F 명령 입력 받기

#           북  동 남 서
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

elapsed_time = 0 # 흐른 시간 나타내는 변수
x, y = 0, 0 # 시작점
dir_num = 0 # 시작 방향(북쪽)
flag = False # 시작점으로 되돌아 왔는지 여부 확인하는 변수

# 입력받은 명령 하나씩 순회하는 반복문
for elem in inputs:
    elapsed_time += 1 # 시간 1초씩 증가
    if elem == 'L':
        dir_num = (dir_num + 3) % 4 # 방향 왼쪽으로 90도 이동
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4 # 방향 오른쪽으로 90도 이동
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num] # 바라보는 방향으로 한칸 이동
    
    if x == 0 and y == 0: # (0, 0)에 다시 되돌아왔을 경우
        print(elapsed_time) # 지금까지 걸린 시간(초) 출력
        flag = True
        break

if flag == False: # 만약 n초 동안 (0, 0)에 도달하지 못했을 경우
    print(-1)