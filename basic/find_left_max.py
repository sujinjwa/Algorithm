n = int(input())
a = list(map(int, input().split()))

# 처음 for문 돌 때는 전체 중 최댓값 구해야하므로, n으로 설정
prev_max_idx = n

# 첫 번째 원소가 최대가 되기 전까지 계속 반복
while True:
    max_idx = 0

    # 두 번째 원소부터 바로 직전에 최댓값으로 뽑힌
    # 원소 전까지 보면서 그 중 최대 index 갱신
    # index를 오름차순으로 보기 때문에 최댓값 여러개인 경우 가장 왼쪽 원소 뽑힘
    for i in range(1, prev_max_idx):
        if a[i] > a[max_idx]:
            max_idx = i
    
    print(max_idx + 1, end=" ")

    # 최댓값이 첫 번째 원소라면 while문 종료
    if max_idx == 0:
        break

    # 바로 직전 최댓값의 index 갱신
    prev_max_idx = max_idx