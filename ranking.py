# 경기 수 : k번, 개발자 수 : n명
k, n = tuple(map(int, input().split()))

# k개의 경기 결과 입력 받기
rank = [
    list(map(int, input().split())) # 각각의 개발자 번호 의미, 입력으로 먼저 주어진 순서대로 순위 높음
    for _ in range(k)
]

cnt = 0 # 조건 만족하는 모든 경우의 수

# 개발자의 모든 (i, j) 쌍 중 모든 경기에서 i가 j보다 더 높은 순위인 경우의 수 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        
        if j == i: # 동일한 개발자일 경우 건너뛰기
            continue

        is_true = True # 조건 충족하는 경우
        for l in range(k): # 모든 경기 순회
        
            if rank[l].index(j) < rank[l].index(i): # j가 i보다 순위 더 높은 경우
                is_true = False
        
        if is_true: # 모든 경기에서 i가 j보다 순위 높은 경우
            cnt += 1

print(cnt)