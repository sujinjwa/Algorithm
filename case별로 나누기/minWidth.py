# 두 직사각형 양쪽 두 점의 좌표 입력 받기
x1, y1, x2, y2 = tuple(map(int, input().split())) # 두 개의 점 좌표
a1, b1, a2, b2 = tuple(map(int, input().split())) # 두 개의 점 좌표

# 두 직사각형 포함할 수 있는 직사각형 최소 넓이
ans = (max(a2, x2) - min(x1, a1)) * (max(b2, y2) - min(y1, b1))
print(ans)