MAX_A = 100

n = int(input())
section = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 3개의 선분 모두 골라보면서
# 모두 겹쳐지지 않도록 하는 가짓수 구하기
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # i, j, k번 선분 제외했을 때
            # 모든 선분 겹치지 않으면 ans + 1
            
            # overlap : 모든 선분이 겹치지 않으면 false
            overlap = False
            arr = [0] * (MAX_A + 1) # 0으로 초기화된 길이 100인 1차원 직선 배열

            for x in range(n):
                if x == i or x == j or x == k: # i, j, k번 선분 제외
                    continue

                for y in range(section[x][0], section[x][1] + 1): # n-3개의 나머지 선분 위치에 +1
                    arr[y] += 1
            
            for x in range(MAX_A + 1):
                if arr[x] > 1:
                    overlap = True # 선분 겹치는 경우 한 번이라도 있을 경우
            
            if overlap == False: # 모든 선분 겹치지 않으면
                ans += 1

print(ans)