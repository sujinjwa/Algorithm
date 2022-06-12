OFFSET = 1000 # 10 * 100 (오, 왼 최대 경로)
MAX_R = 2000 # 오 왼 합친 최대 경로

n = int(input()) # 명령의 개수 : n번
segments = []

# 현재 위치
cur = 0

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        # 왼쪽으로 이동할 경우 : cur - distance ~ cur까지 경로 이동
        section_left = cur - distance
        section_right = cur
        cur -= distance
    
    else:
        # 오른쪽으로 이동할 경우 : cur ~ cur + distance까지 경로 이동
        section_left = cur
        section_right = cur + distance
        cur += distance
    
    segments.append([section_left, section_right])

checked = [0] * (MAX_R + 1)

for x1, x2 in segments:
    # OFFSET 더해준다
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    # 구간 칠해준다
    # 구간 단위로 진행하는 문제이므로
    # x2에 등호가 들어가지 않음에 유의한다
    for i in range(x1, x2):
        checked[i] += 1

# 2번 이상 지나간 영역의 크기 구한다
cnt = 0
for elem in checked:
    if elem >= 2:
        cnt += 1
print(cnt)