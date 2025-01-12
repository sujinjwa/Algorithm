# n : 도시의 개수
n = int(input())

# 인접한 두 도시 연결하는 도로의 길이
distances = list(map(int, input().split()))

# 각 도시 내 주유소의 리터당 가격
costs = list(map(int, input().split()))

min_cost = 0            

i = 0 # 현재 조회중인 도시
while True:

    if i >= len(costs) - 1:
        break

    # 다음 도시들 중에서 주유가격이 더 작은 곳 찾기
    for j in range(i + 1, len(costs)):
        min_cost += costs[i] * distances[j - 1]

        if j == len(costs) - 1:
            i = j
            break

        if costs[i] > costs[j]:
            i = j
            break
    
        
print(min_cost)