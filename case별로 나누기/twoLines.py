# 두 선분의 위치 : 각각 (x1, x2), (x3, x4)
x1, x2, x3, x4 = tuple(map(int, input().split()))

# 1. 안 겹치는 경우를 생각하기
if x2 < x3 or x4 < x1:
    print("nonintersecting")
else:
    print("intersecting")