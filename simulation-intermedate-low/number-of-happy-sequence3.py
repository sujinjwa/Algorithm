n, m = tuple(map(int, input().split())) # n : 격자의 크기, m : 연속해야 하는 숫자의 개수

# n * n 크기 격자의 각 칸의 정보 입력 받기
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# n 크기의 1차원 배열 초기화
seq = [0 for _ in range(n)]

num_happy = 0 # num_happy : 행복한 수열의 개수

# 내 버전) seq에서 i ~ i + m 까지의 숫자들이 모두 동일한지 확인
def is_happy_sequence():
    for i in range(n - m + 1): # i : seq에서 길이가 m인 수열들 중 첫 번째 숫자
        cnt = 1
        for j in range(i, i + m): # j : seq에서 길이가 m인 수열들 내 모든 숫자 하나씩 조회
            if seq[i] != seq[j]: # 동일한 숫자가 아니면 cnt를 1로 초기화
                cnt = 1
            else:
                cnt += 1
        
        if cnt == m: # 동일한 숫자가 반복된 횟수가 m번인 경우 = 행복한 수열의 조건 만족
            return True
    
    return False

# 해설 버전) seq 내 연속하는 숫자의 개수 세기
def is_happy_sequence2():
    # consecutive_count : seq 내 연속하는 숫자의 개수
    consecutive_count, max_count = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1 # 연속하는 경우 + 1
        else:
            consecutive_count = 1 # 연속하지 않으면 1로 초기화

        # seq 내 숫자 하나씩 조회할 때마다 최대로 연속하는 개수 확인
        max_count = max[max_count, consecutive_count]

    return max_count >= m # 연속하는 개수가 m개 이상인 경우 true 반환

# 가로로 행복한 수열의 수 세기
for i in range(n):
    seq = grid[i][:] # seq : grid의 i번째 행에 위치한 모든 숫자들의 모임

    if is_happy_sequence():
        num_happy += 1

# 세로로 행복한 수열의 수 세기
for i in range(n):
    for j in range(n):
        seq[j] = grid[j][i] # seq : grid의 j번째 열에 위치한 모든 숫자들의 모임

    if is_happy_sequence():
        num_happy += 1

# 행복한 수열의 총 개수 출력
print(num_happy)
