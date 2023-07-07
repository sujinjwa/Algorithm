import sys

# n : 행 크기, m : 열 크기
n, m = list(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 서로 겹치지 않는
# 두 개의 직사각형. 꼭 두 개여야 함. 기울어지지 않아야 함.
# 숫자들의 총 합이 최대

# x1, y1, w1, h1 = 첫번째 직사각형의 왼쪽 상단 위치, 넓이, 높이
# x2, y2, w2, h2 = 두번째 직사각형의 왼쪽 상단 위치, 넓이, 높이


# 점(x, y)가 격자 벗어나지 않는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 두 직사각형 겹치는지 확인
def is_overlapped(x1, y1, w1, h1, x2, y2, w2, h2):
    # 1. 두 직사각형 겹치는지 확인하는 첫번째 방법
    # 한 직사각형의 오른쪽 하단과 다른 직사각형의 왼쪽 상단이 겹치거나
    # 또는 한 직사각형의 오른쪽 상단과 다른 직사각형의 왼쪽 하단이 겹치거나
    # 왼쪽 하단과 오른쪽 상단이 겹치거나
    # 왼쪽 상단과 오른쪽 하단이 겹치거나

    # 두 직사각형의 왼쪽 상단 위치가 같을 때
    # if x1 == x2 and y1 == y2:
    #     return True
    
    # # (x1, y1)이 (x2, y2)의 왼쪽에 위치할 때
    # elif y1 < y2:
    #     if y1 + w1 - 1 >= y2 and x1 + h1 - 1 >= x2:
    #         return True
    
    #     if y1 + w1 - 1 >= y2 and x1 <= x2 + h2 - 1:
    #         return True
    
    # # (x1, y1)이 (x2, y2)의 오른쪽에 위치할 때
    # else:
    #     if y2 + w2 - 1 >= y1 and x2 + h2 - 1 >= x1:
    #         return True
    
    #     if y2 + w2 -1 >= y1 and x2 <= x1 + h1- 1:
    #         return True

    # 2. 두 직사각형 겹치는지 확인하는 두번째 방법
    # 새로운 격자 visited에 각 직사각형 영역마다 1씩 더해주고
    # 숫자가 2 이상인 칸 있는지 확인
    visited = [
        [0] * m
        for _ in range(n)
    ]

    for i in range(h1):
        rx = x1 + i
        for j in range(w1):
            ry = y1 + j
            if not in_range(rx, ry):
                return True

            visited[rx][ry] += 1
    
    for i in range(h2):
        rx = x2 + i
        for j in range(w2):
            ry = y2 + j
            
            if not in_range(rx, ry):
                return True
            
            visited[rx][ry] += 1

    for row in visited:
        for elem in row:
            if elem >= 2:
                return True
    
    return False


# 직사각형 2개의 최대합 구하기
def get_sum(x1, y1, w1, h1, x2, y2, w2, h2):

    sum_of_nums = 0
    # x1, y1부터 시작해서 오른쪽으로 w1만큼 아래로 h1만큼 모든 숫자 더하기
    # 어떻게 더하지?
    # 아래로 h1만큼 이동하면서 한칸씩 이동할 때마다 오른쪽으로 w1만큼 이동해서 숫자 더하기
    for i in range(h1):
        rx = x1 + i
        for j in range(w1):
            ry = y1 + j
            
            # if not in_range(x1, y1):
            #     return -sys.maxsize
            
            sum_of_nums += grid[rx][ry]
    
    for i in range(h2):
        rx = x2 + i
        for j in range(w2):
            ry = y2 + j
            
            # if not in_range(x2, y2):
            #     return -sys.maxsize

            sum_of_nums += grid[rx][ry]
    
    return sum_of_nums
    

# 점(x1, y1)를 맨 왼쪽 상단 위치로 가지며 넓이가 w1, 높이가 h1인 직사각형 한 개와
# 점(x2, y2)를 맨 왼쪽 상단 위치로 가지며 넓이가 w2, 높이가 h2인 직사각형 한 개가
# 서로 겹치지 않는 경우 최대값 구하기
ans = -sys.maxsize
for x1 in range(n):
    for y1 in range(m):
        for w1 in range(1, m+1):
            for h1 in range(1, n+1):
                for x2 in range(n):
                    for y2 in range(m):
                        for w2 in range(1, m+1):
                            for h2 in range(1, n+1):
                                if not is_overlapped(x1, y1, w1, h1, x2, y2, w2, h2):
                                    ans = max(ans, get_sum(x1, y1, w1, h1, x2, y2, w2, h2))

print(ans)