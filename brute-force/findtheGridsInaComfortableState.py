n, m = tuple(map(int, input().split())) # 격자 크기 n과 색칠하는 횟수 m번 입력 받기

#           북  서 동 남
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

# m개의 줄에 걸쳐 색칠할 칸의 위치 (r, c) 입력 받기
printed = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# n * n 격자 생성
grid = [
    [0] * n
    for _ in range(n)
]

# 해당 칸(x, y)이 격자 벗어나는지 확인하는 함수
def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 해당 칸(x, y)이 색칠되었는지 확인하는 함수
def is_printed(x, y):
    return grid[x][y] == 1

for (r, c) in printed:
    r, c = r - 1, c - 1 # index 0부터 시작하므로 입력받은 r행 c열에서 -1씩 해줘야 함
    cnt = 0 # 인접한 4개의 칸 중 색칠된 칸의 개수
    if is_range(r, c):
        grid[r][c] = 1
    
    up_x, up_y = r + dxs[0], c + dys[0] # 위 칸
    left_x, left_y = r + dxs[1], c + dys[1] # 왼쪽 칸
    right_x, right_y = r + dxs[2], c + dys[2] # 오른쪽 칸
    down_x, down_y = r + dxs[3], c + dys[3] # 아래 칸

    if is_range(up_x, up_y) and is_printed(up_x, up_y): # 격자 벗어나지 않으면서 색칠된 칸인 경우
        cnt += 1
    if is_range(left_x, left_y) and is_printed(left_x, left_y):
        cnt += 1
    if is_range(right_x, right_y) and is_printed(right_x, right_y):
        cnt += 1
    if is_range(down_x, down_y) and is_printed(down_x, down_y):
        cnt += 1
    
    if cnt == 3: # 해당 격자가 '편안한 상태'인 경우
        print(1)
    else:
        print(0)