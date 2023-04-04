# n : 격자의 크기, m : 플레이어의 수, k : 라운드의 수
n, m, k = tuple(map(int, input().split()))

# n * n 크기의 격자 내 총의 정보 입력 받기
# : 0은 빈 칸, 0보다 큰 값은 총의 공격력 의미
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid2 = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# 각 칸에 놓여있는 총들
for x in range(n):
    for y in range(n):
        if grid[x][y] != 0:
            grid2[x][y].append(grid[x][y])

# 각 플레이어들의 정보(위치, 방향, 초기 능력치, 포인트, 보유한 총의 공격력)
pos = []
direc = [] # 북: 0, 동: 1, 남: 2, 서: 3
power = []
point = [0] * m
gun = [0] * m

for _ in range(m):
    x, y, d, s = tuple(map(int, input().split()))
    pos.append((x - 1, y - 1)) # x, y : 플레이어의 위치
    direc.append(d) # 방향
    power.append(s) # 초기 능력치

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def can_go(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(k):
    lose_player = []
    win_player = []

    for i in range(m):
        # 진 플레이어의 경우 continue
        for j in range(len(lose_player)):
            if lose_player[j] == i:
                continue

        # 1-1. 플레이어들이 순차적으로 한 칸씩 이동        
        x, y = pos[i]
        new_x, new_y = x + dxs[direc[i]], y + dys[direc[i]]

        if not can_go(new_x, new_y): # 격자를 벗어나는 경우
            direc[i] = (direc[i] + 2) % 4 # 정반대 방향으로 방향 전환
            new_x, new_y = x + dxs[direc[i]], y + dys[direc[i]]
        
        pos[i] = new_x, new_y # 한 칸 이동
    

        # 2. 이동한 칸에 플레이어 있는지 확인
        x, y = pos[i] # 이동한 칸
        
        has_other_player = False
        other_player = -1 # other_player의 번호
        for j in range(m):
            px, py = pos[j]
            if i != j and x == px and y == py:
                has_other_player = True
                other_player = j
                break
    
        # 2-1. 이동한 칸에 플레이어가 없다면 총이 있는지 확인
        if not has_other_player:
            # max_g = 0
            # index = -1
            # for j in range(len(grid2[x][y])):
            #     if max_g < grid2[x][y][j]:
            #         max_g = grid2[x][y][j]
            #         index = j

            # if gun[i] < max_g: # 놓여 있는 총 중 가장 쎈 총과 가지고 있는 총 중 더 쎈 총 선택
            #     temp = gun[i]
            #     gun[i] = max_g

            #     arr = []
            #     for k in range(len(grid2[x][y])):
            #         if grid2[x][y][k] != max_g:
            #             arr.append(grid2[x][y][k])
                
            #     grid2[x][y] = arr
            #     grid2[x][y].append(temp)
            grid2[x][y].append(gun[i])
            grid2[x][y].sort(reverse=True)
            a = grid2[x][y][0]
            gun[i] = a
            grid2[x][y].pop(0)

    
        # 2-2-1. 이동한 칸에 플레이어가 있다면
        else:
            if power[i] + gun[i] > power[other_player] + gun[other_player]: # win
                point[i] += ((power[i] + gun[i]) - (power[other_player] + gun[other_player]))
                win_player.append(i)
                lose_player.append(other_player)
                
            elif power[i] + gun[i] < power[other_player] + gun[other_player]: # lose
                point[other_player] += ((power[other_player] + gun[other_player]) - (power[i] + gun[i]))
                win_player.append(other_player)
                lose_player.append(i)
            else: # 같다면
                if power[i] > power[other_player]: # win
                    point[i] += ((power[i] + gun[i]) - (power[other_player] + gun[other_player]))
                    win_player.append(i)
                    lose_player.append(other_player)
                else: # lose
                    point[other_player] += ((power[other_player] + gun[other_player]) - (power[i] + gun[i]))
                    win_player.append(other_player)
                    lose_player.append(i)


            # 2-2-2. 진 플레이어
            num = lose_player[-1] # 금방 진 플레이어의 번호
            lx, ly = pos[num] # 금방 진 플레이어의 위치

            # 본인이 가지고 있는 총 해당 격자에 내려놓기
            grid2[lx][ly].append(gun[num])
            gun[num] = 0

            # 한 칸 이동
            for _ in range(4):
                new_x, new_y = lx + dxs[direc[num]], ly + dys[direc[num]]

                # 해당 칸에 다른 플레이어 있는지 확인
                has_other_player = False
                for k in range(m):
                    rx, ry = pos[k]
                    if num != k and rx == new_x and ry == new_y:
                        has_other_player = True

                if not has_other_player and can_go(new_x, new_y):
                    # direc[num] = (direc[num] + 1) % 4 # 방향을 오른쪽으로 90도 이동
                    # new_x, new_y = lx + dxs[direc[num]], ly + dys[direc[num]]
                    pos[num] = new_x, new_y # 한 칸 이동
                    break
                
                direc[num] = (direc[num] + 1) % 4
            
            #pos[num] = new_x, new_y # 한 칸 이동
    
            lx, ly = pos[num] # 이동한 칸

            # 가장 공격력 높은 총 획득
            # max_g = 0 # 가장 쎈 총의 공격력
            # index = -1
            # for j in range(len(grid2[lx][ly])):
            #     if max_g < grid2[lx][ly][j]:
            #         max_g = grid2[lx][ly][j]
            #         index = j

            # if gun[num] < max_g: # 놓여 있는 총 중 가장 쎈 총과 가지고 있는 총 중 더 쎈 총 선택
            #     temp = gun[num]
            #     gun[num] = max_g

            #     arr = []
            #     for k in range(len(grid2[lx][ly])):
            #         if grid2[lx][ly][k] != max_g:
            #             arr.append(grid2[lx][ly][k])
                
            #     grid2[lx][ly] = arr
            #     grid2[lx][ly].append(temp)
            
            grid2[lx][ly].append(gun[num])
            grid2[lx][ly].sort(reverse=True)
            a = grid2[lx][ly][0]
            gun[num] = a
            grid2[lx][ly].pop(0)


            # 이긴 플레이어
            num = win_player[-1] # 금방 이긴 플레이어의 번호
            wx, wy = pos[num] # 금방 이긴 플레이어의 위치

            # 가장 공격력 높은 총 획득           
            # max_g = 0
            # index = -1
            # for j in range(len(grid2[wx][wy])):
            #     if max_g < grid2[wx][wy][j]:
            #         max_g = grid2[wx][wy][j]
            #         index = j

            # if gun[num] < max_g: # 놓여 있는 총 중 가장 쎈 총과 가지고 있는 총 중 더 쎈 총 선택
            #     temp = gun[num]
            #     gun[num] = max_g

            #     arr = []
            #     for k in range(len(grid2[wx][wy])):
            #         if grid2[wx][wy][k] != max_g:
            #             arr.append(grid2[wx][wy][k])
                
            #     grid2[wx][wy] = arr
            #     grid2[wx][wy].append(temp)
            grid2[wx][wy].append(gun[num])
            grid2[wx][wy].sort(reverse=True)
            a = grid2[wx][wy][0]
            gun[num] = a
            grid2[wx][wy].pop(0)

for p in point:
    print(p, end=' ')