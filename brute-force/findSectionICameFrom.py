OFFSET = 100
MAX_R = 200

# 2차원 배열 초기화
## 주의!
# 범위는 (MAX_R + 1) 이어야 함 : -100~1까지 100개, 1~100까지 100개, 0 1개 -> 201개
n = int(input())
checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for _ in range(n):
    # (x1, y1), (x2, y2) 입력
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    # OFFSET 더해주기
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    # 직사각형 범위 내 1 더하기 (직사각형 칠해주기)
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] += 1

# 모든 직사각형의 넓이
area = 0

for row in checked:
    for elem in row:
        if elem >= 1:
            area += 1

print(area)