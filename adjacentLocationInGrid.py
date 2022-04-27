n = int(input()) # 격자의 행과 열 범위 나타내는 변수 n 입력 받기
x, y = 0, 0
        # 동 남 서 북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# n * n 크기의 격자 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 해당 좌표 (x, y)가 격자를 벗어나지 않고 안에 위치하는지 확인하는 함수
def in_range(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True

total_cnt = 0 # 인접한 칸에 숫자 1이 3개 이상 적혀있는 서로 다른 칸의 수 세는 변수
for x in range(n):
    for y in range(n):
        cnt = 0 # 각 좌표의 인접한 칸 중 숫자 1의 개수 세는 변수
        # 해당 좌표 (x, y)의 상하좌우 인접한 칸을 순회하며 해당 값에 숫자 1을 가지는지 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 좌표 (nx, ny)가 격자를 벗어나지 않으며, 숫자 1을 가질 경우
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            total_cnt += 1

print(total_cnt)    