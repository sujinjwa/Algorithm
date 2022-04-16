OFFSET = 100
MAX_R = 200

# 색종이 갯수
n = int(input())

# n개의 색종이 좌측하단 꼭짓점 입력
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 2차원 좌표평면 선언
checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for x, y in rects:
    # OFFSET 더하기
    x, y = x + OFFSET, y + OFFSET

    # 직사각형 칠하기
    for i in range(x, x+8):
        for j in range(y, y+8):
            checked[i][j] += 1

# 모든 정사각형 색종이의 총 넓이
area = 0
for row in checked:
    for elem in row:
        if elem >= 1:
            area += 1

print(area)