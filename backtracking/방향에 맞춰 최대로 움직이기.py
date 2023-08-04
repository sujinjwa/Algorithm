n = int(input()) # n : 격자의 크기

# grid : 각 칸에 해당하는 숫자가 입력된 n * n 크기의 2차원 격자
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

#        위 오위 오 오아 아 왼아 왼 왼위
direcs = [0, (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# directions : 각 칸에 적힌 방향 나타내는 숫자
directions = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = tuple(map(int, input().split())) # (r, c) : 시작 위치

arr = [(r, c)]
ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(curr_num, r, c):
    for i in range(1, n + 1):
        dx, dy = direcs[directions[r][c]]

        nx, ny = r + dx * i, c + dy * i

        if in_range(nx, ny) and grid[nx][ny] > grid[r][c]:
            return True
    
    return False


# 현재 위치 (r, c)에서 출발하여 curr_num번째로 이동할 수 있는 칸 고르는 함수
def choose(curr_num, r, c):
    global ans

    # 만약 이동할 수 있는 방향에 더 큰 숫자가 없는 경우 종료
    if not can_go(curr_num, r, c):
        ans = max(ans, curr_num)
        return

    # 이동할 수 있는 숫자
    # = 해당 방향으로 격자 범위 벗어나기 직전까지 이동하면서 만난 모든 숫자들
    for i in range(1, n + 1):
        dx, dy = direcs[directions[r][c]] # 현재 위치(r, c)에서 이동 가능한 방향
        
        nx, ny = r + dx * i, c + dy * i # nx, ny : 이동한 다음 위치

        # nx, ny가 격자 벗어나지 않으면서 더 큰 값이면 arr에 추가
        if in_range(nx, ny) and grid[nx][ny] > grid[r][c]:
            arr.append((nx, ny))
            choose(curr_num + 1, nx, ny)
            arr.pop()

r, c = r - 1, c - 1        
choose(0, r, c)

print(ans)