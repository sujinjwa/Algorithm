n = int(input()) # n : 격자의 크기

# grid : n * n 크기의 격자이며 각 칸에 1 또는 0 이 존재
# 1이면 동전이 있는 것이고 0이면 동전이 없는 것
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 위치 (x, y) 가 해당 격자 밖으로 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

#      위 위오 오 오아 아 아왼 왼 왼오
dxs = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 0, 1, 1, 1, 0, -1, -1, -1]

max_count = 0 # max_count : 최종적으로 3*3 격자의 경우의 수 중 가장 많은 동전의 개수

# gird 내 모든 칸을 순회, O(N^2)
for x in range(n):
    for y in range(n):
        
        cur_count = 0 # 해당 격자(x, y)가 중심에 있을 때의 3*3 격자에서의 동전의 개수

        # 해당 격자(x, y)와 인접한 8개의 칸 순회하여
        # grid 내부 밖으로 벗어나지 않으면서 동전이 몇 개 존재하는지(1인지) 확인
        for dx, dy in zip(dxs, dys):
            next_x = x + dx # (x, y)에서 인접한 칸의 x값(행)
            next_y = y + dy # (x, y)에서 인접한 칸의 y값(열)
            
            if in_range(next_x, next_y) and grid[next_x][next_y]:
                cur_count += 1
        
        # 지금까지 조회한 3*3 격자들 중 최대 동전의 개수를 max_count로 갱신
        if max_count < cur_count:
            max_count = cur_count

print(max_count)