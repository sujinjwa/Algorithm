# 격자의 크기 n, 주어진 시간 t 입력 받기
n, t = tuple(map(int, input().split()))

# n * n 크기의 격자 만들기 (생략 가능)
# grid = [
#    [0] * n
#    for _ in range(n)
# ]

# 구슬의 초기 위치 r행 c열, 방향 d 입력 받기
r, c, d = input().split()

# 초기 좌표 위치 := (r, c)
x, y = int(r) - 1, int(c) - 1 # 배열의 인덱스 0부터 시작하므로, 좌표 -> 행, 열 변환 시 -1 해주어야 함

#          위  오  왼 아래
dxs, dys = [-1, 0, 0, +1], [0, 1, -1, 0]

mapper = {
    'U' : 0, # 위
    'R' : 1, # 오
    'L' : 2, # 왼
    'D' : 3 # 아래
}

move_dir = mapper[d] # 입력받은 방향 문자열 변수 d와 match되는 index값 mapper dictionary에서 찾기

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 주어진 시간만큼 좌표 이동 및 방향 바꾸는 반복문
for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not is_range(nx, ny): # 이동할 시 격자 범위를 벗어날 경우
        move_dir = 3 - move_dir # 방향 바꾸기
        # i += 1 # 1초 흐름 (생략 가능, i 없이 주어진 시간만큼만 반복되는 for문 순회 가능)
    
    else: # 이동할 시 격자 범위 벗어나지 않을 경우
        x, y = nx, ny
        # x, y = x + dxs[move_dir], y + dys[move_dir] # 해당 방향으로 한 칸 이동
        # (33줄에서 nx, ny에 한 칸 이동한 위치 선언했으므로, nx와 ny 값을 x, y에 대입만 해주면 됨)
        # i += 1 # 1초 흐름 (생략 가능)

print(x + 1, y + 1) # index가 0부터 시작하는 행, 열에서 좌표로 변환시 + 1 해주어야 함