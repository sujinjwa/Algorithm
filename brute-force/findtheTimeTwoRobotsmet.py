MAX_T = 1000000

# 변수 선언 및 입력
# 로봇 A가 움직이는 횟수 n, 로봇 B가 움직이는 횟수 m
n, m = tuple(map(int, input().split()))
# 1초마다 로봇 A와 B가 이동하는 위치 저장하는 배열
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)
# 배열의 크기는 1000000까지의 index를 사용할 수 있게 해줘야 하므로, 1을 더 크게 잡아줘야 함

# 로봇 A가 매 초마다 서있는 위치 기록
time_a = 1 # 로봇 A가 총 몇 초동안 이동하는지 나타내는 변수
for _ in range(n):
    # 로봇 A가 t초 만큼 방향 d로 이동함을 입력
    t, d = tuple(input().split())
    # 로봇 A가 t초만큼 방향 d로 이동한 1초마다의 위치를 pos_a 배열에 저장하는 반복문
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1 # 1초 지났으므로 + 1
    
# 로봇 B가 매 초마다 서있는 위치 기록
time_b = 1 # 로봇 B가 총 몇 초동안 이동하는지 나타내는 변수
for _ in range(m):
    # 로봇 B가 t초 만큼 방향 d로 이동함을 입력
    t, d = tuple(input().split())
    # 로봇 B가 t초만큼 방향 d로 이동한 1초마다의 위치를 pos_b 배열에 저장하는 반복문
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1 # 1초 지났으므로 + 1
    
# 두 로봇이 모두 동작을 멈추기 전까지
# 먼저 멈춘 로봇의 마지막 위치를 계속해서 기록함
if time_a < time_b:
    for i in range(time_a, time_b):
        pos_a[i] = pos_a[i - 1]
elif time_a > time_b:
    for i in range(time_b, time_a):
        pos_b[i] = pos_b[i - 1]

# 두 로봇이 새롭게 만나는 횟수 구하기
cnt = 0
time_max = max(time_a, time_b) # 로봇 A와 B 중 총 이동한 시간이 더 많은 시간을 나타내는 변수
# 더 많이 이동한 시간동안 1초마다의 로봇 A와 B의 위치를 확인하는 반복문
for i in range(1, time_max):
    # 바로 직전에는 서로 다른 위치에 있다가 그 다음 번에 같은 위치에 오게 되는 경우
    if pos_a[i] == pos_b[i] and pos_a[i - 1] != pos_b[i - 1]:
        cnt += 1

print(cnt)