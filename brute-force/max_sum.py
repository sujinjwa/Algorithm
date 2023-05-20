x, y = tuple(map(int, input().split()))

ans = 0
for i in range(x, y+1): # x부터 y 사이의 숫자들 중 각 자리 숫자의 합이 최대인 숫자 구하기
    arr = list(str(i)) # 숫자 i의 각 자리 숫자들이 elements 구성된 배열 arr 생성

    sum_ = 0
    for num in arr:
        sum_ += int(num) # 각 자리 숫자의 합
    
    ans = max(ans, sum_)

print(ans)