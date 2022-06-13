n, k = list(map(int, input().split())) # 폭탄 개수 : n개, 특정 거리 : k

bomb = [
    int(input()) # n개의 각 폭탄에 부여된 정수
    for _ in range(n)
]

# 같은 정수가 부여된 폭발끼리 거리가 k 안에 있다면 폭발

# pop : 폭탄 위치 별 터진 횟수
pop = [0] * (n)

for i in range(n): # 폭탄의 두 쌍 (i, j)의 모든 경우 조회
    for j in range(i+1, n):

        dis = j - i # 두 폭탄 간 거리
        if bomb[i] == bomb[j] and dis <= k: # 각 폭탄에 부여된 정수 같고, 서로 k 이내에 위치한다면
            pop[i] += 1 # i번째 폭탄 터지는 횟수 + 1
            pop[j] += 1 # j번째 폭탄 터지는 횟수 + 1

# bomb_num : 각 폭탄 번호(부여된 정수) 별 터진 횟수, index = 폭탄 번호
# 이때, 100은 어림 잡은 범위
bomb_num = [0] * (100)
for i in range(n):
    # i번째 폭탄 터지는 횟수 1보다 크다면, 
    # 해당 폭탄에 부여된 정수 num 번째의 bomb_num 요소에 +1
    if pop[i] >= 1:
        num = bomb[i]
        bomb_num[num] += 1 # 해당 폭탄 번호의 index 위치에 + 1

# max_bomb_num : 폭탄 번호 중 가장 많이 터진 폭탄의 번호
max_bomb_num = 0 
for i in range(1, 100):
    if max(bomb_num) == 0: # 아무 폭탄도 터지지 않을 경우
        max_bomb_num = 0
        break

    if bomb_num[i] == max(bomb_num):
        # 폭발한 폭탄 중 가장 많이 터진 폭탄인 경우
        # 가장 많이 터진 폭탄 여러개인 경우,
        # 가장 큰 번호 출력
        max_bomb_num = i # 해당 폭탄이 지닌 정수 출력

print(max_bomb_num)