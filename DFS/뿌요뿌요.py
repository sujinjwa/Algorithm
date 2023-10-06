n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

all_cnt_of_block = 0
cnt_of_block = 0
max_block = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

def dfs(x, y, cnt):
    global cnt_of_block
    
    cnt_of_block = max(cnt_of_block, cnt)

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny) and grid[x][y] == grid[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1)

for x in range(n):
    for y in range(n):

        if can_go(x, y):
            cnt_of_block = 0
            cnt = 1 # cnt : 칸의 개수
            visited[x][y] = True
            dfs(x, y, cnt)

            # 블럭의 크기 최대값으로 갱신
            max_block = max(max_block, cnt_of_block)

            # 블럭 이루는 칸의 수가 4 이상인 경우 터지게 되는 블럭의 수 + 1
            if cnt_of_block >= 4:
                all_cnt_of_block += 1

print(all_cnt_of_block, max_block)