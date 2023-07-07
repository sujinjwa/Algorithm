n = int(input()) # n = 격자의 크기

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 점(x, y)부터 시작해서 1,2,3,4의 방향으로 이동하면서 
# k만큼의 넓이, l만큼의 높이 가지는 직사각형 이루는 숫자들의 합 구하기
def get_sum(x, y, k, l):
              # 1, 2, 3, 4의 방향 순서대로 x, y축 이동
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l] # k = 기울어진 직사각형의 넓이, l = 높이
    sum_nums = 0
    nx, ny = x, y # 기울어진 직사각형의 시작점 (x, y)으로 nx, ny 초기화
    
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num): # move_num 만큼 해당 방향(dx, dy)으로 이동
            nx, ny = nx + dx, ny + dy

            if not in_range(nx, ny): # 직사각형이 격자 범위 벗어나면
                return 0
        
            sum_nums += grid[nx][ny] # 직사각형 이루는 숫자들의 합 구하기

    return sum_nums

ans = 0
# 기울어진 직사각형 만들기 위한 모든 시작점 (x, y)
for x in range(2, n): # 행은 index=2부터 조회
    for y in range(1, n - 1): # 열은 index=1부터 조회
        
        # k = width
        # l = height
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_sum(x, y, k, l))

print(ans)