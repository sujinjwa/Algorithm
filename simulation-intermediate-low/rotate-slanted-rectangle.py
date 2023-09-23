from collections import deque

n = int(input()) # n : 격자의 크기

# n * n 크기의 격자 정보 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# (r, c) : 기울어진 직사각형 시작점
# m1, m2, m3, m4 : 각 1~4번 방향으로 이동한 거리
# direc : 0이면 반시계 방향, 1이면 시계 방향
r, c, m1, m2, m3, m4, direc = list(map(int, input().split()))

r, c = r - 1, c - 1

# m1, m2, m3, m4 방향에 따라 x, y 칸의 변화
dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
dirs = [m1, m2, m3, m4]

arr = deque()

# 1. (r, c)부터 시작해서 m1, m2, m3, m4 에 위치한 숫자들을 차례로 arr에 추가
nx, ny = r, c
arr.append(grid[nx][ny])
for dx, dy, d in zip(dxs, dys, dirs):
    for _ in range(d):
        nx, ny = nx + dx, ny + dy

        if nx == r and ny == c:
            break

        arr.append(grid[nx][ny])

# 2. arr(예: [2, 3, 4, 2, 3, 1]) 알맞게 변환 
# 반시계 방향이면 arr = [1, 2, 3, 4, 2, 3]로 변환 (마지막 원소를 맨 앞으로)
# 시계 방향이면 arr = [3, 4, 2, 3, 1, 2]로 변환 (맨 앞 원소를 맨 뒤로)
if direc: # 시계 방향
    tmp = arr.popleft()
    arr.append(tmp)
else: # 반시계 방향
    tmp = arr.pop()
    arr.appendleft(tmp)


# 3. m1, m2, m3, m4 방향대로 변경된 arr 요소로 업데이트
nx, ny = r, c
grid[nx][ny] = arr[0]
index = 0
for dx, dy, d in zip(dxs, dys, dirs):
    for _ in range(d):
        index += 1
        nx, ny = nx + dx, ny + dy

        if nx == r and ny == c:
            break

        grid[nx][ny] = arr[index]


# 회전 이후의 결과 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()