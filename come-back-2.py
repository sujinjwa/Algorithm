orders = input() # n개의 명령 입력 받기

x, y = 0, 0 # 시작 위치
cur_dir = 0 # 시작 방향

# 북, 동, 남, 서로 이동하는 데 필요한 x, y 연산 모음
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

is_back = False # 다시 (0,0)으로 돌아오는지 판단하기 위한 변수

# 입력 받은 명령에 따라 방향 전환 또는 전진 진행
for i in range(len(orders)):
    if orders[i] == 'L': # 왼쪽으로 90도 방향 전환
        cur_dir = (cur_dir + 3) % 4
        continue
    
    elif orders[i] == 'R': # 오른쪽으로 90도 방향 전환
        cur_dir = (cur_dir + 1) % 4
        continue
    
    else: # cur_dir 방향으로 1칸 전진
        x, y = x + dxs[cur_dir], y + dys[cur_dir]

        if x == 0 and y == 0: # 시작점으로 돌아온 경우 걸린 시간 출력
            is_back = True
            print(i + 1)
            break

# 시작점으로 되돌아오지 못한 경우 -1 출력
if not is_back:
    print(-1)