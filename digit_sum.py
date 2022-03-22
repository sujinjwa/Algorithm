nums = list(map(int, input().split()))

result = 1
for num in nums:
    result *= num

def sum_nums(a):
    if a < 10:
        return a

    return sum_nums(a // 10) + a % 10

answer = sum_nums(result)
print(answer)