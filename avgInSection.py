n = int(input())
arr = list(map(int, input().split()))

cnt = 0 # 특정 구간 내 원소들의 평균값이 그 구간의 원소 중 하나가 되는 가짓수

for i in range(n): # 특정 구간 중 시작하는 index := i
    for j in range(i, n): # 특정 구간 중 끝나는 index := j

        sum_val = 0 # 특정 구간 내 원소들의 합 나타내는 변수
        for k in range(i, j+1): # 구간 i ~ j 까지 순회하는 반복문
            sum_val += arr[k]
        avg = sum_val / (j - i + 1) # 해당 구간 내 원소들의 평균값 구하기

        # 평균값이 특정 구간의 원소 중 하나와 동일한 경우
        for k in range(i, j+1):
            if avg == arr[k]:
                cnt += 1
                break

print(cnt)