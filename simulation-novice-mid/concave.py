import sys
# 19 * 19 크기의 오목판에 1(검은색 바둑알), 2(흰색 바둑알), 0(놓이지 않는 자리) 입력 받기
arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

# 좌표가 아닌 2차원 행렬로 생각해야 함
# 따라서 dx가 세로열 / dy가 가로열
# x := 아래로 이동시 +1 위로 이동시 -1
# y := 오른쪽 이동시 +1 왼쪽 이동시 -1

        # 북 북동 동 동남 남 남서 서 서북 
dxs, dys = [-1, -1, 0,  1,  1,  1, 0, -1], [0,  1,  1,  1,  0, -1, -1, -1]

def in_range(x, y): # (x, y) 좌표가 19 * 19 크기의 오목판에 위치하는지 확인
    return x >= 0 and x < 19 and y >= 0 and y < 19

def is_same_color(i, j, x, y): # 한칸 앞으로 접근한 위치와 그 이전의 위치에 있는 바둑알 색상 같은지 확인
    return arr[i][j] == arr[x][y]

# 19 * 19 크기의 오목판을 행1 열1 위치부터 차례대로 탐색하는 반복문
for i in range(19):
    for j in range(19):
        # 8가지의 방향을 모두 탐색하며, 같은 색상의 바둑알이 5개 있을 경우 승리
        
        if arr[i][j] == 0:
            continue

        for dx, dy in zip(dxs, dys): # 8가지의 방향으로 접근하는 반복문
            for l in range(1, 5): # 현재 위치인 (i, j)에서 앞으로 나아가는 횟수 := l
                curx = i # 현재 행 번호
                cury = j # 현재 열 번호
                nx, ny = curx + dx * l, cury + dy * l # 8가지의 방향 중 4번씩 앞으로 나아갔을 때 4가지의 각각 위치
                
                if in_range(nx, ny) == False:
                    break
                if is_same_color(i, j, nx, ny) == False:
                    break
                    
                if l == 4: # 5개의 바둑알 모두 오목판 벗어나지 않고, 같은 색상인 경우
                    print(arr[i][j]) # 해당 위치의 색상 출력
                    print(i + (2 * dx) + 1, j + (2 * dy) + 1) # 행과 열 숫자 구해야 하므로 index에서 1씩 더해줘야 함
                    sys.exit()

print(0)