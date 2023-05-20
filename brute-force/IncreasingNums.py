n = int(input()) # 입력할 숫자의 개수 나타내는 변수 n

# n개의 줄에 걸쳐 숫자 하나씩 arr배열에 입력하기
arr = [
    int(input())
    for _ in range(n)
]

# 원소의 숫자가 연속해서 증가하는 횟수를 나타내는 변수 cnt
# cnt들 중 가장 최대값을 구하기 위한 변수 ans
ans, cnt = 0, 1
for i in range(n):
    if i >= 1 and arr[i-1] < arr[i]: # 원소의 숫자가 연속해서 증가할 경우
        cnt += 1
    else: # 연속한 숫자끼리 감소되는 경우
        cnt = 1

    ans = max(ans, cnt) # ans와 cnt 중 더 큰 값을 ans로 설정

print(ans) # 연속해서 증가하는 횟수 중 최대값인 ans 출력