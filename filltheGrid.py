n, m = tuple(map(int, input().split()))

# n * m 크기의 격자 만들기
answer = [
    [0] * m
    for _ in range(n)
]

#          오 아래 왼 위
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0 # 시작 점의 행렬 좌표
dir_num = 0 # 시작 방향 := 오른쪽

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

answer[0][0] = 1 # 시작 점에 숫자 "1"로 초기화
# n*m 크기의 격자 오->아래->왼->위로 90도씩 돌며 방문하는 반복문
for i in range(2, n*m + 1):
		# 다음 이동 위치를 nx, ny에 대입
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if not is_range(nx, ny) or answer[nx][ny] != 0: # 만약 격자 범위 벗어났거나 이미 방문한 곳이라면
        dir_num = (dir_num + 1) % 4 # 방향 90도 변경
    
    # 방향 바꾼 후 다시 이동
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

# 2차원 배열인 answer 격자 출력
for row in answer:
    for elem in row:
        print(elem, end=' ')
    print()