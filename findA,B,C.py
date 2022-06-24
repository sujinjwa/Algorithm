nums = list(map(int, input().split())) # 해당 숫자 랜덤한 순서로 입력 받기

nums.sort() # 오름차순 정렬

# 오름차순 정렬 시,
# 가장 작은 숫자는 항상 A,
# 두 번째로 작은 숫자는 항상 B
a = nums[0]
b = nums[1]

# 가장 큰 숫자는 항상 A + B + C 이므로
# C는 끝 숫자 - A - B
c = nums[6] - (a + b)

print(a, b, c)