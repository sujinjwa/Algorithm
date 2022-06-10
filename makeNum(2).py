# 변수 선언 및 입력
a, b, c = tuple(map(int, input().split()))

ans = 0 # cnt 중 최댓값

# a를 몇 회 사용할지 전부 시도
# 모든 경우의 수에 대해 최대가 되도록 하는 수를 계산
for i in range(c // a + 1): # C보다 작은 범위 내에서 A의 사용 횟수는 c // a 넘지 않음
    # a를 i회 사용
    cnt = a * i

    # 값을 최대로 하기 위해 b를 몇회 (num_b) 사용해야 하는지 계산
    num_b = (c - cnt) // b

    cnt += num_b * b
    
    ans = max(ans, cnt) # cnt := i 값마다 a * i + b * num_b 값

print(ans)