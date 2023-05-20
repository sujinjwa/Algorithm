n, m = tuple(map(int, input().split())) # 직사각형 크기 : n * m

#      위 오른 아래 왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
cur_dir = 1

# 모든 칸이 0으로 이루어진 n * m 크기의 직사각형 생성
answer = [
    [0] * m
    for _ in range(n)
]

x, y = 0, 0 # 시작 위치
answer[x][y] = 1 # 시작 칸에 1 로 색칠

def in_range(x, y): # 직사각형 구간 벗어나는 경우
    return 0 <= x and x < n and 0 <= y and y < m

# n * m 크기의 칸을 2부터 색칠하는 반복문
for i in range(2, n * m + 1):

    nx, ny = x + dxs[cur_dir], y + dys[cur_dir] # 현재 바라보는 방향으로 한 칸 이동한 위치

    # 구간을 벗어났거나
    # 이미 방문한 곳인 경우
    # 위 <-> 아래, 오른 <-> 왼으로 방향 전환 시키기
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        cur_dir = (cur_dir + 1) % 4
    
    # 이동한 위치로 x, y 새로 선언하기
    x, y = x + dxs[cur_dir], y + dys[cur_dir]

    # 이동한 해당 위치에 i 로 색칠
    answer[x][y] = i

# 색칠 완성된 직사각형 출력
for row in answer:
    for elem in row:
        print(elem, end=' ')
    print()