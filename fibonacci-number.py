n = int(input()) # n : 피보나치 수열의 마지막 숫자

dp = [0] * n # dp : 수열에서 이전 두 항의 합으로 다음 항의 값을 구하기 위한 n 길이의 1차원 배열

if n <= 2: # 길이가 2 이하인 피보나치 수열인 경우 피보나치 수로 1 출력
    print(1)
else:
    # 피보나치 수열 중 첫번째 원소와 두번째 원소 1로 선언
    dp[0] = 1
    dp[1] = 1

    # 이전 두 항의 합으로 i번째 항의 값 구하기
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]
    
    # n번째 피보나치 수 출력
    print(dp[n - 1])