n = int(input())

nums = [
    int(input())
    for _ in range(n)
]

ans, cnt = 0, 0
for i in range(n):
    if i >= 1 and (nums[i] * nums[i-1]) > 0: # 연속하는 숫자 2개를 곱한 값이 양수일 때
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)