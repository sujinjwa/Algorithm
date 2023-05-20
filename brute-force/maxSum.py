import sys
INT_MIN = -sys.maxsize

n = int(input()) # 숫자의 개수
arr = list(map(int, input().split())) # n개의 숫자들 입력 받기

sum_max = INT_MIN # 인접하지 않은 두 숫자 합 중 최댓값
for i in range(n):
    # j가 i+2부터 시작해도 인접하지 않은 모든 두 숫자 조회 가능
    for j in range(i+2, n):
        sum_num = arr[i] + arr[j]
        sum_max = max(sum_max, sum_num) # sum_num 하나씩 조회할 때마다 sum_max와 비교해줘야 함

print(sum_max)