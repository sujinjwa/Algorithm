MAX_A = 10000

# 숫자의 개수 : n개, 칸막이로 나뉜 구간의 수 : m개
n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split())) # n개의 숫자 입력 받기

ans = 0
# 구간의 합의 최댓값을 i라고 할 때,
# 최댓값 i가 맞고,
# 구간의 개수 m인 게 맞는지 확인
for i in range(1, MAX_A + 1):
    
    possible = True # 구간 나눌 수 있으면 true
    cnt_m = 1 # 첫 숫자부터 구간 1개에 포함되므로 시작은 0이 아니라 1부터! 구간의 개수
    cur_sum = 0 # 숫자의 합

    for j in range(n):

        if nums[j] > i:
            # 최댓값 i보다 nums[j]가 더 큰 경우 하나라도 있으면
            # i는 최댓값 될 수 없음
            possible = False
            break
        
        # j번째 숫자 더했을 때 i보다 커지면
        # j번째 숫자부터 다음 구간으로 만들기
        if cur_sum + nums[j] > i:
            # >= 가 아니라 > 여야 함
            # 같은 경우까지는 해당 구간에 nums[j] 포함될 수 있기 때문
            cur_sum = 0
            cnt_m += 1

        # 이번 구간에 j번째 숫자 더하기
        cur_sum += nums[j]
    
    if possible and cnt_m <= m: # i가 최댓값이 될 수 있고, 구간의 개수 m개 이하인 게 맞다면
        ans = i
        break # 가장 먼저 ans로 정의된 i 값이 i 중 최솟값이므로, 바로 break 하면 됨

print(ans)