n = int(input())
nums = list(map(int, input().split()))

nums.sort()

max_sum = 0
for i in range(2*n):
    sum_ = nums[i] + nums[2*n-i-1]
    if max_sum < sum_:
        max_sum = sum_

print(max_sum)