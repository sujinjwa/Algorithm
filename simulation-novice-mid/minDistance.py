import sys
INT_MAX = sys.maxsize

n = int(input()) # 방의 개수
# n개의 각 방에 들어가야 하는 사람들의 수
house = [
    int(input())
    for _ in range(n)
]

min_dist = INT_MAX

# 각 i번째 집으로 모였을 때 합 구하기
for i in range(n):
    sum_dist = 0
    for j in range(n):
        dist = (j + n - i) % n # i번째 집에서 출발한 방향으로 다시 돌아간 j번째 집으로부터의 거리
        sum_dist += dist * house[j]
    
    min_dist = min(sum_dist, min_dist)

print(min_dist)