OFFSET = 1000
MAX_R = 2000

# 2000 * 2000 좌표 0으로 채우기
arr = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

# 두 개의 직사각형 좌측하단 좌표와 우측하단 좌표 입력
rects = [
    tuple(map(int, input().split()))
    for _ in range(2)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    # OFFSET 더하기
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    # 첫번째 직사각형은 1로 채우고,
    # 두번째 직사각형은 2로 채우기
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = i

# 아직 숫자 1로 남아있는 곳들 중 최대 최소 x, y 값을 전부 계산
min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if arr[i][j] == 1:
            first_rect_exist = True
            min_x = min(i, min_x)
            max_x = max(i, max_x)
            min_y = min(j, min_y)
            max_y = max(j, max_y)

if not first_rect_exist:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)