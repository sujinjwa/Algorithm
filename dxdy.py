n = int(input())
infos = [
    list(input().split()) # n개의 줄에 걸쳐 이동 방향과 이동 거리 입력 받기
    for _ in range(n)
]

#     북  동 남  서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
directions = ['N', 'E', 'S', 'W']

x, y = 0, 0 # 초기 좌표 위치
for direction, distance in infos:
    distance = int(distance)

    # 동서남북 중 해당 방향 찾아서 distance 만큼 이동
    for i in range(4):
        if direction == directions[i]:
            x, y = x + dxs[i] * distance, y + dys[i] * distance

print(x, y) # 최종 위치 출력