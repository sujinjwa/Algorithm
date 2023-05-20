MAX_T = 1000000 # 주어진 T의 단위가 1 <= t <= 1,000 이므로

n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1) , [0] * (MAX_T + 1)

time_a = 1 # 흐른 시간을 나타내는 변수
# A가 매 초마다 서있는 위치 기록하기 위한 반복문
for _ in range(n):
    d, t = input().split()
    for _ in range(int(t)):
        # 1초 전 위치(pos_a[time_a - 1]에서 입력받은 d가 R이면 +1을, L이면 -1을 더해줌
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1 # 1초 흘렀음을 나타내기 위해 +1

time_b = 1
# B가 매 초마다 서있는 위치 기록하기 위한 반복문
for _ in range(m):
    d, t = input().split()
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

# 최초로 만나는 시간 구하기
ans = -1
for i in range(1, time_b):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)