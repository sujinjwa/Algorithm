answer = 0

def solution(m, n, board):
    
    for i in range(m):
        board[i] = list(board[i])
    
    temp = [
        [False for _ in range(n)]
        for _ in range(m)
    ]
    
    dxs, dys = [0, 0, 1, 1], [0, 1, 1, 0]
    
    def in_range(x, y):
        return 0 <= x and x < m and 0 <= y and y < n
    
    def four_same(i, j):
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            
            if not in_range(nx, ny) or board[i][j] != board[nx][ny]:
                return False
        
        return True
    
    def find():
        for i in range(m):
            for j in range(n):
                if board[i][j] != '' and four_same(i, j):
                    for dx, dy in zip(dxs, dys):
                        nx, ny = i + dx, j + dy
                        
                        temp[nx][ny] = True
    
    def erase():
        cnt = 0
        for i in range(m):
            for j in range(n):
                if temp[i][j]:
                    board[i][j] = ''
                    cnt += 1
        
        return cnt
    
    def fall_down():
        temp2 = [
            ['' for _ in range(n)]
            for _ in range(m)
        ]
        
        for i in range(n):
            index = m - 1
            for j in range(m - 1, -1, -1):
                if board[j][i] != '':
                    temp2[index][i] = board[j][i]
                    index -= 1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = temp2[i][j]
    
    def reset_temp():
        for i in range(m):
            for j in range(n):
                temp[i][j] = False
    
    def simulate():
        global answer

        # 1. 지울 수 있는 4개의 칸 구하고 temp에 True로 기록
        find()
        
        # 2. temp에서 True인 개수 구하고 True인 곳을 board에 ''으로 표시
        # answer += True 개수
        cnt = erase()
        answer += cnt
        if cnt == 0:
            return
        
        # 3. 중력 작용
        fall_down()
        
        # temp 초기화
        reset_temp()
        
        return simulate()
        
    simulate()

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
