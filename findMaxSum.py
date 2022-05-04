n = int(input()) # 격자의 크기 n 입력 받기
# 0 또는 1로 이루어진 n * n 크기의 격자 입력 받기
grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_num = 0 # 1 * 3 크기의 격자 범위 내 최대 동전의 개수

# i := 행, j := 열

sum_num = 0 # 모든 1 * 3 크기의 격자 범위 내 동전의 개수
for i in range(n):
    for j in range(n-2):
        sum_num = grid[i][j] + grid[i][j+1] + grid[i][j+2]
    
        max_num = max(max_num, sum_num)

print(max_num)