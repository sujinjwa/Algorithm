# 변수 선언 및 입력 (직사각형의 크기 R * C)
R, C = tuple(map(int, input().split()))
# R * C 크기의 직사각형을 'W'과 'B'으로 입력 받기
grid = [
    input().split()
    for _ in range(R)
]

# 이동 시에 행과 열이 전부 증가하도록
# 모든 쌍을 다 잡아봅니다.
cnt = 0 # 시작, 도착 지점 제외 정확히 2번 점프하여 오른쪽 하단에 도달한 경우의 수
for i in range(1, R):
    for j in range(1, C):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수 세기
                if grid[0][0] != grid[i][j] and \
                grid [i][j] != grid[k][l] and \
                grid[k][l] != grid[R-1][C-1]:
                        cnt += 1

print(cnt)