n = int(input())
a1, b1, c1 = tuple(map(int, input().split())) # 첫 번째 조합
a2, b2, c2 = tuple(map(int, input().split())) # 두 번째 조합

# 모든 자리의 수 (i, j, k)가 주어진 첫 번째 조합 (a1, b1, c1)과의 거리가 2 이내인지 확인하는 함수
def config_first(i, j, k):
    return (abs(a1 - i) <= 2 or abs(a1 - i) >= (n - 2)) and (abs(b1 - j) <= 2 or abs(b1 - j) >= (n - 2)) and (abs(c1 - k) <= 2 or abs(c1 - k) >= (n - 2))

# 모든 자리의 수 (i, j, k)가 주어진 두 번째 조합(a2, b2, c2)과의 거리가 2 이내인지 확인하는 함수
def config_second(i, j, k):
   return (abs(a2 - i) <= 2 or abs(a2 - i) >= (n - 2)) and (abs(b2 - j) <= 2 or abs(b2 - j) >= (n - 2)) and (abs(c2 - k) <= 2 or abs(c2 - k) >= (n - 2))

# 모든 조합 다 만들어 보는 반복문
cnt = 0 # 조합의 경우의 수
for i in range(1, n+1):
    for j in range(1, n+1): # i+1부터 시작하는 게 아닌 1부터 시작
        for k in range(1, n+1):
            # 모든 자리가 주어진 첫 번째 조합(a1, b1, c1)과의 거리가 2 이내인지 확인
            if config_first(i, j, k):
                cnt += 1
            # 모든 자리가 주어진 두 번째 조합(a2, b2, c2)과의 거리가 2 이내인지 확인
            # elif 로 설정하여, config_first 함수 조건에 만족하면 config_second 함수는 실행되지 않게 함
            elif config_second(i, j, k):
                cnt += 1

print(cnt)