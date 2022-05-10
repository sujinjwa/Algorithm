import sys
INT_MAX = sys.maxsize

n = int(input()) # 체크 포인트

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_dis = INT_MAX # 마라톤 완주하는 최소 거리
for i in range(1, n-1):
    # 제외할 체크 포인트의 index := i
    dis = 0 # 구할 거리
    prev_idx = 0
    for j in range(1, n):
        if j == i: # j가 제외할 체크포인트의 index일 경우
            continue
        # 체크포인트 간의 거리 더해주기
        dis += abs(points[prev_idx][0] - points[j][0]) + abs(points[prev_idx][1] - points[j][1])
        prev_idx = j # j == i 일때 prev_idx = j로 갱신되지 않으므로, i - 1번째 체크포인트부터 i + 1번째 체크포인트까지의 거리 구할 수 o

    min_dis = min(min_dis, dis) # 여러 경우의 수 중 최소 거리 구하기

print(min_dis)