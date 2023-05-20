n, m, k = list(map(int, input().split()))
# n : 턴의 수 (= 주어지는 숫자의 개수)
# m : 윷놀이 판의 상태(길이)
# k : 말의 수

move = list(map(int, input().split()))
# move : n번의 각 턴마다 말이 이동하는 범위

horses = [0] * k # 각 말의 이동 위치

# arr = [0] * m # 윷놀이 판
max_cnt = 0 # 최대로 얻을 수 있는 점수
cnt = 0

# 해당 턴일 때 얻은 점수가 최대 점수인지 확인
def is_max_cnt(cnt):
    global max_cnt

    if max_cnt < cnt:
        max_cnt = cnt

# turn := 턴의 각 순서
# turn 번째 턴일 때 1 ~ k 중 움직이는 말 선택
def choose(turn):

    global cnt

    # 종료 조건: 턴의 수 초과했을 때
    if turn == n:

        for horse in horses:
            if horse >= m - 1:
                cnt += 1

        is_max_cnt(cnt)
        cnt = 0 # 초기화
        return
    
    # 1 ~ k 번째 말 중 움직일 말 선태
    for i in range(k):
        # move = [2 4 2 4]
        # horses = [0 0 0] -> 3마리

        # i번째 말에 turn번째의 이동 범위 더해주기
        horses[i] += move[turn]
        choose(turn + 1)
        horses[i] -= move[turn]
    
    return

choose(0)

print(max_cnt)