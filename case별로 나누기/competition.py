n = int(input()) # 점수 변동 목록의 수
honors = [
    list(input().split())
    for _ in range(n)
]

score_a, score_b = 0, 0 # A와 B의 초기 점수

last_winner = 0 # 이전 우승자
cur_winner = 0 # 현재 우승자
cnt = 0 # 명예의 전당 조합 바뀌는 횟수

for c, s in honors:
    # c : 점수가 1등인 사람
    # s : 점수 변동값
    s = int(s)
    last_winner = cur_winner # 이전 승부에서 승리한 사람을 last_winner로 초기화

    # 점수 얻은 만큼 승리한 사람의 총 점수에 더해 주기
    if c == 'A':
        score_a += s
    else:
        score_b += s
    
    # A와 B 중 총 점수가 더 높은 사람이 cur_winner
    # 1이면 A가 승리, 2이면 B가 승리, 0 이면 무승부
    if score_a > score_b:
        cur_winner = 1
    elif score_a < score_b:
        cur_winner = 2
    else:
        cur_winner = 0
    
    # 명예의 전당에 올라간 사람의 조합이 이전 승부 때와 바뀐 경우
    if last_winner != cur_winner:
        cnt += 1

print(cnt)