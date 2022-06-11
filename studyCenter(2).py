n = int(input()) # 좌석의 개수 : n개
seat = list(input()) # n개의 좌석 공석 여부 입력 받기

def min_dist():
    dist = n

    # 둘 다 1인 곳에 대해
    # 모든 쌍을 조사하여, 그 중 가장 가까운 거리 구한다
    for i in range(n):
        for j in range(i + 1, n):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i) # 가장 가까운 거리 구하기
    
    return dist

ans = 0

# 들어갈 위치를 일일이 정해보며
# 그 상황에서 가장 가까운 사람 간의 거리 구해
# 가능한 경우 중 최댓값 계산한다
for i in range(n):
    if seat[i] == '0':
        # 비어있는 위치에 인원 배치
        seat[i] = '1'

        # 가장 가까운 사람 간의 거리 구해 최댓값 갱신
        ans = max(ans, min_dist())

        # 채워졌던 인원 초기화함
        seat[i] = '0'
