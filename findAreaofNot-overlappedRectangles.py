OFFSET = 1000
MAX_R = 2000

# 직사각형 A,B,M의 좌측 최하단 좌표 (x1, y1), 우측 최상단 좌표 (x2, y2) 입력
rects = [
    tuple(map(int, input().split()))
    for _ in range(3)
]

# 2차원 공간
arr = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    
    # OFFSET 더하기
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    # 직사각형 각 A,B,M 칠하기
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = i

# M으로 덮이지 못한 직사각형 A,B의 총 넓이
area = 0

for row in arr:
    for elem in row:
        if elem == 1 or elem == 2:
            area += 1

print(area)