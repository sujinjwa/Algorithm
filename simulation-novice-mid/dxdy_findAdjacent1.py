n = int(input()) # n : 격자의 크기
grid = [
    list(map(int, input().split())) # n개의 줄에 걸쳐 각 행 입력 받기
    for _ in range(n)
]

#     위 오른쪽 아래 왼쪽
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y): # 해당 격자 내에 위치하는지 확인
    return 0 <= x and x < n and 0 <= y and y < n

x, y = 0, 0 # 1행 1열에 위치하는 초기 좌표
ans = 0
for i in range(n): # grid의 전체 좌표 하나씩 조회하는 반복문
    for j in range(n):
        
        cnt = 0 # 인접한 칸 내 숫자 1 개수
        for k in range(4):
            # 상하좌우 칸의 index 확인하는 for문
            ax, ay = i + dxs[k], j + dys[k]

            # 격자 벗어나지 않으면서
            # 인접한 칸에 숫자 1 위치하는 경우
            if in_range(ax, ay) and grid[ax][ay] == 1:
                cnt += 1
        
        if cnt >= 3: # 인접한 칸 중 숫자 1 적혀 있는 칸의 수가 3개 이상이라면
            ans += 1

print(ans) # 해당 조건 만족하는 칸의 개수 출력