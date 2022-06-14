# 숫자 개수 : n개, 1씩 증가시키는 원소의 개수 : l개
n, l = tuple(map(int, input().split()))
nums = list(map(int, input().split())) # n개의 숫자 배열

max_h = 0 # h 중 최댓값

# n개의 입력 받은 숫자 중 모든 값을 h 점수라 생각하고 하나씩 확인
for h in range(1, n + 1): #in nums:

    cnt = 0 # h보다 큰 숫자의 개수
    plusOne = 0 # +1 한 숫자의 개수

    # # h보다 큰 숫자인 경우 cnt += 1 하고,
    # h보다 작은 숫자인 경우,
    # plusOne < l인 경우에만 cnt +=1 , plusOne += 1 한 후,
    # 마지막에 cnt >= h 인지 확인

    for num in nums:
        if (h - num) == 1: # num이 h보다 1만큼만 작아서, +1 하면 h와 같은 숫자가 될 경우
            if plusOne < l:
                plusOne += 1
                cnt += 1
        elif num >= h: # num가 h보다 큰 경우
            cnt += 1
        # else: # nums[i]가 h보다 1보다 더 차이나게 작은 경우
        #     continue

    if cnt >= h: # and plusOne <= l:
        max_h = max(max_h, h) # max_h = h 로 대체 가능

print(max_h)