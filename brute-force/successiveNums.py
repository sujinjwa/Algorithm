pos = list(map(int, input().split()))

cnt = 0 # 두 숫자가 연속하는 횟수
cnt2 = 0 # 두 숫자가 2칸 차이나는 횟수

for i in range(1, 3):
    if abs(pos[i - 1] - pos[i]) == 1: # 연속하는 숫자인 경우
        cnt += 1
    elif abs(pos[i - 1] - pos[i]) == 2: # 두 숫자 간 2칸씩 차이나는 경우
        cnt2 += 1


if cnt == 2: # 모든 숫자가 연속하는 경우
    print(0)
if cnt2 >= 1:
    # 두 숫자 간 2칸씩 차이나는 경우가 하나만 있어도
    # 한 번만 움직이면 된다
    print(1)
if cnt <= 1 and cnt2 == 0:
    # 두 숫자가 연속하는 경우 하나 있더라도
    # 다른 숫자가 연속하지 않은 숫자이면
    # 두 번 움직여야 한다
    print(2)