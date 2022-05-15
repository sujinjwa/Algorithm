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
        if strings[curx][cury] == 'L': # 만약 조회한 칸에 'L'이 있다면
            # 8개의 방향으로 나아가며 'LEE'인지 확인하는 반복문
            for dx, dy in zip(dxs, dys):
                curt = 1 # curt == 3 일 경우 'LEE'임을 증명 / L이면 curt == 1, 그 뒤에 E 나오면 curt == 2, 또 E 나오면 curt == 3
                curx = i # 현재 행 번호
                cury = j # 현재 열 번호    

                while True:
                    nx = curx + dx
                    ny = cury + dy

                    if in_range(nx, ny) == False:
                        break
                    if strings[nx][ny] != 'E':
                        break
                        
                    curt += 1 # 해당 위치에 문자 'E' 있다는 의미
                    curx = nx # 이동한 위치로 curx 재선언
                    cury = ny # 이동한 열 번호로 cury 재선언

                if curt >= 3: # 'LEE'일 경우
                    cnt += 1

print(cnt)