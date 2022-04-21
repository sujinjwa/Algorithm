MAX_T = 1000000

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# A가 매 초마다 서있는 위치를 기록
time_a = 1 # 흐른 시간 나타내는 변수
for _ in range(n):
		d, t = tuple(input().split()) # 이동하는 방향 나타내는 변수 d와 이동량 나타내는 변수 t
		for _ in range(int(t)):
				pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
				time_a += 1

# B가 매 초마다 서있는 위치를 기록
time_b = 1
for _ in range(m):
		d, t = tuple(input().split())
		for _ in range(int(t)):
				pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
				time_b += 1

# 최초로 만나는 시간을 구합니다.
ans = -1
for i in range(1, time_a):
		if pos_a[i] == pos_b[i]:
				ans = i
				break

print(ans)