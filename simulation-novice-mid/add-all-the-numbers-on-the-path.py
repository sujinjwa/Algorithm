# n : 격자의 크기, t : 명령의 개수 (명령 = L, R, F)
n, t = tuple(map(int, input().split()))
orders = input() # L, R, F 로 이루어진 명령 입력 받기

# 숫자로 이루어진 n * n 크기의 정사각형 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cur_dir = 3 # 북쪽 향한 상태
x, y = n // 2, n // 2 # 시작 위치
#        동 남 서 북
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# x, y 위치가 격자 벗어나는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

sum_of_nums = grid[x][y] # 이동한 칸의 숫자들의 합 초기화

for order in orders:
    # L 명령어인 경우 방향을 왼쪽으로 변경
    if order == 'L':
        cur_dir = (cur_dir + 3) % 4
    # R 명령어인 경우 방향을 오른쪽으로 변경
    elif order == 'R':
        cur_dir = (cur_dir + 1) % 4
    # F 명령어인 경우 해당 방향으로 한 칸 전진
    else:
        # 이동할 수 있는 칸인 경우에만 전진
        if in_range(x + dx[cur_dir], y + dy[cur_dir]):
            x, y = x + dx[cur_dir], y + dy[cur_dir]
            sum_of_nums += grid[x][y]

print(sum_of_nums)