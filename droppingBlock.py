n, m, k = list(map(int, input().split()))
# n : 격자의 크기, m : 블록의 크기, k : 블록 떨어질 위치(열) 정보
k = k - 1 # 입력받은 행을 실제 배열의 인덱스 값으로 변경

# n 개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

row_blockIn = -1 # 새로운 블럭이 위치할 행

is_true = False
for i in range(n): # i : 조회할 행 위치 / 0 ~ n
    for j in range(k, k + m): # j : 조회할 열(블록 크기) / k ~ k + m - 1
        
        if grid[i][j] == 1: # 해당 칸에 블럭이 있다면
            row_blockIn = i - 1 # 아래로 내려갈 새로운 블럭이 위치할 행
            is_true = True
            break
    if is_true:
        break

# 새로운 블럭 위치시키기
for i in range(k, k + m):
    grid[row_blockIn][i] = 1

# 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()