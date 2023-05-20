MAX_NUM = 10
UNDEFINED = -1

n = int(input()) # n : 비둘기 관찰 횟수
movements = [
    list(map(int, input().split())) # 몇 번 비둘기가 어느 위치에 있었는지
    for _ in range(n)
]

# 현재 비둘기의 위치 기록
# UNDEFINED 이면 아직 미정인 상태,
# 초기 값 모두 UNDEFINED로 설정
pos = [UNDEFINED] * 11

move_cnt = 0 # 1 ~ 10번 비둘기들이 도로 건넌 횟수

# 입력으로 주어진 움직임에 따라
# 비둘기 위치 이동
for pigeon, move_dir in movements:
    # 해당 비둘기의 위치가 미정이라면
    if pos[pigeon] == UNDEFINED:
        # 주어진 첫 번째 위치에서 비둘기의 위치 시작된다고
        # 생각하는 게 비둘기의 이동 횟수 최소로 하는 방법
        pos[pigeon] = move_dir

    # 해당 비둘기의 이미 위치 정해져 있는데,
    # 옮겨간 위치와 다른 위치라면
    elif pos[pigeon] != move_dir: 
        pos[pigeon] = move_dir # 이동하기
        move_cnt += 1 # 답 갱신

print(move_cnt)