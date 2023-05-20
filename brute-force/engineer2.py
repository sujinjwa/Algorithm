import sys

arr = list(map(int, input().split())) # 개발자 6명의 각 알고리즘 능력 수치화한 정수 입력 받기

min_diff = sys.maxsize # 최대 팀과 최소 팀 간의 차가 최소일 때의 차

# i : 1팀의 첫 번째 개발자, j : 1팀의 두 번째 개발자
# k : 2팀의 첫 번째 개발자, l : 2팀의 두 번째 개발자
for i in range(6):
    sum1 = 0
    for j in range(i+1, 6):
        for k in range(i+1, 6):
            sum2, sum3 = 0, 0
            for l in range(k+1, 6):
                if k == j or l == j: # 2팀의 개발자가 1팀의 두 번째 개발자와 동일할 경우 제외
                    continue
                
                sum1 = arr[i] + arr[j] # 1팀의 능력 총합
                sum2 = arr[k] + arr[l] # 2팀의 능력 총합
                sum3 = sum(arr) - (sum1 + sum2) # 3팀의 능력 총합
                
                max_sum = max(sum1, sum2, sum3) # 능력 최대인 팀의 총합
                min_sum = min(sum1, sum2, sum3) # 능력 최소인 팀의 총합

                min_diff = min(min_diff, max_sum - min_sum) # 최대 팀과 최소 팀 간의 차 중 최소일 때의 차

print(min_diff)