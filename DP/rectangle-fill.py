n = int(input()) # n : 사각형의 가로의 길이

MAX_NUM = 1000 # n의 최대로 가능한 수

dp = [-1] * (MAX_NUM + 1)

# 사각형 가로의 길이가 1,2,3일 때의 
# 사각형 채우는 서로 다른 방법의 수 초기화
dp[1] = 1
dp[2] = 2
dp[3] = 3

# 사각형 가로의 길이가 4 ~ n 일 때
# 사각형 채우는 서로 다른 방법의 수 점화식으로 구하기
for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# 2 * n 크기의 사각형 채우는 방법의 수를 10,007로 나눈 나머지 출력
print(dp[n] % 10007)