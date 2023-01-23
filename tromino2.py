n, m = tuple(map(int, input().split())) # n : 영역의 가로 크기, m : 영역의 세로 크기

# n * m 크기의 이차원 영역 내 각 위치에 주어진 자연수 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 가능한 모든 모양을 적어준다
shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]]
]

# (x, y) 위치가 격자를 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 1) 내가 작성한 버전
# shapes 내에 선언한 6개의 블럭 모양의 각 첫 번째 칸이 (i, j)칸일 때 
# 각 블럭이 격자를 벗어나지 않는다면 블럭 안에 적힌 숫자의 합 구하기
def find_max_sum(i, j):
    max_sum = 0
    
    # 6개의 블럭 모양 순회
    for shape in shapes:
        sum_of_nums = 0 # 블럭 안에 적힌 숫자의 합

        # 각 블럭의 한 칸씩 순회
        for k in range(3):
            is_not_in_range = False
            for l in range(3):
                # 해당 블럭의 칸에 적힌 숫자가 1인 곳이 격자 벗어나지 않는지 확인
                if shape[k][l] == 1 and not in_range(i + k, j + l):
                    is_not_in_range = True
                    break
                
                # 격자를 벗어나지 않는 경우에만 해당 칸의 숫자 더하기
                if shape[k][l] == 1 and in_range(i + k, j + l):
                    sum_of_nums += grid[i + k][j + l]
            
            # 해당 블럭이 격자를 벗어나는 경우 순회를 종료하고 다음 블럭 확인
            if is_not_in_range:
                break
                
        # 해당 블럭에서 3개의 1이 적힌 각 칸의 숫자의 최대 합 갱신
        max_sum = max(max_sum, sum_of_nums)
    
    return max_sum

# 2) 해설 버전
# 주어진 위치(x, y)에 대하여 가능한 모든 모양(shapes[i]) 탐색하며 최대 합 반환
def find_max_sum2(x, y):
    max_sum = 0
    for i in range(6):
        is_possible = True
        sum_of_nums = 0
        for dx in range(0, 3):
            for dy in range(0, 3):
                # 블럭 내에 있는 칸이 아닌 경우
                if shapes[i][dx][dy] == 0:
                    continue
                
                # 해당 칸이 격자를 벗어나는 경우
                if x + dx >= n or y + dy >= m:
                    is_possible = False
                
                else:
                    sum_of_nums += grid[x + dx][y + dy]
        
        if is_possible:
            max_sum = max(max_sum, sum_of_nums)

    return max_sum

max_sum = 0

# n * m 크기의 grid의 각 칸 탐색
for i in range(n):
    for j in range(m):
        
        max_sum = max(max_sum, find_max_sum(i, j))

# 숫자의 합이 최대일 때의 결과 출력
print(max_sum)