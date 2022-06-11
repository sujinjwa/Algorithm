# 숫자 최대 범위 : n, 숫자 쌍 : m개
n, m = list(map(int, input().split()))

# m개의 줄에 걸쳐 숫자 쌍의 정보(a, b) 입력 받기
nums = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

max_cnt = 0

# 1 ~ n 사이 숫자로 이루어진 모든 (x, y) 숫자 쌍 조회
for x in range(1, n+1):
    for y in range(1, n+1):

        cnt = 0 # 해당 숫자 쌍 등장한 횟수
        for a, b in nums: # 해당 (x, y) 숫자 쌍이 입력 받은 정보(a, b)와 동일한지 확인
            if (x == a and y == b) or (x == b and y == a) :
                cnt += 1
        
        max_cnt = max(max_cnt, cnt) # 등장한 숫자 쌍 중 최댓값 구하기

print(max_cnt)