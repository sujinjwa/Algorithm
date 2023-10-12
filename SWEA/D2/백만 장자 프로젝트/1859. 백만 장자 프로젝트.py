def solution():
    n = int(input()) # n : 총 날짜 수
    
    # prices : 각 날짜별 매매가
    prices = list(map(int, input().split()))

    benefit = 0 # 총 이익

    max_index = 0
    max_num = 0
    start_index = 0

    while True:
        max_num = 0
        max_index = 0

        if start_index == len(prices) - 1:
            break

        for i in range(start_index, len(prices)):
            if max_num <= prices[i]:
                max_num = prices[i]
                max_index = i

        if max_num == prices[start_index]: # 이제 이익 날 게 없음
            start_index += 1
            continue

        for i in range(start_index, max_index):
            benefit += (max_num - prices[i]) # 이익 더해주기

        if max_index == len(prices) - 1:
            break

        # start_index 갱신
        start_index = max_index + 1

    # 출력
    return benefit

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    print("#%d"%i, solution())