n, t = tuple(map(int, input().split())) # n : 컨베이어 벨트 길이, t : 흐른 시간

# 2 * n 개의 숫자로 이루어진 두 줄의 컨베이어 벨트 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(2)
]

for _ in range(t):
    # 상위 또는 하위 벨트로 이동해야 하는 마지막 칸의 숫자 temp1, temp2 변수에 임시 저장
    temp1, temp2 = grid[0][-1], grid[1][-1]
    
    # # 위 아래 각 벨트의 숫자들을 오른쪽으로 한 칸씩 이동
    for i in range(n - 1, 0, -1):
        grid[0][i] = grid[0][i - 1]
    
    for j in range(n - 1, 0, -1):
        grid[1][j] = grid[1][j - 1]
    
    grid[0][0], grid[1][0] = temp2, temp1

# t초 후 벨트에 놓여있는 숫자들의 상태 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()