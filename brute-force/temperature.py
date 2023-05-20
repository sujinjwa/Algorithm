### 각 장비의 작업량 정의
# 1. 만약 데이터센터의 온도범위가 장비 A가 선호하는 온도 Ta 보다 낮다면 C만큼의 작업량을 수행하고,
# 2. 만약 데이터센터의 온도범위가 장비 A가 선호하는 온도 Ta와 Tb 사이에 있다면 G만큼의 작업량을 수행하고,
# 3. 만약 데이터센터의 온도범위가 장비 A가 선호하는 온도 Tb 보다 높다면 H만큼의 작업량을 수행합니다.

# 장비 개수 : n개, 각 온도별 작업량 : c, g, h
n, c, g, h = tuple(map(int, input().split()))

# 각 장비별 선호하는 온도
temps = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def find_work(i, j): # 온도i 일때 j번째 장비의 작업량 구하는 함수
    # 특정 온도 : i
    # n개의 각 장비 순서 : j

    ta = temps[j][0] # j번째 장비가 선호하는 온도 ta
    tb = temps[j][1] # j번째 장비가 선호하는 온도 tb
    
    if i < ta: # 현재 온도가 Ta보다 낮다면
        return c
    elif i <= tb: # 현재 온도가 온도 Ta와 Tb 사이에 있다면
        return g
    else: # 현재 온도가 Tb보다 높다면
        return h

total_sum = 0
for i in range(0, 1001): # 0부터 1000 사이의 각 온도별 n개의 모든 장비의 작업량 합 구하기
    work = 0 # 온도 i일 때 모든 장비의 작업량
    for j in range(len(temps)):
        work += find_work(i, j)
    total_sum = max(total_sum, work)

print(total_sum)