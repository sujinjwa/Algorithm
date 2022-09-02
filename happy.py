n, m = list(map(int, input().split())) # n : 격자의 크기, m : 연속하는 숫자의 수
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

happy = 0 # 행복한 수열 총 개수

# grid의 각 행에서 나올 수 있는 행복한 수열 개수 세기
for row in range(n): # row: grid의 모든 행 순회
    
    max_cnt1 = 1 # 각 행에서 행복한 수열 안에 존재하는 동일한 원소의 최대 수
    # 동일한 원소 가장 적을 때 1개이므로 1로 초기화

    # col1 ~ col2 까지 행복한 수열인지 확인
    for col1 in range(n - m + 1):
        cnt = 1 # 연속하는 숫자의 수
        for col2 in range(col1 + 1, n):

            if grid[row][col1] != grid[row][col2]:
                break # 동일한 원소 아닐 경우 바로 다음 col1 ~ col2 확인하러 break
            else:
                cnt += 1 # 동일한 원소일 경우 행복한 수열 내 원소 개수 + 1
        max_cnt1 = max(max_cnt1, cnt) # 각 행 내에서 가장 긴 수열 내 원소개수를 max_cnt1 으로 갱신
    
    if max_cnt1 >= m: # 수열 내 동일한 원소 개수가 m 이상임을 만족할 경우
        happy += 1
        continue # 다음 행 조회하러 continue

# grid의 각 열에서 나올 수 있는 행복한 수열 개수 세기
for col in range(n): # col : grid의 모든 열 순회

    max_cnt2 = 1 # 각 열에서 행복한 수열 안에 존재하는 동일한 원소의 최대 수
    # 동일한 원소 가장 적을 때 1개이므로 1로 초기화

    # row1 ~ row2 까지 행복한 수열인지 확인
    for row1 in range(n - m + 1):
        cnt = 1
        for row2 in range(row1 + 1, n):

            if grid[row1][col] != grid[row2][col]:
                break # 동일한 원소 아닐 경우 바로 다음 row1 ~ row2 확인하러 break
            else:
                cnt += 1 # 동일한 원소일 경우 행복한 수열 내 원소 개수 + 1
        max_cnt2 = max(max_cnt2, cnt) # 각 열 내에서 가장 긴 수열 내 원소개수를 max_cnt2 으로 갱신
            
    if max_cnt2 >= m: # 수열 내 동일한 원소 개수가 m 이상임을 만족할 경우
        happy += 1
        continue # 다음 열 조회하러 continue

print(happy)