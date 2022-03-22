n = int(input())
nums = list(map(int, input().split()))

def max_func(a):
    if a == 0: # nums가 길이가 1인 문자일 경우
        return nums[0]
    
    return max(max_func(a - 1), nums[a])

print(max_func(n - 1))