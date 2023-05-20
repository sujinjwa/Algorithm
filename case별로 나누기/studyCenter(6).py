import sys

INT_MAX = sys.maxsize

n = int(input())
seats = list(input())

# Step1-1. 최적의 위치 찾기
# 인접한 쌍들 중 가장 먼 1 간의 쌍 찾기
max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                # 1간의 쌍을 골랐을 때
                # 두 좌석 간의 거리가 지금까지의 최적의 답 보다 더 좋다면
                # 값을 갱신한다
                if j - i > max_dist:
                    max_dist = j - i
                
                    # 이때, 두 좌석의 위치 기억한다
                    max_i, max_j = i, j
                
                # 인접한 쌍을 찾았으므로 빠져나온다
                break

# Step1-2. 최적의 위치 찾기 (예외 처리)
# 만약 맨 앞 좌석이 비거나, 맨 뒷 좌석이 비어있는 경우의
# 예외 처리 해준다
max_dist2 = -1
max_idx = -1
# 맨 앞 좌석이 비어있을 때, 맨 앞 좌석에 배정하면
# 거리가 얼마나 줄어드는지 확인한다
if seats[0] == '0':
    dist = 0
    for i in range(1, n):
        if seats[i] == '1':
            break
        dist += 1

    if dist > max_dist2:
        max_dist2 = dist
        max_idx = 0

# 맨 뒷 좌석이 비어있을 때, 맨 뒷 좌석에 배정하면
# 거리가 얼마나 줄어드는지 확인한다
if seats[n - 1] == '0':
    dist = 0
    for i in range(n - 2, -1, -1):
        if seats[i] == '1':
            break
        dist += 1
    
    if dist > max_dist2:
        max_dist2 = dist
        max_idx = n - 1

# Step2. 최적의 위치에 1 놓는다
# 앞서 찾은 자리들 중 최적의 위치에 놓으면 된다
if max_dist2 >= max_dist // 2:
    seats[max_idx] = '1'
else:
    seats[(max_i + max_j) // 2] = '1'

# Step3. 이제 인접한 쌍들 중 가장 가까운 1 간의 쌍 찾는다
# 이때의 값이 답이 된다
ans = INT_MAX
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)

                # 인접한 쌍 찾았으므로 빠져 나온다
                break

print(ans)