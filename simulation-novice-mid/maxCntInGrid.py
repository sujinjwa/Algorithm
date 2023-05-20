n = int(input()) # n : 격자의 크기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0 # 최대 동전의 수

# row와 col 로 모든 3 * 3 격자의 좌측 상단 index 조회
for row in range(n-2):
    for col in range(n-2):

        cnt = 0 # 동전의 개수

        # 모든 3 * 3 격자의 좌측 상단 인덱스부터 row 아래로 3칸, column 오른쪽으로 3칸칸. 
        # 총 9칸 한칸씩 모두 조회
        for x in range(row, row+3):
            for y in range(col, col+3):
                if grid[x][y] == 1: # 동전 있는 경우
                    cnt += 1
        
        max_cnt = max(max_cnt, cnt)

print(max_cnt)