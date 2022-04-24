MAX_T = 1000000

n, m = tuple(map(int, input().split()))
pos_A, pos_B = [0] * (MAX_T + 1), [0] * (MAX_T + 1) # 이게 맞는지 잘 몰겠다

time_a = 1
# A가 N번에 걸쳐 주어지는 특정 시간(t) 동안의 속도(v) 입력 받기
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        # 1시간 동안 이동한 거리 구하기
        pos_A[time_a] = pos_A[time_a - 1] + v
        time_a += 1

time_b = 1
# B가 N번에 걸쳐 주어지는 특정 시간(t) 동안의 속도(v) 입력 받기
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        # 1시간 동안 이동한 거리 구하기
        pos_B[time_b] = pos_B[time_b - 1] + v
        time_b += 1

# leader: A와 B 중 더 앞서 있는 경우 확인
# ans: 선두가 몇 번 바뀌는지 횟수 나타내는 변수
leader, ans = 0, 0
for i in range(1, time_b):
    if pos_A[i] > pos_B[i]:
        # 기존 리더가 B였다면
        # 답 갱신
        if leader == 2:
            ans += 1

        # 리더를 A로 변경
        leader = 1

    elif pos_A[i] < pos_B[i]:
        # 기존 리더가 A였다면
        # 답 갱신
        if leader == 1:
            ans += 1
        
        # 리더를 B로 변경
        leader = 2

print(ans)