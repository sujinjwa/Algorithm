T = int(input())

def solution():
    n = int(input())
    
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    
    result1 = [
    	[0 for _ in range(n)]
    	for _ in range(n)
    ]
    
    for col in range(n - 1, -1, -1):
        for row in range(n):
            result1[row][col] = grid[n - 1 - col][row]
    
    result2 = [
        [0 for _ in range(n)]
    	for _ in range(n)
    ]
    
    for row in range(n - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            result2[row][col] = grid[n - 1 - row][n - 1 - col]
    
    result3 = [
        [0 for _ in range(n)]
    	for _ in range(n)
    ]
    
    for col in range(n):
        for row in range(n - 1, -1, -1):
            result3[row][col] = grid[col][n - 1 - row]
    
    for row in range(n):
        for col in range(n):
            print(result1[row][col], end = '')
        
        print(' ', end='')
        
        for col in range(n):
            print(result2[row][col], end = '')
        print(' ', end='')
        
        for col in range(n):
            print(result3[row][col], end = '')
        print()

for test_case in range(1, T + 1):
    print("#%d"%test_case)
    solution()