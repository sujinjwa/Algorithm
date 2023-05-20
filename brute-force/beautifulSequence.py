n, m = tuple(map(int, input().split()))

A = list(map(int, input().split())) # n개의 숫자로 이루어진 수열 A 입력 받기
B = list(map(int, input().split())) # m 개의 숫자로 이루어진 수열 B 입력 받기

cnt = 0 # 아름다운 수열의 수
for i in range(0, n - m + 1): # 수열 A에서 out of range 하지 않기 위해 n - m + 1 까지만 순회하는 반복문
    # A에서 B의 길이만큼의 모든 구간 찾아 sort2 
    if sorted(A[i:i+m]) == sorted(B):
        cnt += 1

print(cnt)