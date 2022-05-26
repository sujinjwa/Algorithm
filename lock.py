n = int(input()) # 조합 가능한 최대 숫자 n
a, b, c = tuple(map(int, input().split())) # 주어지는 3자리 숫자의 조합

cnt = 0 # 가능한 서로 다른 조합의 수
# 나올 수 있는 총 조합의 수(n * n * n) 모두 순회하는 반복문
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(i - a) <= 2 or abs(j - b) <= 2 or abs(k - c) <= 2: # 자물쇠가 열릴 수 있는 조건 만족한 경우
                cnt += 1

print(cnt)