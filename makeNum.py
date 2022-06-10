a, b, c = list(map(int, input().split()))

max_sum = 0
for i in range(1000): # a를 사용한 횟수 : i 번

    diff_sum = 0
    for j in range(1000): # b를 사용한 횟수 : j 번
        
        diff_sum = a * i + b * j 
        
        if diff_sum <= c: # a와 b를 이용한 diff_sum이 c보다 작거나 같다면
            max_sum = max(max_sum, diff_sum)
    
print(max_sum)