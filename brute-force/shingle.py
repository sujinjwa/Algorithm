n = int(input()) # a, b 종이컵 교환 횟수 : n번

cups = [
    list(map(int, input().split())) # a, b, c 입력
    for _ in range(n)
]

max_score = 0 # 

for i in range(1, 4): # 처음 조약돌 넣을 종이컵 1,2,3번일 때 모두 순회

    rock = [0] * 4 # 3개 종이컵 중 조약돌 위치
    rock[i] = 1 # i번째 종이컵에 조약돌 위치한 곳 "1"로 표시 

    score = 0 # 조약돌의 특정 위치일 때 총 점수
    for j in range(n):
        
        a = cups[j][0]
        b = cups[j][1]
        c = cups[j][2]

        # a번 종이컵과 b번 종이컵 교환
        temp = rock[a]
        rock[a] = rock[b]
        rock[b] = temp

        if rock[c] == 1: # c번 종이컵에 조약돌 있을 때
            score += 1
    
    max_score = max(max_score, score)

print(max_score)