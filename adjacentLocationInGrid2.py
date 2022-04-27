n = int(input()) # n * n 격자 범위 나타내는 변수
# n * n 크기의 격자 arr 배열에 입력 받기
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

#      북 동 남 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 해당 좌표가 격자 벗어나지 않는지 확인하는 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 해당 좌표(x, y)에 인접한 칸 순회하는 함수
def adjacent_cnt(x, y):
    cnt = 0 # 인접한 칸이 숫자 1 가지는 횟수 세는 변수
    # 좌표 (x, y)의 상하좌우 칸 순회하는 반복문
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # 해당 좌표가 격자 벗어나지 않고, 숫자 1을 가질 경우
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt

# 각 칸 탐색하기
ans = 0
for i in range(n): # 행 하나하나 탐색
    for j in range(n): # 열 하나하나 탐색
        if adjacent_cnt(i, j) >= 3:
            ans += 1

print(ans)