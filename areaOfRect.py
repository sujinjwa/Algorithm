n = int(input()) # 점의 개수
# n개의 각 점의 위치 (x, y) 공백 두고 입력 받기
dots = [
    list(map(int, input().split()))
    for _ in range(n)
]

INT_X, INT_Y = 0, 0 # x축, y축 최댓값 나타내는 변수 0으로 초기화
for i in range(n): # 입력 받은 좌표 중 최댓값인 x좌표와 y좌표 구하기 위한 반복문
    INT_X = max(INT_X, dots[i][0])
    INT_Y = max(INT_Y, dots[i][1])

min_area = INT_X * INT_Y # 주어진 좌표들 기준 직사각형 넓이 최대일 때로 초기화

for i in range(n):
    min_x, max_x = INT_X , 0
    min_y, max_y = INT_Y, 0

    # i번째 점 제외한 모든 점들의 최소,최대 x,y좌표 구하기 위한 반복문
    for j in range(n):
        if j == i: # i번째 점 제외
            continue
        
        min_x = min(min_x, dots[j][0])
        max_x = max(max_x, dots[j][0])
        min_y = min(min_y, dots[j][1])
        max_y = max(max_y, dots[j][1])

    # 넓이 구하기
    area = (max_x - min_x) * (max_y - min_y)
    min_area = min(min_area, area)

print(min_area)