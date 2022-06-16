n = int(input()) # 선분의 개수 : n개
# n개의 줄에 걸쳐 선분 (x1, x2)의 정보 입력
lines = [
    list(map(int, input().split()))
    for _ in range(n)
]

area = [0] * 101 # 모든 선분에게 정해진 범위 1 <= x1 <= x2 <= 100

for line in lines:
    # 입력 받은 각 선분의 구간에
    # + 1 로 색칠
    x1, x2 = line[0], line[1]
    for i in range(x1, x2 + 1):
        area[i] += 1

interSect = False # 모든 선분이 겹치는지 확인하기 위한 변수

for elem in area:
    # 모든 선분의 구간이 색칠된 area 배열에서
    # 모든 선분이 겹치는 지점 있다면 True
    if elem == n:
        interSect = True

if interSect:
    print("Yes")
else:
    print("No")