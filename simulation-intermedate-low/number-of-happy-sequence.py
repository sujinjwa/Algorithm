# n : 격자의 크기, m : 연속해야 하는 숫자의 수
n, m = map(int, input().split())

# grid: n * n 크기의 격자
# 각 칸에는 1 이상 100 이하의 숫자 주어짐
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# grid 내의 각 행이 행복한 수열인지 확인하기 위해
# 각 행에서 m개의 숫자를 포함하는 모든 경우의 수열을 조회
def is_happy_sequence(i, j):
    for k in range(j + 1, j + m):
        if grid[i][j] != grid[i][k]:
            return False
    return True

# grid 내의 각 열이 행복한 수열인지 확인하기 위해
# 각 열에서 m개의 숫자를 포함하는 모든 경우의 수열을 조회
def is_happy_sequence2(i, j):
    for k in range(j + 1, j + m):
        if grid[j][i] != grid[k][i]:
            return False
    return True

# 행복한 수열의 개수
# 행복한 수열 = 연속하여 m개 이상의 동일한 원소 포함하는 수열
count_of_happy_sequence = 0

# n * n 격자 각 행 또는 열을 조회하여 행복한 수열인지 확인
# 시간 복잡도: O(N^2)
for i in range(n):
    is_happy1 = False
    is_happy2 = False
    for j in range(n - m + 1):
        # 각 행의 수열이 행복한 수열인지 확인
        if is_happy_sequence(i, j):
            is_happy1 = True
    
        # 각 열의 수열이 행복한 수열인지 확인
        if is_happy_sequence2(i, j):
            is_happy2 = True
    
    # 각 행 또는 열의 수열이 행복한 수열인 경우
    # count + 1
    if is_happy1:
        count_of_happy_sequence += 1
    
    if is_happy2:
        count_of_happy_sequence += 1

# 2n개 중 행복한 수열의 총 개수 출력
print(count_of_happy_sequence)