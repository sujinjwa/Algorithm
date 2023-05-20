n = int(input()) # n : 격자의 크기

# grid : n * n 크기의 격자이며, 각 칸에 1 또는 0 주어짐
# 1이면 해당 위치에 동전이 있는 것, 0이면 동전이 없는 것
# 공간 복잡도 : O(N^2)
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# x ~ x + 2 행부터 y ~ y + 2 열까지의 3*3 격자 내에서
# 동전의 개수 구하는 함수, O(3*3) = O(9)
def calculate_count_of_coin(x, y):
    count_of_coin = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if grid[i][j] == 1:
                count_of_coin += 1
    
    return count_of_coin

# (x, y) 위치: 가능한 3 * 3 격자 내에서 가장 좌측 상단의 위치
# (x, y) 위치 조회하여 각 3*3 격자 내의 동전 개수 중 최대 개수 구하는 함수
# 시간복잡도: O(N^2)
max_count = 0
for x in range(n - 2):
    for y in range(n - 2):
        count_of_coin = calculate_count_of_coin(x, y)

        # 최대 동전 개수 나올 때마다 max_count에 갱신
        max_count = max(max_count, count_of_coin)

print(max_count)