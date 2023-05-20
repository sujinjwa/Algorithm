grid = [
    list(input())
    for _ in range(10)
]

# L, B, R 위치 찾기
Lx, Ly, Rx, Ry, Bx, By = 0, 0, 0, 0, 0, 0
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'L':
            Lx, Ly = i, j
        
        if grid[i][j] == 'R':
            Rx, Ry = i, j
        
        if grid[i][j] == 'B':
            Bx, By = i, j

# Case 1: L과 B가 일직선 상에 있지 않은 경우
if Lx != Bx and Ly != By:
    print(abs(Lx - Bx) + abs(Ly - By) - 1)

# Case 2: L과 B가 세로로 일직선 상에 있는 경우
if Lx != Bx and Ly == By:
    if Ry == Ly and min(Lx, Bx) < Rx and max(Lx, Bx) > Rx: # 만약 R이 일직선 상에 함께 있는 경우
        # 2칸 +
        print(abs(Lx - Bx) - 1 + 2)
    else:
        print(abs(Lx - Bx) - 1)

# Case 3: L과 B가 가로로 일직선 상에 있는 경우
if Lx == Bx and Ly != By:
    if Rx == Lx and min(Ly, By) < Ry and max(Ly, By) > Ry:
        print(abs(Ly - By) - 1 + 2)
    else:
        print(abs(Ly - By) - 1)