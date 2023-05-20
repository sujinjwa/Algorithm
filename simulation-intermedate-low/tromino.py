n, m = tuple(map(int, input().split())) # n : 영역의 가로 크기, m : 영역의 세로 크기

# n * m 크기의 이차원 영역 내 각 위치에 주어진 자연수 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# (x, y) 칸이 n * m 크기의 이차원 영역을 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

max_num = 0 # 3칸의 블럭 내 숫자들의 최대 합

# n * m 크기의 영역 한 칸씩 조회
for i in range(n):
    for j in range(m):

        # 1) 3칸으로 이루어진 'ㄴ'자 블럭 내 숫자의 최대 합 구하기
        dxs1, dys1 = [0, 0, 1, 1], [0, 1, 1, 0] # dxs1, dys1 : 'ㄴ'자 모양의 블럭 회전하거나 뒤집은 4가지 모양 만들기 위한 방향
        num = 0 # num : 블럭 놓인 칸 안의 숫자들의 합
        not_in_range = False

        #  블럭이 놓일 수 있는 모든 경우 확인
        for dx, dy in zip(dxs1, dys1):
            if not in_range(i + dx, j + dy):
                not_in_range = True
                break
            else:
                # 격자 벗어나지 않는다면 블럭이 놓인 칸 안의 숫자 더하기
                num += grid[i + dx][j + dy]

        if not not_in_range:
            # dxs1, dys1 로 조회한 4개의 칸 중 하나씩 제외하여
            # 'ㄴ'자 모양의 블럭 내 숫자들의 합 중 최대값 구하기
            max_num = max(max_num, num - grid[i + dxs1[0]][j + dys1[0]], num - grid[i + dxs1[1]][j + dys1[1]], num - grid[i + dxs1[2]][j + dys1[2]], num - grid[i + dxs1[3]][j + dys1[3]])

        # 2) 3칸으로 이루어진 'ㅡ' 또는 '|'자 블럭 내 숫자의 최대 합 구하기 
        dxs2, dys2 = [0, 0, 0], [0, 1, 2]
        num1, num2 = 0, 0

        # 'ㅡ'자 모양의 블럭 내 숫자들의 합 구하기
        for dx, dy in zip(dxs2, dys2):
            if not in_range(i + dx, j + dy):
                break
            else:
                num1 += grid[i + dx][j + dy]
        
        # '|'자 모양의 블럭 내 숫자들의 합 구하기
        for dx, dy in zip(dxs2, dys2):
            if not in_range(i + dy, j + dx):
                break
            else:
                num2 += grid[i + dy][j + dx]
        
        # 숫자들의 최대 합 갱신
        max_num = max(max_num, num1, num2)

# 총 최대 합 출력
print(max_num)