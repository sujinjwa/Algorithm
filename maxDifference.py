n, k = list(map(int, input().split())) # 원소의 개수 : n개, 최대 차이 값 : k
# n 개의 줄에 걸쳐 한 줄에 하나씩 원소 값 입력 받기
nums = [
    int(input())
    for _ in range(n)
]

MAX_R = max(nums) # 모든 경우 중 어림 잡은 최솟값의 최댓값

max_cnt = 0
for i in range(MAX_R + 1): # 최솟값이 i번째 값인 경우 어림 잡아 MAX_R 될 때까지 모두 조회
    
    cnt = 0 # 최솟값이 i 일 때 최대 최소 원소 간 차이가 k 넘지 않는 원소의 수
    
    for num in nums:

        # i가 최솟값이므로 num이 i보다 커야하고,
        # num 과 i 간의 차가 k 이하여야 한다
        
        if num >= i and (num - i) <= k:
            cnt += 1
        
    max_cnt = max(max_cnt, cnt)

print(max_cnt)