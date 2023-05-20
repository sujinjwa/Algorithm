n = int(input())  # 점의 개수 : n개
# n개의 줄에 걸쳐 각 점의 위치 공백을 사이에 두고 입력 받기
points = [
    list(map(int, input().split()))
    for _ in range(n)
]

def parallelToX(i, j, k):  # 3개의 점 중 x축과 같은 거리에 위치한 두 점 있는지 확인
    return x1 == x2 or x2 == x3 or x3 == x1

def parallelToY(i, j, k):  # 3개의 점 중 y축과 같은 거리에 위치한 두 점 있는지 확인
    return y1 == y2 or y2 == y3 or y3 == y1


max_ans = 0  # 최대 넓이 0으로 초기화
for i in range(n):  # i, j, k번째 점의 모든 경우 순회하는 반복문
    for j in range(i+1, n):
        for k in range(j+1, n):

            # i번째 점의 좌표 : (x1, y1)
            # j번째 점의 좌표 : (x2, y2)
            # k번째 점의 좌표 : (x3, y3)

            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            x3 = points[k][0]
            y3 = points[k][1]

            if parallelToX(x1, x2, x3) and parallelToY(y1, y2, y3):  # 해당 삼각형의 한 면은 x축에 평행하며, 다른 한 면은 y축에 평행한 경우
                ans = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) / 2  # 세 점 (x1, y1), (x2, y2), (x3, y3)로 이루어진 삼각형의 넓이
                max_ans = max(max_ans, ans)

print(int(max_ans * 2))  # 최대 넓이에 2 곱한 값 출력