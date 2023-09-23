# 코드트리 > intermediate-low > 시뮬레이션 > 단 한 번의 2048 시도 

# 문제 링크: https://www.codetree.ai/missions/2/problems/one-trial-of-2048-game/description

# 시간 복잡도 : O(N^2) (n = 격자 크기 = 4)

# 공간 복잡도 : O(N^2) (n = 격자 크기 = 4)

# grid : 4 * 4 크기의 grid의 각 칸에 위치하는 숫자 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(4)
]

# dir_str : 움직일 방향(L, R, U, D)
dir_str = input()

# 시뮬레이션 절차
# 1. 입력 받은 방향으로 중력 작용
# 2. 바닥부터 조회하면서 같은 숫자 2개가 만나는 경우 합쳐주기
#    - 합쳐줄 때 바닥에 가까운 칸에 두 숫자의 합 입력, 다른 칸에는 0 입력
#    - 합친 후 다음 값부터 조회하면서 같은 동작을 끝날 때까지 반복
# 3. 마지막으로 중간에 0 있는 곳 바닥 쪽으로 댕겨주기

# 각 입력값(L, R, U, D) 별 행(row)과 열(col)의 변화 과정
# L: row: 0~4 별 col: 0~4
# R: row: 0~4 별 col: 3~-1
# U: col: 0~4 별 row: 0~4
# D: col: 0~4 별 row: 3~-1

# L: row: 0~4 별 col: 0~4
if dir_str == 'L':
    for i in range(4):
        # 1. 입력 받은 방향으로 중력 작용
        temp = []
        for j in range(4):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
        
        for j in range(4):
            if j >= len(temp):
                grid[i][j] = 0
            else:
                grid[i][j] = temp[j]
        
        # 2. 왼쪽부터 조회하면서 같은 숫자 2개가 만나는 경우 합치기
        for j in range(3):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] = grid[i][j] + grid[i][j + 1]
                grid[i][j + 1] = 0
        
        # 3. 마지막으로 각 row에서 중간에 0 있는 곳 없도록 왼쪽으로 땡겨주기
        temp = []
        for j in range(4):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
            
        for j in range(4):
            if j >= len(temp):
                grid[i][j] = 0
            else:
                grid[i][j] = temp[j]


# R: row: 0~4 별 col: 3~-1
elif dir_str == 'R':
    for i in range(4):
        # 1. 입력 받은 방향으로 중력 작용
        temp = []
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
        
        for _ in range(4 - len(temp)):
            temp.append(0)
        
        temp.reverse()
        
        for j in range(3, -1, -1):
            grid[i][j] = temp[j]
        
        # 2. 오른쪽부터 조회하면서 같은 숫자 2개가 만나는 경우 합치기
        for j in range(3, 0, -1):
            if grid[i][j] == grid[i][j - 1]:
                grid[i][j] = grid[i][j] + grid[i][j - 1]
                grid[i][j - 1] = 0
        
        # 3. 마지막으로 각 row에서 중간에 0 있는 곳 없도록 오른쪽으로 땡겨주기
        temp = []
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
            
        for _ in range(4 - len(temp)):
            temp.append(0)
        
        temp.reverse()
        
        for j in range(3, -1, -1):
            grid[i][j] = temp[j]

# U: col: 0~4 별 row: 0~4
elif dir_str == 'U':
    for j in range(4):
        # 1. 입력 받은 방향으로 중력 작용
        temp = []
        for i in range(4):
            if grid[i][j] != 0:
                temp.append(grid[i][j])

        for i in range(4):
            if i >= len(temp):
                grid[i][j] = 0
            else:
                grid[i][j] = temp[i]
        
        # 2. 위부터 조회하면서 같은 숫자 2개가 만나는 경우 합치기
        for i in range(3):
            if grid[i][j] == grid[i + 1][j]:
                grid[i][j] = grid[i][j] + grid[i + 1][j]
                grid[i + 1][j] = 0
        
        # 3. 마지막으로 각 column의 중간에 0 있는 곳 없도록 위쪽으로 땡겨주기
        temp = []
        for i in range(4):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
            
        for i in range(4):
            if i >= len(temp):
                grid[i][j] = 0
            else:
                grid[i][j] = temp[i]


# D: col: 0~4 별 row: 3~-1
else:
    for j in range(4):
        # 1. 입력 받은 방향으로 중력 작용
        temp = []
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
        
        for _ in range(4 - len(temp)):
            temp.append(0)
        
        temp.reverse()
        
        for i in range(3, -1, -1):
            grid[i][j] = temp[i]
        
        # 2. 바닥부터 조회하면서 같은 숫자 2개가 만나는 경우 합치기
        for i in range(3, 0, -1):
            if grid[i][j] == grid[i - 1][j]:
                grid[i][j] = grid[i][j] + grid[i - 1][j]
                grid[i - 1][j] = 0
        
        # 3. 마지막으로 각 column의 중간에 0 있는 곳 없도록 바닥 쪽으로 댕겨주기
        temp = []
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
            
        for _ in range(4 - len(temp)):
            temp.append(0)
        
        temp.reverse()
        
        for i in range(3, -1, -1):
            grid[i][j] = temp[i]


# 출력
for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()