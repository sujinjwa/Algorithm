n, m = tuple(map(int, input().split())) # n : 격자의 크기, m : 금 한 개의 가격

# n * n 격자 내 금이 있는지 여부를 입력 받는다
# 금이 있는 경우 1, 없는 경우 0
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# k번 이내로 이동하여 채굴한 방법의 총 비용 반환
def get_cost(k):
    return k * k + (k + 1) * (k + 1)

# (x, y)가 중심점일 때 k 만큼의 마름모 모양 순회하여
# 금의 개수 반환
def get_num_of_gold(x, y, k):
    sum_of_gold = 0
    for i in range(n):
        for j in range(n):
            if abs(x - i) + abs(y - j) <= k:
                sum_of_gold += grid[i][j]
    
    return sum_of_gold
        

max_num_of_gold = 0
# n * n 격자 내 모든 위치를 순회하며
# 해당 위치가 마름모의 중심점일 때 k = 0 ~ 2(n - 1) 인 경우마다
# 중심점으로부터 k 이내인 모든 위치들을 순회하며 금이 있는지 확인
for x in range(n):
    for y in range(n):
        # 격자의 크기(n)에서 k의 최댓값 = 2 * (n - 1)
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(x, y, k)
            
            # 손해 보지 는 경우 가장 많은 금의 개수 갱신
            if num_of_gold * m >= get_cost(k):
                max_num_of_gold = max(max_num_of_gold, num_of_gold)

# 가장 많은 금의 최종 개수 출력
print(max_num_of_gold)