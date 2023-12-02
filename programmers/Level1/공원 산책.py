# 공원 산책 문제, level 1
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    grid = [
        [p2 for p2 in p]
        for p in park
    ]
    
    W = len(grid[0]) # 공원 가로 길이
    H = len(grid) # 공원 세로 길이
    print(W, H)
    
    routes = [(r.split()[0], int(r.split()[1])) for r in routes]
    
    #     동  서  남  북
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    
    # 공원 벗어나느지 확인
    def in_range(x, y):
        return 0 <= x and x < H and 0 <= y and y < W
        
    print(grid)
    
    # 강아지는 S 위치에서 시작
    x, y = 0, 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                x, y = i, j
                break
    
    for dir, cnt in routes:
        dir2 = 0
        
        if dir == 'E': dir2 = 0
        elif dir == 'W': dir2 = 1
        elif dir == 'S': dir2 = 2
        else: dir2 = 3
        
        sx, sy = x, y
        for _ in range(cnt):
            nx, ny = x + dxs[dir2], y + dys[dir2]
            
            # 주어진 방향으로 이동 시 공원 벗어나는지 확인
            if not in_range(nx, ny):
                x, y = sx, sy
                break
            
            # 장애물 만나는지(칸의 숫자가 X 인지) 확인
            if grid[nx][ny] == 'X':
                x, y = sx, sy
                break
            
            x, y = nx, ny
                    
    answer = [x, y]
    return answer