n, t = tuple(map(int, input().split())) # n : 격자의 크기, t : 주어진 시간

r, c, d = input().split() # 초기 구슬 위치: r행 c열, 초기 구슬 바라보는 방향: d

# R(오른쪽) U(위) D(아래) L(왼쪽)
mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

#      R  D   U  L
dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 실제 좌표 위치는 (r-1, c-1)
x = int(r) - 1
y = int(c) - 1
cur_dir = mapper[d] # 바라보는 방향

for _ in range(t): # t초 동안 반복
    
    x, y = x + dxs[cur_dir], y + dys[cur_dir] # 1초마다 움직인 좌표

    if in_range(x, y) == False: # 만약 좌표 벗어난 경우
        cur_dir = 3 - cur_dir # 위 <-> 아래, 왼 <-> 오 방향 전환
        x, y = x + dxs[cur_dir], y + dys[cur_dir] # 좌표에서 벗어나기 직전의 좌표로 원위치

print(x + 1, y + 1) # 최종 행열 위치 출력