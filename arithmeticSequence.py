n = int(input()) # 숫자 개수 : n
nums = list(map(int, input().split())) # n개의 숫자 입력 받기

max_cnt = 0
for k in range(1, 101): # 1 ~ 100까지의 모든 자연수 k로 선정하여, (nums[i], nums[j]) 조합과 비교
    cnt = 0
    for i in range(n):
        for j in range(i+1, n): # 서로 다른 수인 (nums[i], nums[j]) 조합의 모든 경우의 수 순회
            
            if nums[i] <= nums[j]: # 두 수의 차가 양수인 경우
                if (nums[j] - k) == (k - nums[i]): # i, k, j가 등차수열인 경우
                    cnt += 1
            else: # 두 수의 차가 음수인 경우
                if (nums[j] - k) == (k - nums[i]): # i, k, j가 등차수열인 경우
                    cnt += 1
        
    max_cnt = max(max_cnt, cnt)

print(max_cnt)