import sys

min_moving = sys.maxsize # 모든 사람들의 최소 이동 거리

n = int(input()) # 집의 개수
# 각 집에 살고 있는 사람의 수
A = list(map(int, input().split()))

for i in range(n):
    # i = 모이는 집의 idx
    sum_moving = 0 # 모든 사람들의 이동 거리의 합
    for j in range(n):
        sum_moving += abs(i - j) * A[j] # 모이는 집[i]와 다른 집[j]간의 거리 * 다른 집[j]에 사는 사람 수
    
    min_moving = min(min_moving, sum_moving)

print(min_moving)

## moving이라는 이름보다, dist라는 이름 사용하기
## sys.maxsize 사용할 때는 상수임을 나타내기 위해 INT_MAX 이름 사용하기