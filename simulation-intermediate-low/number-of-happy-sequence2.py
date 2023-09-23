n, m = tuple(map(int, input().split())) # n : 격자의 크기, m : 연속해야 하는 숫자의 개수

# n * n 크기의 격자에서 각 칸의 정보 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 행복한 수열의 개수
# 행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
count_of_happy_seq = 0

# grid 격자에서 각 행이 행복한 수열인지 확인하는 함수
def is_happy_row(i, j):
    for k in range(j, j + m): # k : 같은 행에서 m개의 연속하는 열의 숫자들을 하나씩 조회
        if grid[i][j] != grid[i][k]:
            return False
    
    return True

# grid 격자에서 각 열이 행복한 수열인지 확인하는 함수
def is_happy_col(i, j):
    for k in range(j, j + m): # k : 같은 열에서 m개의 연속하는 행의 숫자들을 하나씩 조회
        if grid[j][i] != grid[k][i]:
            return False
    
    return True
    

# i번째 행의 j번째 열부터 시작하는 수열이 행복한 수열인지 확인
for i in range(n):
    for j in range(n - m + 1): # j : i번째 행의 각 열에서 연속하는 숫자들의 수열 중 첫번째 숫자

        if is_happy_row(i, j):
            count_of_happy_seq += 1
            break # 해당 행이 행복한 수열인 경우 바로 다음 행 조회

# i번째 열의 j번째 행부터 시작하는 수열이 행복한 수열인지 확인
for i in range(n):
    for j in range(n - m + 1): # j : i번째 열의 각 행에서 연속하는 숫자들의 수열 중 첫번째 숫자
        
        if is_happy_col(i, j):
            count_of_happy_seq += 1
            break # 해당 열이 행복한 수열인 경우 바로 다음 열 조회

# 행복한 수열의 총 개수 출력
print(count_of_happy_seq)