# 코드트리 > intermediate-low > 백트래킹 > '강력한 폭발' 문제

# 문제 링크 : https://www.codetree.ai/missions/2/problems/strong-explosion?utm_source=clipboard&utm_medium=text

# M : 폭탄이 놓일 수 있는 위치의 개수
# N : 격자의 크기

# 시간 복잡도 : O(3^M * N^2)
# => 3개의 종류의 폭탄이 M개의 위치에 놓이는 모든 경우의 수 구하므로 3^M이고,
#   해당 경우마다 N*N 크기의 2차원 배열 temp를 조회하니까 N^2를 곱해줘야 함

# 공간 복잡도 : N^2 + M = O(N^2)



n = int(input()) # n : 격자의 크기

# grid : 각 칸이 0, 1로 이루어진 2차원 격자
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 폭탄 유형별 터지는 위치를 dx, dy로 표기
# 3가지 폭탄을 가지고 특정 위치에 놓이는 모든 경우 구하고 
# 그때의 초토화되는 지역의 개수도 구하기
bombs = [[(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0)],
         [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)],
         [(0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]]


able_regions = []
# grid 하나씩 조회하면서 폭탄 놓을 수 있는 위치의 row, col 저장해두기
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            able_regions.append((row, col))

# selected_bombs : 각 지역별 놓이는 폭탄을 저장하는 배열
# selected_bombs의 인덱스 = able_regions에서 동일한 인덱스의 region
selected_bombs = []

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 현재까지 놓인 폭탄들로 초토화시킨 영역의 개수 구하는 함수
def count_ans():
    # temp : 폭탄으로 인해 초토화되는 칸의 수 구하기 위한 grid와 동일한 크기의 2차원 배열
    temp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for bomb, region in zip(selected_bombs, able_regions):
        r1, r2 = region # 폭탄 놓이게 될 위치
        
        # 해당 종류의 폭탄이 영향 미칠 수 있는 거리의 영역 구하기
        for b1, b2 in bombs[bomb]:
            nx, ny = r1 + b1, r2 + b2 # (nx, ny): 폭탄 터지는 곳
            
            if in_range(nx, ny): # 격자 벗어나는지 확인
                temp[nx][ny] = 1
    
    # temp에 1인 영역의 수 구하기 = 초토화된 지역의 수
    cnt = 0
    for row in temp:
        for elem in row:
            if elem == 1:
                cnt += 1
                
    return cnt

        
ans = 0
# 현재 위치(curr_region)에 놓일 폭탄(i) 고르는 함수
def choose(curr_region):
    global ans

    if curr_region == len(able_regions):
        ans = max(ans, count_ans())
        return
    
    for i in range(3):
        selected_bombs.append(i)
        choose(curr_region + 1)
        selected_bombs.pop()
    

choose(0)

# 초토화된 지역의 수가 최대일 때의 값 출력
print(ans)