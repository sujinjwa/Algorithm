# [코드트리] 1차원 바람 문제
# https://www.codetree.ai/missions/2/problems/The-1D-wind-blows/description


# n : 행 크기, m : 열 크기, q : 바람이 불어온 총 횟수
n, m, q = map(int, input().split())

# n * m 크기의 건물 상태 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# q개의 바람에 대한 정보 입력 받기 (r, d)
# r : 바람에 영향 받는 행 번호
# d : 바람 불어오는 방향 ('L' 또는 'R'의 값 가짐)
winds = [
    tuple(input().split())
    for _ in range(q)
]

for r, d in winds:
    # r행에 바람 불어 한칸씩 미뤄짐
    row = int(r) - 1
    if d == 'L': # 바람이 왼쪽에서 불어올 때 r행의 모든 원소들이 오른쪽으로 한 칸씩 shift
        tmp = grid[row][-1]
        for i in range(m-1, 0, -1):
            grid[row][i] = grid[row][i-1]
        grid[row][0] = tmp
    else: # 바람이 오른쪽에서 불어올 때 r행의 모든 원소들이 왼쪽으로 한 칸씩 shift
        tmp = grid[row][0]
        for i in range(m-1):
            grid[row][i] = grid[row][i+1]
        grid[row][-1] = tmp
    
    # r의 윗 행으로 전파
    # 1) 같은 열에 같은 숫자가 있는지 확인
    d1 = d
    for i in range(row-1, -1, -1):
        cnt = 0
        for j in range(m):
            if grid[i][j] == grid[i+1][j]:
                d1 = 'R' if d1 == 'L' else 'L' # 방향 전환 (l <-> R)
                if d1 == 'L':
                    tmp = grid[i][-1]
                    for k in range(m-1, 0, -1):
                        grid[i][k] = grid[i][k-1]
                    grid[i][0] = tmp
                else:
                    tmp = grid[i][0]
                    for k in range(m-1):
                        grid[i][k] = grid[i][k+1]
                    grid[i][-1] = tmp
                break
            else:
                cnt += 1
        
        if cnt == m: # 같은 열에 같은 숫자가 한 개도 없으면 이후 행에는 전파 확산 종료
            break
            
    d2 = d
    # r의 아랫 행으로 전파
    for i in range(row+1, n):
        cnt = 0
        for j in range(m):
            if grid[i][j] == grid[i-1][j]:
                d2 = 'R' if d2 == 'L' else 'L' # 방향 전환 (l <-> R)
                if d2 == 'L':
                    tmp = grid[i][-1]
                    for k in range(m-1, 0, -1):
                        grid[i][k] = grid[i][k-1]
                    grid[i][0] = tmp
                else:
                    tmp = grid[i][0]
                    for k in range(m-1):
                        grid[i][k] = grid[i][k+1]
                    grid[i][-1] = tmp
                break
            else:
                cnt += 1
        
        if cnt == m: # 같은 열에 같은 숫자가 한 개도 없으면 이후 행에는 전파 확산 종료
            break
    
# 시뮬레이션 종료 후 grid 상태 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()