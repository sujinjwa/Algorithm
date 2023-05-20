import sys

arr = list(map(int, input().split())) # 개발자 6명의 각 알고리즘 능력 수치화환 배열

def get_diff(i, j, k):
    sum1 = arr[i] + arr[j] + arr[k] # (i, j, k)의 3명으로 구성된 1팀의 능력 총합
    sum2 = sum(arr) - sum1 # 전체 총합에서 1팀의 합 뺀 2팀의 능력 총합
    return abs(sum1 - sum2) # 1팀과 2팀의 능력 총합 간의 차이

min_diff = sys.maxsize # 팀원들의 능력 총합 간의 최소 차

# 6명의 개발자 중 3명으로 구성되는 팀의 모든 조합 순회하는 반복문
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)