n, t = list(map(int, input().split())) # 삼각형 각 변에 위치한 숫자 개수: n개, 총 흐른 시간: t초

# 삼각형의 왼쪽 위 변, 오른쪽 위 변, 아래 변에 위치한 n개의 숫자들 입력 받기
side1 = list(map(int, input().split()))
side2 = list(map(int, input().split()))
side3 = list(map(int, input().split()))

# t초 동안 1초마다 숫자 이동
for _ in range(t):
    
    temp1 = side1[n - 1]
    temp2 = side2[n - 1]
    temp3 = side3[n - 1]

    for i in range(n - 1, 0, -1):
        side1[i] = side1[i - 1]
        side2[i] = side2[i - 1]
        side3[i] = side3[i - 1]
    
    side1[0] = temp3
    side2[0] = temp1
    side3[0] = temp2

# t초 후 삼각형 컨베이어 벨트 숫자 위치 출력
for elem in side1:
    print(elem, end=' ')

print()

for elem in side2:
    print(elem, end=' ')

print()

for elem in side3:
    print(elem, end=' ')