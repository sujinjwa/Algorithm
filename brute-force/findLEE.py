n, m = tuple(map(int, input().split())) # 문자열 개수 n, 문자열 길이 m

# m 길이의 문자열 n개 입력 받기
strings = [
    input()
    for _ in range(n)
]

#          북  북동 동 동남 남 남서 서 서북
dxs, dys = [-1, -1, 0,  1,  1,  1, 0,  -1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y): # (x, y)가 주어진 행렬에 벗어나는지 확인
    return 0 <= x and x < n and 0 <= y and y < m

cnt = 0 # 'LEE'의 개수
# n * m 크기의 문자열 행렬의 모든 칸 조회하는 반복문
for i in range(n):
    for j in range(m):
        curx = i # 현재 행 번호
        cury = j # 현재 열 번호
        if strings[curx][cury] == 'L': # 만약 조회한 칸에 'L'이 있다면
            # 8개의 방향으로 나아가며 'LEE'인지 확인하는 반복문
            for dx, dy in zip(dxs, dys):
                # 해당 방향으로 2칸 이동하는 반복문
                for k in range(1, 3):
                    nx, ny = curx + dx * k, cury + dy * k # 해당 방향으로 k칸 나아간 위치
                    
                    if in_range(nx, ny) == False: # 격자를 벗어났을 경우
                        break
                    
                    if strings[nx][ny] != 'E': # 해당 위치의 문자가 'E'가 아닐 경우
                        break
                    
                    if k == 2: # 만약 k==1, k==2 일 때 모두 범위를 벗어나지 않으며 문자가 'E'라면
                        cnt += 1

print(cnt)