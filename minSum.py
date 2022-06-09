# 중첩 완전 탐색 문제
import sys

n = int(input())
nums = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(n): # nums 내 숫자 하나씩 순회
    
    nums[i] *= 2 # i번째 숫자 2배

    for j in range(n):

        new_nums = []

        for k, elem in enumerate(nums):
            
            # j번째 숫자 제외한 모든 숫자 new_nums 배열에 append
            if k != j:
                new_nums.append(elem)

        diff_sum = 0
        for l in range(1, len(new_nums)):
            diff_sum += abs(new_nums[l - 1] - new_nums[l]) # 인접한 두 숫자간 차이의 합

        min_sum = min(min_sum, diff_sum) # 합의 최솟값 구하기
    
    nums[i] //= 2 # 2배한 i번째 숫자 초기화

print(min_sum)