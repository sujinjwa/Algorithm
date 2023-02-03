n, t = tuple(map(int, input().split())) # n : 격자의 크기, t : 주어진 시간
r, c, d = input().split() # r, c = 구슬의 시작 위치, d : 구슬의 방향

directions = {
    # "방향" : dxs, dys 인덱스
    'L': 0,
    'U': 1,
    'D': 2,
    'R': 3,
}

r, c = int(r) - 1, int(c) - 1 # 구슬의 현재 위치
cur_dir = directions[d] # 구슬의 현재 방향

#     왼 위 아래 오
dxs = [0, -1, 1, 0]
dys = [-1, 0, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# t초마다 위치 이동
for _ in range(t):
    # 벽에 부딪힌 경우 방향 180도 회전
    if not in_range(r + dxs[cur_dir], c + dys[cur_dir]):
        cur_dir = 3 - cur_dir
        continue

    r, c = r + dxs[cur_dir], c + dys[cur_dir]

print(r + 1, c + 1)