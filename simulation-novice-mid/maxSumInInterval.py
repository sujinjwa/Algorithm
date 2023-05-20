import sys

n, k = tuple(map(int, input().split())) 
arr = list(map(int, input().split())) # n개의 숫자 입력 받고 리스트에 저장

max_sum = -sys.maxsize # 최댓값 구하기 위한 변수

# n개의 숫자들 중 모든 연속한 k개의 숫자들의 합 구하는 반복문 
for i in range(n-k+1):
    ans = 0 # arr[i] ~ arr[i+k-1] 까지의 합
    for j in range(i, i+k):
        ans += arr[j]
    max_sum = max(max_sum, ans)

print(max_sum)